import FIRALib
import math
import time

while True:
    PosicaoBola = FIRALib.bola()
    PosicaoCarro = FIRALib.amareloCar(1)
   ## FIRALib.movimente(0,True,1,-1)

    if (PosicaoBola[1]+0.61) > (PosicaoCarro[1]+0.61):## Se a bola estiver a direita do carrinho
        C = ((-PosicaoBola[0] + 0.72) - (-PosicaoCarro[0]+0.72))
        B = ((PosicaoBola[1]+  0.61) - (PosicaoCarro[1]+0.61))
        if (-PosicaoBola[0] + 0.72) < (-PosicaoCarro[0]+0.72):
            theta =  -(3.1 + math.atan(B/C))
        else:
            theta =  -math.atan(B/C)

    if (PosicaoBola[1]+0.61) < (PosicaoCarro[1]+0.61):## Se a bola estiver a direita do Esquerda
        C = (-(-PosicaoBola[0] + 0.72) + (-PosicaoCarro[0]+0.72))
        B = ((PosicaoBola[1]+  0.61) - (PosicaoCarro[1]+0.61))
        if (-PosicaoBola[0] + 0.72) < (-PosicaoCarro[0]+0.72):
            theta =  ( math.atan(B/C) + 3.1)
        else:
            theta =  math.atan(B/C)
           
           
###########################################################################################################
    print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   

    if( PosicaoCarro[2] + 1.55 > theta and PosicaoCarro[2] - 1.55 < theta ):
        if ((PosicaoCarro[2]+0.299) > theta):
            
            FIRALib.movimente(0,True,-20,-50)#direita


        if ((PosicaoCarro[2]- 0.299) < theta):

            FIRALib.movimente(0,True,-50,-10)#esquerda

        if((PosicaoCarro[2]+0.398) > theta and theta > (PosicaoCarro[2]- 0.398) ):

            FIRALib.movimente(0,True,-30,-30)
    else:
        if(theta < -2 and PosicaoCarro[2] > 2):
            FIRALib.movimente(0,True,-50,-20)#esquerda
        elif(theta > 2 and PosicaoCarro[2] < -2):
            FIRALib.movimente(0,True,-10,-50)#direita

        else:
            if( theta > 0):
                if ((PosicaoCarro[2]+0.299 + 3) < theta):
        
                    FIRALib.movimente(0,True,20,50)#Esquerda


                if ((PosicaoCarro[2]- 0.299 + 3) > theta):

                    FIRALib.movimente(0,True,50,10)#Direita
                
                if((PosicaoCarro[2]+0.298 +3) > theta and theta > (PosicaoCarro[2]- 0.298 + 3) ):

                    FIRALib.movimente(0,True,30,30)

            if( theta < 0):
                if ((PosicaoCarro[2]+0.299 - 3) < theta):
        
                    FIRALib.movimente(0,True,10,50)#Esquerda


                if ((PosicaoCarro[2]- 0.299 - 3) > theta):

                    FIRALib.movimente(0,True,50,10)#Direita
                
                if((PosicaoCarro[2]+0.298 -3) > theta and theta > (PosicaoCarro[2]- 0.298 - 3) ):

                    FIRALib.movimente(0,True,30,30)


             





