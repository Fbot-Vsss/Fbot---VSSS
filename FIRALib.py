import socket
import sys
sys.path.insert(0,"./msg")
from packet_pb2 import Environment, Packet
from command_pb2 import Commands, Command


localhost = "127.0.0.1"                  #endereços string
host = "224.0.0.1"
porta_recebe = 10002                #porta int  
porta_envia = 20011                 #porta int


socket_envia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket



def bola():
    socket_recebe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket
    socket_recebe.bind((host, porta_recebe))# .bind(1 argumento) é usado para endereço local e .connect() para endereço remoto
    ambiente = Environment()            # Ambiente do FIRASIm que foi que esta no packet

##############################################################################################################################

    data, addr = socket_recebe.recvfrom(2048)  #resposta do servidor
    ambiente.ParseFromString(data) #ele preenche a classe stub com os dados da string binária
    frame = ambiente.frame #frame do Envorironment do proto Packet
    ball = frame.ball      #Recebe as cordenas da bola

    return([ball.x, ball.y])


def amareloCar(id):
    socket_recebe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket
    socket_recebe.bind((host, porta_recebe))# .bind(1 argumento) é usado para endereço local e .connect() para endereço remoto
    ambiente = Environment()            # Ambiente do FIRASIm que foi que esta no packet


    data, addr = socket_recebe.recvfrom(2048)  #resposta do servidor
    ambiente.ParseFromString(data) #ele preenche a classe stub com os dados da string binária
    frame = ambiente.frame #frame do Envorironment do proto Packet
    ball = frame.ball      #Recebe as cordenas da bola
    for robot in frame.robots_yellow:
        if robot.robot_id == id:
            return([robot.x, robot.y, robot.orientation])


def AzulCar(id):
    socket_recebe = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket
    socket_recebe.bind((host, porta_recebe))# .bind(1 argumento) é usado para endereço local e .connect() para endereço remoto
    ambiente = Environment()            # Ambiente do FIRASIm que foi que esta no packet


    data, addr = socket_recebe.recvfrom(2048)  #resposta do servidor
    ambiente.ParseFromString(data) #ele preenche a classe stub com os dados da string binária
    frame = ambiente.frame #frame do Envorironment do proto Packet
    ball = frame.ball      #Recebe as cordenas da bola
    for robot in frame.robots_blue:
        if robot.robot_id == id:
            return([robot.x, robot.y, robot.orientation])


def movimente(id, ToF, VE,VD):
    pacote = Packet()
    cmd = Command()
    cmd.id = id
    cmd.yellowteam = ToF
    cmd.wheel_left = VE
    cmd.wheel_right = VD
    pacote.cmd.robot_commands.append(cmd) #esta adiconando ao packet as informações do command ## appen() adiciona um item no final de lista 
    pacote_byte = pacote.SerializeToString()# .SerializeToString() serealiza dos dados
    socket_envia.sendto(pacote_byte,(localhost, porta_envia))
