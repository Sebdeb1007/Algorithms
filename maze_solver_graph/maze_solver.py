import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from random import randint
from PIL import Image


class Maze_solver(object):
    
    @classmethod
    def solver_tab(self,tab):
        map_graph = self._create_graph(tab)
        return  nx.shortest_path(map_graph,(0,0),(len(tab)-1,len(tab)-1))
    
    @classmethod
    def solver_random(self,size,proba):
        tab = self._create_map(size,proba)
        return (tab,self.solver_tab(tab))
    
    @classmethod
    def to_png(self,tab,name):
        sh_path = self.solver_tab(tab)
        tab_modif = tab
        for i in sh_path:
            tab_modif[i[0]][i[1]] = 5

        image = []
        for i in range(len(tab)):
            for j in range(len(tab)):
                if tab_modif[i][j] == 1:
                    image.append((51,25,0))
                elif tab_modif[i][j] == 5:
                    image.append((255,0,0))
                elif tab_modif[i][j] == 0:
                    image.append((255,255,255))

        image = np.array(image, dtype = np.uint8)
        image = np.reshape(image,(len(tab),len(tab),3))
        image = Image.fromarray(image)
        if len(tab) < 500:
            image = image.resize((500,500), Image.NEAREST)
        image.save(name)

    @classmethod
    def to_png_random(self,size,proba,name):
        tab,sh_path = self.solver_random(size,proba)
        tab_modif = tab
        for i in sh_path:
            tab_modif[i[0]][i[1]] = 5

        image = []
        for i in range(len(tab)):
            for j in range(len(tab)):
                if tab_modif[i][j] == 1:
                    image.append((51,25,0))
                elif tab_modif[i][j] == 5:
                    image.append((255,0,0))
                elif tab_modif[i][j] == 0:
                    image.append((255,255,255))

        image = np.array(image, dtype = np.uint8)
        image = np.reshape(image,(len(tab),len(tab),3))
        image = Image.fromarray(image)
        if len(tab) < 500:
            image = image.resize((500,500), Image.NEAREST)
        image.save(name)
    
    @classmethod
    def _create_map(self,size,proba):
        map = list()
        for i in range(size):
            sub =list()
            for j in range(size):
                rdm = randint(0,100)
                if rdm <= proba:
                    sub.append(1)
                else:
                    sub.append(0)
            map.append(sub)
        map[0][0] = 0
        map[size -1][size-1] = 0
        return map

    @classmethod
    def draw_graph(self,tab,name):
        #could be time consuming 
        map_graph = self._create_graph(tab)
        a = nx.draw(map_graph, with_labels=True, font_weight='bold')
        plt.savefig(name)
    
    @classmethod
    def _create_graph(self,tab):
        map_graph = nx.Graph()
        for i in range(len(tab)):
            for j in range(len(tab)):
                if tab[i][j] == 0:
                    map_graph.add_node((i,j))
        #nx.draw(map_graph, with_labels=True, font_weight='bold')
        edge_list = list()
        for i in list(map_graph):
            if i[1]<len(tab)-1 and tab[i[0]][i[1]+1] == 0:
                edge_list.append((i,(i[0],i[1]+1)))
            if i[0]<len(tab)-1 and tab[i[0]+1][i[1]] == 0:
                edge_list.append((i,(i[0]+1,i[1])))
        return nx.Graph(edge_list)




