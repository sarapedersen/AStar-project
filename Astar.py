from __future__ import annotations
from math import sqrt
from operator import itemgetter

from Map import Map_Obj

class Node():
    def __init__(self, pos, parent):
        self.pos = pos
        self.cost = 0
        self.heur = 0
        self.total = 0
        self.parent = parent
        self.is_goal = False
        self.heuristic(map_obj.get_goal_pos())     
        self.func()
    
    def func(self):
        # adds up the this node's costs and its parent cost (if it has a parent), with the heurstic. 
        if self.parent != []: 
            self.cost = map_obj.get_cell_value(self.pos) + self.parent.cost
        else: 
            self.cost = map_obj.get_cell_value(self.pos)
        self.total = self.cost + self.heur
        
    def heuristic(self, goal):
        # absolute value of current x minus goal x, plus current y minus goal y
        if int(inputHeur) == 1: 
            # Euclidean distance
            self.heur = sqrt((self.pos[0]-goal[0])**2+(self.pos[1] - goal[1])**2 )
        else: 
            # Manhattan distance
            self.heur = abs(self.pos[0] - goal[0]) + abs(self.pos[1] - goal[1])


class Astar():
    def __init__(self, map_obj):

        # intializes the necessary values
        self.map_obj = map_obj
        self.openList = []
        self.closedList = []

    # Finds the successors of the node, and adds it to openList
    def find_succ(self, parent_node):

        # initializes necessary values
        self.succ = []
        x = parent_node.pos[0]
        y = parent_node.pos[1]
        i = 0

        # if the positions around the node is a wall, it is not added to the successors list
        for i in range(4):
            i += 1
            l = []
            if i == 1: 
                l = [x+1, y]
            elif i == 2: 
                l =[x, y+1]
            elif i == 3:
                l = [x-1, y]
            else:
                l = [x, y-1]

            if (map_obj.get_cell_value(l) > 0):
                self.succ.append(l)
        
        # initializes the successors, and appends the correct ones to openList
        for i in range(len(self.succ)):
            curr_node = Node(self.succ[i], parent_node)
            self.append_and_check_for_equal(curr_node)

        # removes the node from openList since it has been checked out, and puts it in closedList
        self.closedList.append(parent_node)
        self.openList.remove(parent_node)
                
    # Sorts openList based on the total value (the cost and the heuristic)
    def sort_openList(self):
        self.openList.sort(key=lambda x : x.total)
    
    # If the position alreadu lies in openList, it will check if the total of the most recently node is higher than the old
    # if it is, it will replace the new node with the old. If it is not any equal nodes, it will just be appended to the list. 
    def append_and_check_for_equal(self, current_node): 
        a = 0
        for a in range(len(self.openList)):
            if current_node.pos == self.openList[a].pos:
                if current_node.total < self.openList[a].total: 
                    self.openList.pop(a)
                    self.openList.append(current_node)
                return
            a += 1 
        self.openList.append(current_node)  
        

    def recover_path(self, current_node): 
        # tracks the total path back to the start node
        self.path = [current_node.pos]
        while current_node.pos != map_obj.get_start_pos():
            current_node = current_node.parent
            self.path.append(current_node.pos)
        return self.path

if __name__ == "__main__":
        # Initializes the program
        inputTask = int(input('Choose a task from 1 - 4: '))
        inputHeur = input('Choose either Euclidean (1) or Manhattan (2) distance: ')
        inputTrack = input('Show A* algorithm search track (y/n): ')

        map_obj = Map_Obj(task=(inputTask))

        aStar = Astar(map_obj)  
        aStar.current = Node(map_obj.get_start_pos(), [])
        aStar.openList.append(aStar.current)
        
        # Tries to find the best successor until the goal is reached
        while aStar.current.pos != map_obj.get_goal_pos():
            aStar.find_succ(aStar.current)
            aStar.sort_openList()
            aStar.current = aStar.openList[0]
            if inputTrack == 'y': 
                map_obj.replace_map_values(aStar.current.pos, 6, map_obj.get_goal_pos())

        # Draws the map
        path = aStar.recover_path(aStar.current)
        for i in range(len(path)):
            map_obj.replace_map_values(path[i], 5, map_obj.get_goal_pos())
            
        map_obj.get_maps()
        map_obj.show_map()
