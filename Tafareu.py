import FIRALib
import posiciona

## modelando o coleirão
##Goleiro Amarelo


##colocar o carrinho na posição certa
posicionador = 0
orientador = 0
while True:

    Bola = FIRALib.bola()
    Tafareu = FIRALib.amareloCar(0)
##girar o rainho na orientação -1.5
        
    if -Tafareu[0]+0.72 < 0.09:
        
        if (Tafareu[2] + 0.1 > 1.5 and Tafareu[2] - 0.1  < 1.5):
            if Tafareu[1]+0.01 > Bola[1] and Tafareu[1]-0.01 < Bola[1]:
                FIRALib.movimente(0,True,0,0)

            else:
                if Tafareu[1]> Bola[1]:
                    FIRALib.movimente(0,True,-27,-27)
                if Tafareu[1]< Bola[1]:
                    FIRALib.movimente(0,True,27,27)
                if (Tafareu[1]+0.61)< 0.4:
                    FIRALib.movimente(0,True,27,27)
                if Tafareu[1]+0.61> 0.80:
                    FIRALib.movimente(0,True,-27,-27)


        else:
            if (Tafareu[2] > 1.70):
                FIRALib.movimente(0,True,2,-2)
            if (Tafareu[2] < 1.30):
                FIRALib.movimente(0,True,-2,2)
    else:
        posiciona.posicionaBAIXA(0,True,0.04,0.61)



##seguir a bola 










##Goleiro Azul