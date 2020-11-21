#!/usr/bin/env python

# Script que verifica si la ip ingresada corresponde a la misma red del host
# del usuario que ejecuta el script, también dada una mac address, revisa si
# existe en el archivo utilizado como base de datos 
# (https://gitlab.com/wireshark/wireshark/-/raw/master/manuf) 
# y muestra el vendedor de ella.

# Modo de uso:
#
# python3 OUILookup.py

#Use: python3 OUILookup.py --ip <IP<IP>> | --mac <MAC<MAC>> [--help]
    
#    --ip : specify the IP of the host to query.
#	--mac: specify the MAC address to query. P.e. aa:bb:cc:00:00:00.
#	--help: show this message and quit.

import random
import getopt
import sys
import requests
import re
import ipaddress
import socket
from getmac import get_mac_address

#Cuerpo principal
def main():
    try:
        #para tener opciones largas, es necesario colocar las opciones cortas respectivas,
        #aunque no se utilicen. En este caso: -r y -m
        options, args = getopt.getopt(sys.argv[1:],"r,m",['ip=','mac=','help'])
    except:
        print('\n'"Error: Parametros incorrectos.")
        uso()

    if len(sys.argv) != 3:
        uso()

    IP = None
    MAC  = None
    
    for opt, arg in options:
        if opt in ('--help'):
            uso()
        if opt in ('--ip'):
            ip()
        elif opt in ('--mac'):
            mac()
            
    if IP != None and MAC != None:
            print('\n'"Error: Faltan parametros obligatorios.")
            uso()

# Función modo de uso
def uso():
    print('\n' "Use: python3 " + sys.argv[0] + " --ip <IP> | --mac <MAC> [--help] ")
    print("\nParametros:")
    print("     --ip: specify the IP of the host to query.")
    print("     --mac: specify the MAC address to query. P.e. aa:bb:cc:00:00:00.")
    print("     --help: show this message and quit." '\n')
    exit(1)

# Función que verifica si la ip ingresada pertenece a la misma red del host, tambíen muestra 
# mac addres del host
def ip():

    try:
        ip = ipaddress.ip_address(sys.argv[2])
        print('\n%s is a correct IP%s address.\n' % (ip, ip.version))
    except ValueError:
        print('\nIp incorrect')
        uso()
    except:
        print('Usage : %s  ip' % sys.argv[0])
    
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)

    #print ('\nIP of host is: %s' %direccion_equipo)
    
    direccionip = direccion_equipo
    direccionip = direccionip.split('.')
     
    primerOcteto = int(direccionip[0])
    segundoOcteto = int(direccionip[1])
    tercerOcteto = int(direccionip[2])
    cuartoOcteto = int(direccionip[3])
    
    direccionip2 = (sys.argv[2])
    direccionip2 = direccionip2.split('.')
    
    pOcteto1 = int(direccionip2[0])
    sOcteto1 = int(direccionip2[1])
    tOcteto1 = int(direccionip2[2])
    cOcteto1 = int(direccionip2[3])
    
    ip_mac = get_mac_address(str(direccionip))

    if(primerOcteto >= 1 and primerOcteto <=127	):
        #print("\nGiven IP address belongs to Class A")
        if(primerOcteto == pOcteto1):
            print("MAC address : " + ip_mac)
            print("Ip is inside the host network\n")
        else:
            print("Error: ip is outside the host network\n")
    
    elif(primerOcteto >= 128 and primerOcteto <=191):
        #print("\nGiven IP address belongs to Class B")
        if(primerOcteto == pOcteto1 and segundoOcteto == sOcteto1):
            print("MAC address : " + ip_mac)
            print("Ip is inside the host network\n")
        else:
            print("Error: ip is outside the host network\n")
    
    elif(primerOcteto >= 192 and primerOcteto <= 223):
        #print("\nGiven IP address belongs to Class C")
        if(primerOcteto == pOcteto1 and segundoOcteto == sOcteto1 and tercerOcteto == tOcteto1):
            print("MAC address : " + ip_mac)
            print("Ip is inside the host network\n")
        else:
            print("Error: ip is outside the host network\n")
    else:
        print("\nUnknow\n")


    exit(1)    

# Función que revisa que la mac addres ingresada está en la base de datos, en caso de estar
# muestra el vendedor
def mac():

    url = 'https://gitlab.com/wireshark/wireshark/-/raw/master/manuf'

    res = requests.get(url)
    output = res.text
    inputvalue = (sys.argv[2])

    file = open("output.txt", "w")
    file.write(output)

    file = open('output.txt',"r") 
    found = False
    for line in file:  # itera sobre el archivo una línea a la vez
        if re.search(format(inputvalue+"\t"),line):    # si la cadena encontrada está en la línea actual
                                                       # Divide la cadena por el separador especificado,
                                                       # (en este caso un tabulador "\t") en una arreglo
                                                       #  donde cada palabra 
                                                       # es un elemento. 
            line = line.split("\t") 
            line1 = len(line)
            
            if inputvalue == line[1]:
                uso()
            elif line1 == 4:
                print("\nMAC address : " + inputvalue)
                print("\nVendor      : " + line[3])
            elif line1 == 3:
                print("\nMAC address : " + inputvalue)
                print("Vendor      : " + line[2])
            elif line1 == 2:
                print("\nMAC address : " + inputvalue)
                print("\nVendor      : " + line[1])

            found = True
               
    if not found:
        print("\nVendor      : Not found\n")

#Esto se utiliza para poder importar este codigo en otro script para utilizar sus funciones.
if __name__ == '__main__':
    main()
    
    