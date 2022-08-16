from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(290, random.randint(-240, 240))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def get_all_cars(self):
        return self.all_cars

    def increase_cars_speed(self):
        self.car_speed *= 1.2

