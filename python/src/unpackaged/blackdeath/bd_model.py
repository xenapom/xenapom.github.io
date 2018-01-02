#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 25 14:32:12 2017

This is the model code for the black death assignment 2.

The program clculates the total deaths from the disease using historical figures of rat
populations and the population density.

There are two input raster map files:
    
1. Average population density per 100x100 m square
2. Average number of rats caught per 100x100 m square

The relationship between average rats caught per week per 100m x 100m square(r),
average population density per 100m x 100m square(p)
and average deaths per week per 100m x 100m square(d) is:
    
d = (0.8 x r) x (1.3 x p)


The program does the following:
    
1. Reads the two maps and puts them on the screen.
Each pixel represents a 100m x 100m square area.

2. Calculates a map showing average deaths per 100m x 100m square area
for the different geographical regions produced by the intersection of the two images.
It runs through the maps and pulls out the values for each pair of equivalently positioned cells.
It then puts them through the equation and produces a two dimensional array of absolute deaths
that you can convert into an Image mapping the deaths.

3. Displays the three maps.

3. Saves the death map as a text file of absolute deaths. Each line equals a line on the map.

4. Displays the total deaths per week.

5. Allows the user to change the parameter weights for the equation.


@author: paula
"""

import matplotlib.pyplot
import csv
import matplotlib.animation
import sys

population_density = []
rats_caught = []
num_deaths = [] #this list holds the number of deaths based on the calc
txt_list = [] #list for writing to file

# function to read input files and put their values into a list
# One list per input file, i.e. one for the population density and one
# for the average number of rats caught
def read_file(filename):
    items = []
    csv_file = open(filename)
    reader = csv.reader(csv_file)
    for row in reader:
        # new rowlist before each row
        rowlist = []
        for values in row:
            # add the row values into the rowlist, make sure they are integers
            rowlist.append(int(values))
            # add the row to the population density list
        items.append(rowlist)
    return items

# function that iterates the 400 x 400 coordinate system, takes rats
# caught at a given position and the density of people at that same position
# and calculates the number of deaths based on the formula given
def iterate_lists(num_of_iterations, txt_list, rat_weight, population_weight):
    death_list = []
    for i in range(num_of_iterations):  
        tmp_list = [] # temporaty list to store deaths per row
        tmp_txt_list = ""
        num_rats_caught = float(rats_caught[i][i])
        density_people = float(population_density[i][i])
        #deaths = int((0.8 * num_rats_caught) * (1.3 * density_people))
        deaths = int((float(rat_weight) * num_rats_caught) * (float(population_weight) * density_people))
        for j in range(num_of_iterations):
            tmp_list.append(deaths)
            tmp_death = str(deaths)
            if i <= 399:
                tmp_txt_list = tmp_txt_list + tmp_death+","
            else:
                tmp_txt_list = tmp_txt_list + tmp_death
        #add each row to the death list
        death_list.append(tmp_list)
        txt_list.append(tmp_txt_list)

    return death_list

# function that writes the number of deaths to a csv file
# takes the file name as an input parameter and writes a new line for each
def write_file(filename, txt_list):
    with open(filename,'w') as output_file:
        output_file.write('\n'.join(txt_list))


#read the input arguments for the weights
#In Spyder, runas "Configuration per file" and give the input parameters
rat_weight = sys.argv[1]
population_weight = sys.argv[2]

#read the files
population_density = read_file('death_parishes.csv')
rats_caught = read_file('death_rats.csv')
num_deaths = iterate_lists(400, txt_list, rat_weight, population_weight)
#write to the text file
write_file('absolute_deaths.txt', txt_list)

# Plot the three different maps on the screen
plt = matplotlib.pyplot
plt.figure()
plt.figure(figsize=(7, 7))
plt.imshow(population_density)
plt.figure()
plt.figure(figsize=(7, 7))
plt.imshow(rats_caught)
plt.figure()
plt.figure(figsize=(7, 7))
plt.imshow(num_deaths)





