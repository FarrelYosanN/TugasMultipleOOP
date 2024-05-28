class Sailer:
    def dock(self):
        pass

    def cruise(self):
        pass


class Flyer:
    def takeOff(self):
        pass

    def land(self):
        pass

    def fly(self):
        pass


class Vehicle:
    def move(self):
        pass


class RiverBarge(Sailer, Vehicle):
    def dock(self):
        print("River barge is docking.")

    def cruise(self):
        print("River barge is cruising.")

    def move(self):
        print("River barge is moving.")


class Airplane(Flyer, Vehicle):
    def takeOff(self):
        print("Airplane is taking off.")

    def land(self):
        print("Airplane is landing.")

    def fly(self):
        print("Airplane is flying.")

    def move(self):
        print("Airplane is moving.")


class SeaPlane(Sailer, Airplane):
    def dock(self):
        print("Sea plane is docking.")

    def cruise(self):
        print("Sea plane is cruising.")


class Helicopter(Airplane):
    pass


# Contoh penggunaan:
if __name__ == "__main__":
    river_barge = RiverBarge()
    airplane = Airplane()
    sea_plane = SeaPlane()
    helicopter = Helicopter()

    print("\nRiver Barge:")
    river_barge.dock()
    river_barge.cruise()
    river_barge.move()

    print("\nAirplane:")
    airplane.takeOff()
    airplane.fly()
    airplane.land()
    airplane.move()

    print("\nSea Plane:")
    sea_plane.dock()
    sea_plane.cruise()

    print("\nHelicopter:")
    helicopter.takeOff()
    helicopter.fly()
    helicopter.land()