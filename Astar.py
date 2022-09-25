from __future__ import annotations
from Map import Map_Obj

map_obj = Map_Obj(task=1)

class Node():
    state_counter = 0
    def __init__(self, pos):
        self.pos = pos
        self.cost = 0
        self.heur = 0
        self.total = 0
        self.parent = []
        self.kids = []
        self.is_goal = False
    
    def func(self):
        self.cost = map_obj.get_cell_value(self.pos)
        return self.cost + self.heur

    def heuristic(self, goal):
        # absolute value of current x minus goal x, plus current y minus goal y
        self.heur = abs(self.pos[0] - goal[0]) + abs(self.pos[1] - goal[1])
        print(self.heur, ': heuristic value')

class Astar():
    def __init__(self, map_obj):
        self.map_obj = map_obj
        self.openList = []
        self.closedList = []
        self.succ = []
        self.openList.append(self.get_start_pos())
        self.current = Node(map_obj.get_start_pos())
        print(map_obj.get_goal_pos(), 'Mååål')
        print(map_obj.get_start_pos(), ' Start')
        self.current.heuristic(map_obj.get_goal_pos())     
        self.current.total = self.current.func()

    def find_succ(self):
        x = self.pos[0]
        y = self.pos[1]
        i = 0
        for i in range(4):
            if i == 1: 
                self.succ.append([x+1,y])
            elif i == 2: 
                self.succ.append([x, y+1])
            elif i == 3:
                self.succ.append([x-1, y])
            else:
                self.succ.append([x, y-1])
            i += 1

    def next_node(self):
        i = 0
        for i in range(4):
            curr_check = Node(self.succ[i])
            a = 0
            for a in range(len(self.openList)):
                if curr_check.pos in self.openList[a].pos:
                    print('hei, her var det noe spennende')
                    a+=1
            i+=1

Astar(map_obj)  
        