# Project number one
# Random walk

import matplotlib.pyplot as plt
from random import choice
 
# defining a class which will generate random points that will be plotted
class RandomWalk:
    def __init__(self, number = 5000):
        #initalizing the initial points
        self.number = number
        self.x_point = [0]
        self.y_point = [0]
        
    def walk(self):
        case = 0
        while case< self.number:
            case += 1 #for the ending ot the loop as the number reaches the limit inserted
            x_direction = choice([1,-1])
            y_direction = choice([1,-1])
            
            # the amount of distance
            x_distance = choice([0, 1, 2, 3, 4, 5])
            y_distance = choice([0, 1, 2, 3, 4, 5])
            
            #new x coordinate
            x_increment = x_direction * x_distance
            x_coordinate = self.x_point[-1] + x_increment
            #new y coordinate
            y_increment = y_direction * y_distance
            y_coordinate = self.y_point[-1] + y_increment
            
            if x_coordinate == 0 and y_coordinate == 0:
                continue
            else:    
                # inserting the new points in their respective lists
                self.x_point.append(x_coordinate)
                self.y_point.append(y_coordinate)
                
rw = RandomWalk()
rw.walk()

# plotting the points

fix, ax = plt.subplots()
ax.scatter(rw.x_point, rw.y_point, s = 10)
plt.show()
