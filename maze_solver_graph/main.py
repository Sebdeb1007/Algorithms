from matplotlib.pyplot import table
from maze_solver import *


#Maze Solver 
#The starting point is the left top corner and the ending point the right bottom corner (see 10x10.png for an example) 
#Using networkx (https://networkx.org/) to generate graph and to determine shortest path (Djikstra)
#few using case of Maze_solver
def main():

    #maze 10x10
    map10 = [
        [0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,1,0,1,0],
        [0,0,0,1,0,0,1,0,1,1],
        [0,1,0,1,0,0,1,0,0,0],
        [0,0,0,1,0,1,1,0,1,0],
        [1,1,1,1,0,0,0,0,0,0]
    ]


    map20 = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0],
        [0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1],
        [0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0],
        [0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0],
        [1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1],
        [0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,1,0],
        [0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1],
        [0,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0],
        [0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0],
        [1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0]
    ]

    #finding shotest path to solve the maze.
    print(Maze_solver.solver_tab(map10))
    print(Maze_solver.solver_tab(map20))

    #finding shortest path to solve the maze from a random map (size is 100 square and there is 20% chance that a square is a wall).
    print(Maze_solver.solver_random(100,20))
    

    #drawing the graph of a specified graph png or pdf format supported.
    Maze_solver.draw_graph(map10,"graph10.png")
    Maze_solver.draw_graph(map10,"graph20.png")

    #finding shortest path and showing it in a png file, the solution is in red. 
    Maze_solver.to_png(map10,"10x10.png")
    Maze_solver.to_png(map20,"20x20.png")

    Maze_solver.to_png_random(100,20,"100x100.png")
    Maze_solver.to_png_random(1000,20,"1000x1000.png")



if __name__ == "__main__":
    main()