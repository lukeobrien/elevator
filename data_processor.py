'''
Author: Luke O'Brien
File Description: CSV Data Processor for Elevator Program
'''
import csv

class PassengerRequest:
    def __init__(self, time, pid, source, dest):
        self.time = int(time)
        self.id = pid
        self.source = int(source)
        self.dest = int(dest)
        self.pickup_time = None
        self.dropoff_time = None

class DataProcessor:
    """Class to handle data processing for the elevator system."""
    
    def __init__(self, filename, floors):
        self.filename = filename
        self.floors = floors
        self.requests = [PassengerRequest(*row) for row in self._csvReader()]

    def valid(self):
        """Validates the data read from the CSV file."""
        # TODO - Why not remove bad requests and return valid data? 
        # Shouldnt this be an internal method to the data api? 

        for row in self.requests:
            if 'id' not in row or 'source' not in row or 'dest' not in row or 'time' not in row:
                print("Error: Missing required fields in the data.")
                return False
            
            if int(row['source']) < 1 or int(row['source']) > self.floors:
                print(f"Error: Source floor {row['source']} is out of range (1-{self.floors}).")
                return False
            
            if int(row['dest']) < 1 or int(row['dest']) > self.floors:
                print(f"Error: Destination floor {row['dest']} is out of range (1-{self.floors}).")
                return False
            
            if int(row['time']) < 0:
                print(f"Error: Time {row['time']} cannot be negative.")
                return False
        
        return True
        
    def _csvReader(self):
        """Reads a CSV file and returns its contents as a list of dictionaries."""
        # Read the data.csv file
        try:
            with open(self.filename, mode='r') as f:
                input = csv.reader(f)
                return [row for row in input][1:]  # Convert rows into a list of dictionaries

        except FileNotFoundError:
            print("Error: data.csv file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")