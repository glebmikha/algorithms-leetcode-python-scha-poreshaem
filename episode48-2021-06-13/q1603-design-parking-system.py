class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.car_places = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        self.car_places[carType] -= 1
        return self.car_places[carType] >= 0


if __name__ == '__main__':
    ps = ParkingSystem(1, 1, 0)
    for car_type in [1, 2, 3, 1]:
        print(ps.addCar(car_type))
