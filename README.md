## Autor: Sebastián González Morales

## Correo institucional: Sebastian.gonzalez@alumnos.uv.cl

## Modo de uso

Ejemplo de uso sin parámetros o con la opción --help.

**python3 OUILookup.py**

Use: python3 OUILookup.py --ip <IP<IP>> | --mac <MAC<MAC>> [--help]
    
    --ip : specify the IP of the host to query.
	--mac: specify the MAC address to query. P.e. aa:bb:cc:00:00:00.
	--help: show this message and quit.

**Ejemplo de uso con parámetros:**

***Caso ip que pertenezca a su misma red***

**python3 OUILookup.py --ip 192.168.1.5**

    MAC address : b4:b5:fe:92:ff:c5
    Vendor      : Hewlett Packard

***Caso ip que NO pertenezca a su misma red***

**python3 OUILookup.py --ip 192.168.10.5**

    Error: ip is outside the host network
    Caso MAC que esté en la base de datos

**python3 OUILookup.py --mac 98:06:3c:92:ff:c5**

    MAC address : 98:06:3c:92:ff:c5
    Vendor      : Samsung Electronics Co.,Ltd
    Caso MAC que no esté en la base de datos

**python3 OUILookup.py --mac 98:06:3f:92:ff:c5**
    
    MAC address : 98:06:3f:92:ff:c5
    Vendor      : Not found

## A tener en cuenta

En caso de cualquier problema al ejecutar el script instalar lo siguiente

Python utiliza un sistema de gestión y administración de paquetes de sofware:  instalarlo con **sudo apt install python3-pip.** 

También instale el paquete getmac, paquete con el cual se puede obtener dirección MAC de las interfaces de res y los host en la red Local,  **pip3 install getmac**.