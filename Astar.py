from __future__ import annotations
from operator import itemgetter

from Map import Map_Obj

map_obj = Map_Obj(task=1)

class Node():
    def __init__(self, pos, parent):
        self.pos = pos
        self.cost = 0
        self.heur = 0
        self.total = 0
        self.parent = parent
        self.kids = []
        self.is_goal = False
        self.heuristic(map_obj.get_goal_pos())     
        self.func()
    
    def func(self):
        if self.parent != []: 
            self.cost = map_obj.get_cell_value(self.pos) + self.parent.cost
        else: 
            self.cost = map_obj.get_cell_value(self.pos)
        self.total = self.cost + self.heur
        
    def heuristic(self, goal):
        # absolute value of current x minus goal x, plus current y minus goal y
        self.heur = abs(self.pos[0] - goal[0]) + abs(self.pos[1] - goal[1])


class Astar():
    def __init__(self, map_obj):
        self.map_obj = map_obj
        self.openList = []
        self.closedList = []
        print(map_obj.get_goal_pos(), 'Mååål')
        print(map_obj.get_start_pos(), ' Start')

    def find_succ(self, parent_node):
        self.succ = []
        x = parent_node.pos[0]
        y = parent_node.pos[1]
        i = 0
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

        for i in range(len(self.succ)):
            curr_node = Node(self.succ[i], parent_node)
            self.append_and_check_for_equal(curr_node)
        self.closedList.append(parent_node)
        self.openList.remove(parent_node)
                
    def sort_openList(self):
        self.openList.sort(key=lambda x : x.total)
        
    def append_and_check_for_equal(self, current_node): 
        a = 0
        
        for a in range(len(self.openList)):
            if current_node.pos == self.openList[a].pos:
                if current_node.total < self.openList[a].total: 
                    self.openList.pop(a)
                    self.openList.append(current_node)
                    self.openList = self.sort_openList()
                return
            a += 1 
        self.openList.append(current_node)  
        self.sort_openList() 
        

    def recover_path(self, current_node): 
        # tracks the total path back to the start node
        self.path = [current_node.pos]
        while current_node.pos != map_obj.get_start_pos():
            current_node = current_node.parent
            self.path.append(current_node.pos)
        return self.path
                
    def check_for_goal(self, current_node):
        if current_node.pos == map_obj.get_start_pos(): 
            return True
        return False

if __name__ == "__main__":
        aStar = Astar(map_obj)  
        aStar.current = Node(map_obj.get_start_pos(), [])
        aStar.openList.append(aStar.current)
        print(aStar.openList)
        aStar.sort_openList()
        
        while aStar.current.pos != map_obj.get_goal_pos():
            aStar.find_succ(aStar.current)
            aStar.sort_openList()
            aStar.current = aStar.openList[0]
            print(aStar.current.pos, 'test')
        print('yey', aStar.current.pos)
        path = aStar.recover_path(aStar.current)
        # for i in range(len(path)):
        #     map_obj.replace_map_values(path[i], 2, map_obj.get_goal_pos())
            
        map_obj.get_maps()
        map_obj.show_map()



    
        
