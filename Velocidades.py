import numpy as np
import FIRALib


def velocidade(id,ToF,Ve,Wa):
    L = 7.5
    R = 0.001

    V = Ve
    W = np.deg2rad(Wa)

    wr = ((2.0*V)+(W*L))/(2.0+R)
    wl = ((2.0*V)-(W*L))/(2.0+R)

    FIRALib.movimente(0,True,wl,wr)

def mod(a):
    if a < 0:
        a = a * (-1)
    
    return(a)