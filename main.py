import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# When player press Up arrow turtle will move up.
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    # When player walk through all window its position is reset, and it goes back to starting position.
    if player.ycor() > 260:
        player.reset_player_position()
        scoreboard.increase_level()
        scoreboard.write_current_level()

    # When player hits a car it is game over.
    for car in car_manager.get_all_cars():
        if player.distance(car) <= 25:
            scoreboard.game_over()
            time.sleep(5)
            game_is_on = False
