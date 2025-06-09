from elevator import Elevator
import logging
import csv
import statistics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("elevator.log"),
        logging.StreamHandler()
    ]
)

class Scheduler:
    def __init__(self, nelevators=3, floors=100, capacity=4):
        self.elevators = [Elevator(i, capacity) for i in range(nelevators)]
        self.floors = floors
        self.time = 0
        self.passengers = {}
        logging.info(f"Scheduler Initialised with {nelevators} elevators, {floors} floors, capacity {capacity}")

    def _assign_passenger(self, passenger):
        best = None
        best_eta = float('inf')

        for elev in self.elevators:
            if len(elev.passengers) + len(elev.pickup_queue) >= elev.capacity:
                continue

            if elev.direction == 0:  # idle
                eta = abs(elev.current_floor - passenger.source)
            else:
                active_floors = [p.dest for p in elev.passengers] + [p.source for p in elev.pickup_queue]
                if not active_floors:
                    eta = abs(elev.current_floor - passenger.source)
                else:
                    farthest = max(active_floors) if elev.direction == 1 else min(active_floors)
                    eta = abs(elev.current_floor - farthest) + abs(farthest - passenger.source)

            if eta < best_eta:
                best_eta = eta
                best = elev

        if best:
            best.pickup_queue.append(passenger)
            logging.info(f"Passenger {passenger.id} assigned to elevator {best.id} (from {passenger.source} to {passenger.dest})")
            return True
        else:
            logging.warning(f"Passenger {passenger.id} could not be assigned to any elevator at time {self.time}")
            return False

    def run(self, requests, output_file="elevator_positions.csv"):
        requests = sorted(requests, key=lambda x: x.time)
        pending = requests
        log = []
        passenger_done = {}

        while pending or any(e.passengers or e.pickup_queue for e in self.elevators):
            # 1. Log elevator positions
            log.append([self.time] + [e.current_floor for e in self.elevators])
            logging.debug(f"Time {self.time}: Elevator positions: {[e.current_floor for e in self.elevators]}")

            # 2. Process new requests
            new_requests = [r for r in pending if r.time == self.time]
            for r in new_requests:
                self._assign_passenger(r)
                self.passengers[r.id] = r
                logging.info(f"New request: Passenger {r.id} at floor {r.source} to {r.dest} at time {r.time}")
            pending = [r for r in pending if r.time > self.time]

            # 3. Move elevators
            for elev in self.elevators:
                # Drop off
                dropped = [p for p in elev.passengers if p.dest == elev.current_floor]
                for p in dropped:
                    p.dropoff_time = self.time
                    passenger_done[p.id] = p
                    logging.info(f"Passenger {p.id} dropped off by elevator {elev.id} at floor {elev.current_floor} at time {self.time}")
                elev.passengers = [p for p in elev.passengers if p.dest != elev.current_floor]

                # Pick up
                to_pick = [p for p in elev.pickup_queue if p.source == elev.current_floor]
                to_pick = to_pick[:elev.capacity - len(elev.passengers)]
                for p in to_pick:
                    p.pickup_time = self.time
                    logging.info(f"Passenger {p.id} picked up by elevator {elev.id} at floor {elev.current_floor} at time {self.time}")
                elev.passengers.extend(to_pick)
                elev.pickup_queue = [p for p in elev.pickup_queue if p not in to_pick]

                # Move elevator
                elev.move()
                logging.debug(f"Elevator {elev.id} moved to floor {elev.current_floor}")

            # 4. Advance time
            self.time += 1

        # Write elevator position log
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["time"] + [f"elevator_{e.id}" for e in self.elevators])
            writer.writerows(log)
        logging.info(f"Elevator positions written to {output_file}")

        # Write summary stats
        wait_times = [(p.pickup_time - p.time) for p in passenger_done.values()]
        total_times = [(p.dropoff_time - p.time) for p in passenger_done.values()]

        logging.info(f"Total passengers served: {len(passenger_done)}")
        logging.info(f"Wait Time: min={min(wait_times)}, max={max(wait_times)}, mean={statistics.mean(wait_times):.2f}")
        logging.info(f"Total Time: min={min(total_times)}, max={max(total_times)}, mean={statistics.mean(total_times):.2f}")

        print("\n--- Summary Statistics ---")
        print(f"Total passengers served: {len(passenger_done)}")
        print(f"Wait Time: min={min(wait_times)}, max={max(wait_times)}, mean={statistics.mean(wait_times):.2f}")
        print(f"Total Time: min={min(total_times)}, max={max(total_times)}, mean={statistics.mean(total_times):.2f}")

        print("\nWait Time Distribution:")
        for t in sorted(set(wait_times)):
            print(f"  {t} unit(s): {wait_times.count(t)} passenger(s)")

        print("\nTotal Time Distribution:")
        for t in sorted(set(total_times)):
            print(f"  {t} unit(s): {total_times.count(t)} passenger(s)")