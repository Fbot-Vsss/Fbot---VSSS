
import math
from sqlite3 import sqlite_version_info
import FIRALib
from Velocidades import velocidade, mod



def destino(id,team,x,y):
    contador = 1
    x = -x + 0.72
    y = y + 0.61
    while contador==1:
        
        if( team == True):
            PosicaoCarro = FIRALib.amareloCar(id)
        if( team == False):
            PosicaoCarro = FIRALib.AzulCar(id)

        
        pc1 = PosicaoCarro[1] + 0.61
        pc2 =-PosicaoCarro[0] + 0.72
        pc3 = PosicaoCarro[2] + 1.55
        pc4 = PosicaoCarro[2] - 1.55
        pc5 = PosicaoCarro[2] + 0.299
        pc6 = PosicaoCarro[2] - 0.299
        pc7 = PosicaoCarro[2] + 0.298
        pc8 = PosicaoCarro[2] - 0.298
        pc9 = PosicaoCarro[2] + 0.398
        pc10 = PosicaoCarro[2] - 0.398
        if (y) > (pc1):## Se a bola estiver a direita do carrinho
            C = ((x) - (pc2))
            B = ((y) - (pc1))
            if (x) < (pc2):
                theta =  -(3.1 + math.atan(B/C))
                
            else:
                theta =  -math.atan(B/C)

        if (y) < (pc1):## Se a bola estiver a direita do Esquerda
            C = (-(x) + (pc2))
            B = ((y) - (pc1))
            if (x) < (pc2):
                theta =  ( math.atan(B/C) + 3.1)
            else:
                theta =  math.atan(B/C)
##################################################################################################################################################################

        #print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   

        if( pc3 > theta and pc4 < theta ):
            if ((pc5) > theta):
        
                FIRALib.movimente(id,team,-20,-50)#direita


            if ((pc6) < theta):

                FIRALib.movimente(id,team,-50,-20)#esquerda

            if((pc9) > theta and theta > (pc10) ):

                FIRALib.movimente(id,team,-30,-30)
        else:
            if(theta < -2 and PosicaoCarro[2] > 2):
                FIRALib.movimente(id,team,-50,-20)#esquerda
            elif(theta > 2 and PosicaoCarro[2] < -2):
                FIRALib.movimente(id,team,-20,-50)#direita

            else:
                if( theta > 0):
                    if ((pc5 + 3) < theta):
        
                        FIRALib.movimente(id,team,20,50)#Esquerda


                    if ((pc6 + 3) > theta):

                        FIRALib.movimente(id,team,50,20)#Direita
                
                    if((pc7 +3) > theta and theta > (pc8 + 3) ):

                        FIRALib.movimente(id,team,30,30)

                if( theta < 0):
                    if ((pc5 - 3) < theta):
        
                        FIRALib.movimente(id,team,20,50)#Esquerda


                    if ((pc6 - 3) > theta):

                        FIRALib.movimente(id,team,50,20)#Direita
                
                    if((pc7 -3) > theta and theta > (pc8 - 3) ):

                        FIRALib.movimente(0,team,30,30)
        if (pc2+ 0.25 > x and pc2 - 0.25 < x) and ( pc1 + 0.25 > y and pc1 - 0.25 < y):
            
            contador = 0




def SeguiBola(id,team):

    while True:
        PosicaoBola = FIRALib.bola()
    ## FIRALib.movimente(0,True,1,-1)
        if( team == True):
            PosicaoCarro = FIRALib.amareloCar(id)
        if( team == False):
            PosicaoCarro = FIRALib.AzulCar(id)

        pc1 = PosicaoCarro[1] + 0.61
        pc2 =-PosicaoCarro[0] + 0.72
        pc3 = PosicaoCarro[2] + 1.55
        pc4 = PosicaoCarro[2] - 1.55
        pc5 = PosicaoCarro[2] + 0.499
        pc6 = PosicaoCarro[2] - 0.499
        pc7 = PosicaoCarro[2] + 0.498
        pc8 = PosicaoCarro[2] - 0.498
        pc9 = PosicaoCarro[2] + 0.498
        pc10 = PosicaoCarro[2] - 0.498
        pb1 = PosicaoBola[1] + 0.61
        pb2 = -PosicaoBola[0] + 0.72

        if (pb1) > (pc1):## Se a bola estiver a direita do carrinho
            C = ((pb2) - (pc2))
            B = ((pb1) - (pc1))
            modulo = math.sqrt((C*C)+(B*B))
            if (pb2) < (pc2):
                theta =  -(3.1 + math.atan(B/C))
            else:
                theta =  -math.atan(B/C)

        if (pb1) < (pc1):## Se a bola estiver a direita do Esquerda
            C = (-(pb2) + (pc2))
            B = ((pb1) - (pc1))
            modulo = math.sqrt((C*C)+(B*B))
            if (pb2) < (pc2):
                theta =  ( math.atan(B/C) + 3.1)
            else:
                theta =  math.atan(B/C)

###########################################################################################################
       # print("THETA: ",theta,"CARRINHO ORIENTAÇÂO: ",PosicaoCarro[2])   
        print( modulo , theta)
        THETAmod = mod(theta)
        ORImod = mod(PosicaoCarro[2])
        diferen = mod(THETAmod )
        diferen2 = mod( diferen - 1.5)


        if( pc3 > theta and pc4 < theta ):
            print(diferen, "2")
            if ((pc5) > theta):
                velocidade(id,team,-20*(modulo),-50/modulo)


            if ((pc6) < theta):
                velocidade(id,team,-20*(modulo),50/modulo)

            if((pc9) > theta and theta > (pc10) ):
                velocidade(id,team,-33*(modulo*1.5),0)
        else:
            if(theta < -2 and PosicaoCarro[2] > 2):
                velocidade(id,team,-10*(modulo),-50/modulo)
            elif(theta > 2 and PosicaoCarro[2] < -2):
                velocidade(id,team,-10*(modulo),50/modulo)

            else:
                print(diferen2, "1")
                if( theta > 0):
                    if ((pc5 + 3) < theta):
                        velocidade(id,team,20*(modulo),50/modulo)
                        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                    if ((pc6+ 3) > theta):
                        velocidade(id,team,20*(modulo),-50/modulo)
                        print("bbbbbbbbbbbbbbbbbbbbbbbbbbbb")
                    if((pc7 +3) > theta and theta > (pc8 + 3) ):
                        velocidade(id,team,33*(modulo),0)
                        print("cccccccccccccccccccccccccccc")
                if( theta < 0):
                    if ((pc5 - 3) < theta):
                        velocidade(id,team,20*(modulo),50/modulo)
                        print("ddddddddddddddddddddddddddddd")
                    if ((pc6- 3) > theta):
                        velocidade(id,team,20*(modulo),-50/modulo)
                        print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                    if((pc7 -3) > theta and theta > (pc8- 3) ):
                        velocidade(id,team,33*(modulo),0)
                        print("fffffffffffffffffffffffffffffff")
