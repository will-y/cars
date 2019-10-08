import pygame as pg
import math
import random

class Car:
    size = 10, 10
    acceleration = 0.2
    angle_change = 0.4
    max_speed = 3
    def __init__(self, color, starting_pos, screen):
        self.color = color
        self.pos = starting_pos
        self.speed = -random.random()
        self.angle = random.random() * (math.pi / 2) - math.pi/4
        self.screen = screen
        self.dead = False
        self.score = 0

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.size[0], self.size[1]))

    def move(self, action):
        if action == 0:
            # speed up
            self.speed += self.acceleration
        elif action == 1:
            # slow down
            self.speed -= self.acceleration
        elif action == 3:
            #turn left
            self.angle -= self.angle_change
        elif action == 4:
            #turn right
            self.angle += self.angle_change

        # action 2: same speed
        # action 5: same direction
        dx = self.speed * math.sin(self.angle)
        dy = self.speed * math.cos(self.angle)

        self.pos = self.pos[0] + dx, self.pos[1] + dy

    def car_vision(self, background):
        # distance away from walls in all directions
        result = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        result_checked = [False, False, False, False, False, False, False, False]
        while i < 200:
            counter = 0
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if (not result_checked[counter]) and check_point((self.pos[0] + j, self.pos[1] + k), background):
                        result_checked[counter] = True
                        result[counter] = 1 / i
                    counter += 1
                
            i += 1
        
        print("Vision: {}".format(result))

    def check_point(self, point, background):
        for rect in background:
            if background.collidepoint(point):
                return True

        return False

    def check_dead(self, backgorund):
        return self.check_point(self.pos, bakcground) 