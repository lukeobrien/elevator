import pandas as pd
import matplotlib.pyplot as plt

class Passenger:
    def __init__(self, id, request_time, pickup_time, dropoff_time):
        self.id = id
        self.request_time = request_time
        self.pickup_time = pickup_time
        self.dropoff_time = dropoff_time

def plot_elevator_positions(filename="elevator_positions.csv"):
    df = pd.read_csv(filename)
    time = df["time"]

    plt.figure(figsize=(10, 6))
    for col in df.columns[1:]:
        plt.plot(time, df[col], label=col)

    plt.xlabel("Time")
    plt.ylabel("Floor")
    plt.title("Elevator Movement Over Time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_time_distributions(passenger_log_filename="passenger_log.csv"):
    # Expected CSV format: id,request_time,pickup_time,dropoff_time
    df = pd.read_csv(passenger_log_filename)
    df["wait_time"] = df["pickup_time"] - df["request_time"]
    df["total_time"] = df["dropoff_time"] - df["request_time"]

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    axs[0].hist(df["wait_time"], bins=range(df["wait_time"].max() + 2), edgecolor='black')
    axs[0].set_title("Passenger Wait Time Distribution")
    axs[0].set_xlabel("Wait Time (units)")
    axs[0].set_ylabel("Passenger Count")

    axs[1].hist(df["total_time"], bins=range(df["total_time"].max() + 2), edgecolor='black')
    axs[1].set_title("Passenger Total Time Distribution")
    axs[1].set_xlabel("Total Time (units)")
    axs[1].set_ylabel("Passenger Count")

    plt.tight_layout()
    plt.show()

# Optional: Run both visualizations from here
if __name__ == "__main__":
    plot_elevator_positions("elevator_positions.csv")
    plot_time_distributions("passenger_log.csv")
