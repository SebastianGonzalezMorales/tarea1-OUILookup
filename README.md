## Autor: Sebastián González Morales

## Correo institucional: Sebastian.gonzalez@alumnos.uv.cl

## Modo de uso

Ejemplo de uso sin parámetros o con la opción --help.

**./OUILookup**

Use: ./OUILookup --ip <IP> | --mac <IP> [--help]
    
    --ip : specify the IP of the host to query.
	--mac: specify the MAC address to query. P.e. aa:bb:cc:00:00:00.
	--help: show this message and quit.

**Ejemplo de uso con parámetros:**

***Caso ip que pertenezca a su misma red***

**./OUILookup --ip 192.168.1.5**

    MAC address : b4:b5:fe:92:ff:c5
    Vendor      : Hewlett Packard

***Caso ip que NO pertenezca a su misma red***

**./OUILookup --ip 192.168.10.5**

    Error: ip is outside the host network
    Caso MAC que esté en la base de datos

**./OUILookup --mac 98:06:3c:92:ff:c5**

    MAC address : 98:06:3c:92:ff:c5
    Vendor      : Samsung Electronics Co.,Ltd
    Caso MAC que no esté en la base de datos

**./OUILookup --mac 98:06:3f:92:ff:c5**
    
    MAC address : 98:06:3f:92:ff:c5
    Vendor      : Not found
