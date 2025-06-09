'''
Author: Luke O'Brien
File Description: Main file for Elevator Program
Tests: tests.main.py
'''

from data_processor import DataProcessor
from scheduler import Scheduler
import logging



def main(filename, floors=1, elevators=1, capacity=1, output_file="elevator_positions.csv"):
    """Main function to execute the program."""

    data = DataProcessor(filename, floors)  # Initialise the DataProcessor with the CSV file
    if not data.valid:
        print("Invalid csv. Exiting program.")
        return

    requests = data.requests  
    scheduler=Scheduler(nelevators=elevators, floors=floors, capacity=capacity,)  # Initialise the Scheduler with the number of elevators, floors, and capacity
    print(f"Running elevator simulation with {elevators} elevators, {floors} floors, and capacity of {capacity} per elevator.")
    print(f"Processing {len(requests)} requests from {filename}...")
    scheduler.run(requests, output_file=output_file)




if __name__ == "__main__":
    main('data.csv', floors=51, elevators=3, capacity=4, output_file="elevator_positions_data.csv")  
    main('test_case_1.csv', floors=5, elevators=1, capacity=4, output_file="elevator_positions_test_case_1.csv") 
    main('test_case_2.csv', floors=10, elevators=3, capacity=4, output_file="elevator_positions_test_case_2.csv") 
    main('test_case_3.csv', floors=15, elevators=4, capacity=4, output_file="elevator_positions_test_case_3.csv")   
    main('test_case_4.csv', floors=7, elevators=2, capacity=4, output_file="elevator_positions_test_case_4.csv")  
    main('test_case_5.csv', floors=12, elevators=3, capacity=4, output_file="elevator_positions_test_case_5.csv")

