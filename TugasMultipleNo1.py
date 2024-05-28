class Flyer:
    def takeOff(self):
        pass

    def land(self):
        pass

    def fly(self):
        pass


class Airplane(Flyer):
    def takeOff(self):
        print("Airplane is taking off.")

    def land(self):
        print("Airplane is landing.")

    def fly(self):
        print("Airplane is flying.")


class Bird(Flyer):
    def takeOff(self):
        print("Bird is taking off.")

    def land(self):
        print("Bird is landing.")

    def fly(self):
        print("Bird is flying.")

    def buildNest(self):
        print("Bird is building a nest.")

    def layEggs(self):
        print("Bird is laying eggs.")


class Superman(Flyer):
    def takeOff(self):
        print("Superman is taking off.")

    def land(self):
        print("Superman is landing.")

    def fly(self):
        print("Superman is flying.")

    def leapBuilding(self):
        print("Superman is leaping off a building.")

    def stopBullet(self):
        print("Superman is stopping a bullet.")


# Contoh penggunaan:
if __name__ == "__main__":
    airplane = Airplane()
    bird = Bird()
    superman = Superman()

    print("\nAirplane:")
    airplane.takeOff()
    airplane.fly()
    airplane.land()

    print("\nBird:")
    bird.takeOff()
    bird.fly()
    bird.land()
    bird.buildNest()
    bird.layEggs()

    print("\nSuperman:")
    superman.takeOff()
    superman.fly()
    superman.land()
    superman.leapBuilding()
    superman.stopBullet()