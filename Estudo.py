import sys 
import socket 
sys.path.insert(0,"./msg")
from command_pb2 import Command, Commands
from packet_pb2 import Environment, Packet

host = "127.0.0.1"                  #endereços string
porta_recebe = 10002                #porta int  
porta_envia = 20011                 #porta int

socket_recebe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket

socket_recebe.bind((host, porta_recebe))# .bind(1 argumento) é usado para endereço local e .connect() para endereço remoto

socket_envia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket

ambiente = Environment()            # Ambiente do FIRASIm que foi que esta no packet

while True:
    data, addr = socket_recebe.recvfrom(2048)  #resposta do servidor
    ambiente.ParseFromString(data) #ele preenche a classe stub com os dados da string binária
    frame = ambiente.frame #frame do Envorironment do proto Packet
    ball = frame.ball      #Recebe as cordenas da bola
    print(f"Posição da bola:  x = {str(ball.x)}  y = {str(ball.x)}  z = {str(ball.x)}")
    for robot in frame.robots_yellow:
        print(robot)
        print(f"Robo amarelo:  id = {str(robot.robot_id)}  x = {str(robot.x)}  y = {str(robot.x)}  Orientação = {str(robot.orientation)}")
    
    ##############################################################################################################################################
    
    pacote = Packet()
    cmd = Command()
    cmd.id = 0
    cmd.yellowteam = True
    cmd.wheel_left = 1000
    cmd.wheel_right = 1000
    pacote.cmd.robot_commands.append(cmd) #esta adiconando ao packet as informações do command ## appen() adiciona um item no final de lista 
    pacote_byte = pacote.SerializeToString()# .SerializeToString() serealiza dos dados
    socket_envia.sendto(pacote_byte,(host, porta_envia))