class Elevator:
    def __init__(self, eid, capacity):
        self.id = eid
        self.capacity = capacity
        self.current_floor = 1
        self.direction = 0  # -1 = down, 1 = up, 0 = idle
        self.passengers = []
        self.pickup_queue = []

    def move(self):
        # Determine direction
        if not self.passengers and not self.pickup_queue:
            self.direction = 0
            return

        all_floors = [p.dest for p in self.passengers] + [p.source for p in self.pickup_queue]
        if not all_floors:
            self.direction = 0
            return

        target = max(all_floors) if self.current_floor < max(all_floors) else min(all_floors)
        if self.current_floor < target:
            self.current_floor += 1
            self.direction = 1
        elif self.current_floor > target:
            self.current_floor -= 1
            self.direction = -1
        else:
            self.direction = 0