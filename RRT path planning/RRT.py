import pygame
from RRTBasePy import RRTGraph
from RRTBasePy import RRTMap
#import time

def main():
               #   y   x
    dimensions = (610,856)
    start = (50, 305)
           # x   y
    goal = (640,405)
    obsdim = 50
    obsnum = 5
    iteration=0
    #t1 = 0

    pygame.init()
    map = RRTMap(start,goal,dimensions, obsdim, obsnum)
    graph= RRTGraph(start,goal,dimensions, obsdim, obsnum)

    obstacles = graph.makeobs()
    map.drawMap(obstacles)

    #1 = time.time()
    while (not graph.path_to_goal()):
       # x , y = graph.sample_envir()
       # n=graph.number_of_nodes()
       # graph.add_node(n,x,y)
       # graph.add_edge(n-1,n)
       # x1,y1 = graph.x[n],graph.y[n]
       # x2,y2 = graph.x[n-1], graph.y[n-1]
       # if(graph.isFree()):
       #     pygame.draw.circle(map.map,map.red,(graph.x[n],graph.y[n]),map.nodeRad,map.nodeThinckness)
       #     if not graph.crossObstacle(x1,x2,y1,y2):
       #         pygame.draw.line(map.map,map.blue,(x1,y1),(x2,y2),map.edgeThinckness)
       # pygame.display.update()

        #elapsed = time.time()-t1
        #t1 = time.time()

        if iteration % 10 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1],Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),map.edgeThinckness)

        else:
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1],Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),map.edgeThinckness)

        if iteration % 5 == 0:
            pygame.display.update()
        iteration += 1
    map.drawPath(graph.getPathCoords())
    print(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)

##PARTE 2 NÂO TA PRONTA AINDA

if __name__ == '__main__':
    main()
       