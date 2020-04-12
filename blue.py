from arr2_epec_cs_ex import *
import RRT

def initialize(params):
  print(params)

def play_turn(params):
    path = []
##  print(params)
##  params[0].append([Point_2(5,5), Point_2(5, 8), Point_2(5, 10)])
##  params[0].append([Point_2(5, 10), Point_2(5, 13), Point_2(5, 15)])
    print("path:",params[0])
    print("t:", params[1])
    print("d:", params[2])
    print("team status:", params[3])
    print("opp_stat:",params[4])
    print("coupons:",params[5])
    print("data:",params[6])

##    obst1 = Polygon_2([Point_2(0, 0), Point_2(2, 0), Point_2(2, 2), Point_2(0, 2)])
    obst2 = Polygon_2([Point_2(6, 6), Point_2(7, 6)])
    obstacles = [obst2]

    radius = FT(1)
    start = Point_2(10, 12.)
    goal = Point_2(6,1)
    
    RRT.generate_path(path, obstacles, radius, start, goal)
    print("going to",path[0])
    params[0].append(path[0])
    print("going to",path[1])
    params[0].append(path[1])
                      
