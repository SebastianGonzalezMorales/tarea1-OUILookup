#!/usr/bin/env python

# Script que genera tiempos aleatorios de llegada de paquetes con
# una tasa de arribo --rate, entre 0 y --maxtime segundos.

# Modo de uso:
#
# Uso: ./random-test.py --rate <rate>  --maxtime <maximum time> [--help] 
#
# Parametros:
#     --rate: tasa de llegada. Obligatorio
#     --maxtime: tiempo maximo de simulacion. Obligatorio
#     --help: muestra esta pantalla y termina. Opcional
     

import random
import getopt
import sys
import requests
import re
import ipaddress
import socket

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

#
#
#
def uso():
    print('\n' "Use: " + sys.argv[0] + " --ip <IP> | --mac <MAC> [--help] ")
    print("\nParametros:")
    print("     --ip: specify the IP of the host to query.")
    print("     --mac: specify the MAC address to query. P.e. aa:bb:cc:00:00:00.")
    print("     --help: show this message and quit." '\n')
    exit(1)

def ip():

    try:
        ip = ipaddress.ip_address(sys.argv[2])
        print('\n%s is a correct IP%s address.' % (ip, ip.version))
    except ValueError:
        print('ip incorrecta')
        uso()
    except:
        print('Usage : %s  ip' % sys.argv[0])
        #print('\n' "Ip es: " + sys.argv[2] + '\n')
    
    nombre_equipo = socket.gethostname()
    direccion_equipo = socket.gethostbyname(nombre_equipo)

    print ('\nLa IP es: %s' %direccion_equipo)
    
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
    
    if(primerOcteto >= 1 and primerOcteto <=127	):
        print("\nGiven IP address belongs to Class A")
        if(primerOcteto == pOcteto1):
                print("")
                print("Pertenecen a la misma red\n")
        else:
            print("Error: ip is outside the host network\n")
    
    elif(primerOcteto >= 128 and primerOcteto <=191):
        print("\nGiven IP address belongs to Class B")
        if(primerOcteto == pOcteto1 and segundoOcteto == sOcteto1):
            print("")
            print("Pertenecen a la misma red\n")
        else:
            print("Error: ip is outside the host network\n")
    
    elif(primerOcteto >= 192 and primerOcteto <= 223):
        print("\nGiven IP address belongs to Class C")
        if(primerOcteto == pOcteto1 and segundoOcteto == sOcteto1 and tercerOcteto == tOcteto1):
            print("")
            print("Pertenecen a la misma red")
        else:
            print("Error: ip is outside the host network\n")
    else:
        print("\nUnknow\n")


    exit(1)    

def mac():

    url = 'https://gitlab.com/wireshark/wireshark/-/raw/master/manuf'

    res = requests.get(url)

    output = res.text
    inputvalue = (sys.argv[2])

    print("\nMAC address : " + inputvalue)

    #print(output)

    file = open("output.txt", "w")
    file.write(output)

    #print(output)

    file = open('output.txt',"r") 
    found = False
    for line in file:  #iterate over the file one line at a time(memory efficient)
        if re.search(format(inputvalue),line):    #if string found is in current line then print it
             
            line = line.split("\t")
            line1 = len(line)

            if line1 == 3:
                print("Vendor      : " + line[2])
            elif line1 == 2:
                print("Vendor      : " + line[1])

            found = True
               
    if not found:
        print("Vendor      : Not found\n")
    
    
        
#
# Genera Eventos
# Entrada: 
#          rate: tasa de arribo de paquetes.
#          maxTime: tiempo maximo de generacion.
# Salida:
#          eventos : lista que contiene los tiempos de los eventos generados.
#

#def genEvents(rate, maxTime, eventos):
    #t=0
    #while t < maxTime:
      #  dt = random.expovariate(1.0 / rate)
     #   dt = (dt, 1)[dt == 0]

    #    t = (t + dt, maxTime)[t+dt > maxTime]
   #     eventos.append(t)
 
#def showEvents(ev):
 #   for fooEv in ev:
  #      print(fooEv)


#Esto se utiliza para poder importar este codigo en otro script para utilizar sus funciones.
if __name__ == '__main__':
    main()
    
    