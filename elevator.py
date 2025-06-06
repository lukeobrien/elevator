class Elevator():
    def __init__(self, max_floor):
        self.max_floor = max_floor
        self.current_floor = 0
        self.direction = None

    def go_to(self, floor):
        if floor < 0 or floor > self.max_floor:
            raise ValueError("Floor out of range")
        self.direction = "up" if floor > self.current_floor else "down"
        self.current_floor = floor

    def get_current_floor(self):
        return self.current_floor

    def get_direction(self):
        return self.direction