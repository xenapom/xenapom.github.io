# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 07:57:28 2017

Displays agents in a coordinate system and calculates the
distance between them according to the Pythagorean theorem

@author: paula
"""

import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation
import random


num_of_agents = 50
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Loop csv raster data
# new rowlist before each row
# add the row values into the rowlist, make sure they are integers
csv_file = open('in.csv')
reader = csv.reader(csv_file)
for row in reader:
    rowlist = []
    for values in row:
        rowlist.append(int(values))
        
    # add the row to the environment list
    environment.append(rowlist)

# Setup variables in a 100x100 grid
# Create x and y agents in the coordinate system
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents))

carry_on = True

def update(frame_number):
    fig.clear()
    global carry_on
    # Walk the agents in the coordinate system
    for j in range(num_of_iterations):
        for k in range(num_of_agents):
            agents[k].move()
            agents[k].eat()
            agents[k].share_with_neighbours(neighbourhood)
    
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a            # Returns control and waits next call.
        a = a + 1
        

# save the animation as an html file in order to display the animation on a web page
# tested to work on a macbook. Commented out for assignment submission
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
#animation.save('abm.html', fps=30, extra_args=['-vcodec','libx264'])
#matplotlib.pyplot.show()

# shows the output of the agents in the csv pixel data environment
matplotlib.pyplot.imshow(environment)


