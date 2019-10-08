import pygame as pg
import sys
from car import Car
import random

class Cars:
    def __init__(self, num_cars):
        pg.init()
        self.size = 1000, 1000
        self.screen = pg.display.set_mode(self.size)
        self.background = self.create_background()
        self.cars = self.create_cars(num_cars)

        self.draw_loop()

    def create_cars(self, num):
        temp = []
        for i in range(num):
            temp.append(Car(self.random_color(), (500, 500), self.screen))
        return temp

    def draw_cars(self, actions):
        for i in range(len(self.cars)):
            self.cars[i].move(actions[i])
            self.cars[i].draw()

    def create_background(self):
        background = []
        background.append(pg.Rect(100, 100, 100, self.size[1] - 200))
        background.append(pg.Rect(200, self.size[1] -200, self.size[0] - 400, 100))
        background.append(pg.Rect(self.size[0] - 200, 100, 100, self.size[1] - 200))
        background.append(pg.Rect(300, 100, 100, 600))
        background.append(pg.Rect(200, 100, 100, 100))
        background.append(pg.Rect(400, 600, 200, 100))
        background.append(pg.Rect(600, 100, 100, 600))
        background.append(pg.Rect(700, 100, 100, 100))

        return background

    def draw_background(self):
        self.screen.fill(pg.Color(0, 255, 0))
        for rect in self.background:
            pg.draw.rect(self.screen, pg.Color(0, 0, 0), rect)

    def random_color(self):
        return pg.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            

    def draw_loop(self):
        while True:
            # If exited, don't crash
            for event in pg.event.get():
                if(event.type == pg.QUIT):
                    sys.exit()

            self.advance_state()

    def advance_state(self, actions):
        self.draw_background()
        self.draw_cars(actions)
        pg.display.flip()