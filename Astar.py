from __future__ import annotations
import Map

class Node():
    state_counter = 0
    def __init__(self, pos):
        self.pos = pos
        self.g = 0
        self.h = 0
        self.f = 0
        # self.f = self.g + self.h
        self.parent = []
        self.kids = []
        self.cost = cost
        self.is_goal = False
        self.char = char
    
    def func(self):
        return self.g + self.h

    def heuristic(self, goal):
        self.h = abs(self.pos[0] - goal[0] + abs(self.pos[1] - goal[1]))

    def __eq__(self, other):
        return self.pos == other.pos
    def __str__(self):
        return str(self.pos)

class Astar():
    def __init__(self, map_obj):
        self.map_obj = map_obj
        self.openList = []
        self.closedList = []
        self.succ = []

        self.x = Node(map_obj.get_start_pos(), map_obj.get_cell_value(map_obj.get_start_pos()))
        self.x.heuristic(self.map_obj.get_end_goal_pos())
        self.x.func()