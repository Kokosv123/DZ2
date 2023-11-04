import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5

        if hasattr(self, "headmaster"):
            self.headmaster.productivity += 0.12
            self.headmaster.happiness += 1

    def to_sleep(self):
        print("I`ll go sleep")
        self.gladness += 3

    def to_chill(self):
        print("Reset time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self, day):
        print("==============Day", day, "of", self.name, "life ===============")
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")

    def live(self, day):
        self.end_of_day(day)
        self.is_alive()

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.action = "study"
            self.to_study()
        elif live_cube == 2:
            self.action = "sleep"
            self.to_sleep()
        elif live_cube == 3:
            self.action = "chill"
            self.to_chill()

class Headmaster:
    def __init__(self, name):
        self.name = name
        self.productivity = 0
        self.happiness = 32.23
        self.alive = True

    def do_work(self):
        print("It`s time to do documents!")
        self.productivity += 0.09
        self.happiness -= 0.67

    def stay_at_home(self):
        print("I dont want to go to school!")
        self.productivity -= 0.04
        self.happiness += 4

    def study(self):
        print("I need to study in class")
        self.productivity += 0.09
        self.happiness += 1

    def is_alive(self):
        if self.productivity < -0.5:
            print("fired...")
            self.alive = False
        elif self.happiness <= 0:
            print("depression...")
            self.alive = False
        elif self.productivity > 9:
            print("and what I need to do now?...")
            self.alive = False

    def end_of_day(self, day):
        print("==============Day", day, "of", self.name, "life ===============")
        print(f"Happiness = {self.happiness}")
        print(f"Progress = {round(self.productivity, 2)}")

    def live(self, day):
        self.end_of_day(day)
        self.is_alive()

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.action = "It`s time to do documents!"
            self.do_work()
        elif live_cube == 2:
            self.action = "I dont want to go to school!"
            self.stay_at_home()
        elif live_cube == 3:
            self.action = "I need to study in class!"
            self.study()

nick = Student(name="Nick")
johnny = Headmaster(name="Johnny")

for day in range(1, 366):
    if not (nick.alive and johnny.alive):
        break

    nick.live(day)
    johnny.live(day)

