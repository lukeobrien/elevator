# Technical assessment elevator

Sample input:

```csv
time,id,source,dest
0,passenger1,1,51
0,passenger2,1,37
10,passendar3,20,1
```


Desired output
Floor each elevator is at for every point in time to a file. 
Summary statistics :
min, 
max, 
and mean total time 
and wait times were for all passengers.


required packages
statistics# Elevator Simulation

This project simulates the operation of elevators in a building, processing passenger requests from CSV files and generating elevator position logs and statistics.

## Features

- Reads passenger requests from CSV files.
- Simulates multiple elevators with configurable floors and capacities.
- Outputs elevator positions and summary statistics.
- Logging of simulation steps and data manipulation.

## Usage

1. Place your request data in CSV files (see `data.csv` or `test_case_*.csv` for examples).
2. Run the simulation:

   ```bash
   python main.py
   ```

3. Check the output CSV files for elevator positions and `elevator.log` for logs.

## Configuration

Edit the `main.py` file to change:
- Number of elevators
- Number of floors
- Elevator capacity
- Input/output file names

## Files

- `main.py` - Main entry point and simulation runner.
- `data_processor.py` - Handles input data.
- `scheduler.py` - Elevator scheduling logic.
- `elevator.log` - Log file with simulation details.

## Requirements

- Python 3.x

## Author

Luke O'Brien
csv
