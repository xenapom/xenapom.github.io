# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 19:33:38 2017

Contains the Agent class and functions of it

@author: paula
"""

import random

class Agent():
    #x = random.randint()
    #y = random.randint()
    agents = []
    environment = []
    
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y
        
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def move(self):
        # Ensure no agent goes out of bounds
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
    def share_with_neighbours(self, neighborhood):
        for agent in (self.agents):
            distance = self.distance_between(agent)
            if distance <= neighborhood:
                sum = self.store + agent.store
                average = sum / 2
                self.store = average
                agent.store = average
        
    #calculate euclidian distance with pythagoras theorem
    def distance_between(self, agent):
        distance = (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        return distance
