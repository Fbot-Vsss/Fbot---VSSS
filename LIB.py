import socket
import sys
sys.path.insert(0,"./msg")
from packet_pb2 import Environment, Packet
from command_pb2 import Commands, Command


host = "224.5.23.2"                  #endereços string
porta_recebe = 10002                #porta int  
porta_envia = 10003                 #porta int


socket_envia = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #declaro um socket


def movimente(id, ToF, VE,VD):
    pacote = Packet()
    cmd = Command()
    cmd.id = id
    cmd.yellowteam = ToF
    cmd.wheel_left = VE
    cmd.wheel_right = VD
    pacote.cmd.robot_commands.append(cmd) #esta adiconando ao packet as informações do command ## appen() adiciona um item no final de lista 
    pacote_byte = pacote.SerializeToString()# .SerializeToString() serealiza dos dados
    socket_envia.sendto(pacote_byte,(host, porta_envia))
