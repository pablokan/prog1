from dataclasses import dataclass

@dataclass
class Car:
    color: str
    make: str
    model: str
    engineOn: bool = False
    engineRunning: bool = False

    def startEngine(self):
        if self.engineOn:
            print("The engine is already on")
        else:
            print("Starting the engine")
            self.engineOn = True
            self.engineRunning = True

    def stopEngine(self):
        if self.engineOn:
            print("Stopping the engine")
            self.engineOn = False
            self.engineRunning = False
        else:
            print("The engine is already off")

    def start(self):
        if self.engineOn:
            if self.engineRunning:
                print("The car is already running")
            else:
                print("Starting the car")
                self.engineRunning = True
        else:
            print("The engine is off")

    def stop(self):
        if self.engineOn:
            if self.engineRunning:
                print("Stopping the car")
                self.engineRunning = False
            else:
                print("The car is already stopped")
        else:
            print("The engine is off")

auto = Car("red", "ford", "fiesta")
auto.startEngine()
auto.start()
auto.stopEngine()
auto.stop()
