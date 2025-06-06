'''
Author: Luke O'Brien
File Description: Main file for Elevator Program
Tests: tests.main.py
'''

import csv


def csvReader(filename):
    """Reads a CSV file and returns its contents as a list of dictionaries."""
    # Read the data.csv file
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)  # Use DictReader to parse rows into dictionaries
            return [row for row in csv_reader]  # Convert rows into a list of dictionaries

    except FileNotFoundError:
        print("Error: data.csv file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """Main function to execute the program."""
    # Parsed user data
    data = csvReader('data.csv')  # Read the CSV file
    # Hardcoded values cause no example was provided
    elevators = 3
    floors = 51
    # Return a table of all elevators and their floor at every point in time
    compute(data, elevators, floors)

    print(data)

def compute(data, elevators, floors):
    """Computes the elevator data based on the input parameters."""
    # Initialize elevator positions (all start at floor 1)
    elevator_positions = [1] * elevators
    time = 0  # Start at time 0

    # Create a log to track elevator movements
    movement_log = []
    requestTimes = [x['time'] for x in data]
    # Process each passenger request in the data
    for request in data:
        passenger_id = request['id']
        source = int(request['source'])
        dest = int(request['dest'])
        request_time = int(request['time'])

        # Wait until the request time
        while time < request_time:
            time += 1
            movement_log.append((time, elevator_positions.copy()))

        # Find the nearest available elevator
        nearest_elevator = min(range(elevators), key=lambda i: abs(elevator_positions[i] - source))

        # Move the elevator to the source floor
        while elevator_positions[nearest_elevator] != source:
            time += 1
            if elevator_positions[nearest_elevator] < source:
                elevator_positions[nearest_elevator] += 1
            else:
                elevator_positions[nearest_elevator] -= 1
            movement_log.append((time, elevator_positions.copy()))

        # Move the elevator to the destination floor
        while elevator_positions[nearest_elevator] != dest:
            time += 1
            if elevator_positions[nearest_elevator] < dest:
                elevator_positions[nearest_elevator] += 1
            else:
                elevator_positions[nearest_elevator] -= 1
            movement_log.append((time, elevator_positions.copy()))

    # Print the movement log
    for log_entry in movement_log:
        print(f"Time: {log_entry[0]}, Elevator Positions: {log_entry[1]}")

# Test Case 1
# Floors: 5
# Elevators: 1

# Test Case 2:
# Floors: 10
# Elevators: 3

# test case 3
# Floors: 15
# Elevators: 4

# test case 4
# Floors: 7
# Elevators: 2

# Test case 5
# Floors: 12
# Elevators: 3




if __name__ == "__main__":
    main()