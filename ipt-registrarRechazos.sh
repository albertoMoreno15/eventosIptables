#!/bin/bash

#Elimar las reglas en las tablas filter y nat
iptables -t filter -F
iptables -t nat -F

#Reiniciar los contadores en las tablas filter y nat
iptables -t filter -Z
iptables -t nat -Z

#Establecer la politica en las tres cadenas de filter a DROP
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP

#peticiones de una ip concreta y respuestas PING
iptables -A OUTPUT -o enp0s3 -p icmp -j ACCEPT
iptables -A INPUT -i enp0s3 -p icmp -j ACCEPT

#consultas y respuestas DNS 
iptables -A OUTPUT -o enp0s8 -p udp --dport 53 -j ACCEPT
iptables -A INPUT -i enp0s8 -p udp --sport 53 -j ACCEPT

iptables -A OUTPUT -o enp0s8 -p tcp --dport 53 -j ACCEPT
iptables -A INPUT -i enp0s8 -p tcp --sport 53 -j ACCEPT

#habilitar interfaz loopback
iptables -I INPUT 1 -i lo -j ACCEPT
iptables -I OUTPUT 1 -o lo -j ACCEPT

#aceptar trafico http(puerto 80) y https (puerto 443)
iptables -A OUTPUT -o enp0s8 -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -i enp0s8 -p tcp --sport 80 -j ACCEPT

iptables -A OUTPUT -o enp0s8 -p tcp --dport 443 -j ACCEPT
iptables -A INPUT -i enp0s8 -p tcp --sport 443 -j ACCEPT

#aceptar forward 
iptables -A FORWARD -i enp0s3 -o enp0s8 -j ACCEPT
iptables -A FORWARD -i enp0s8 -o enp0s3 -m state --state RELATED,ESTABLISHED -j ACCEPT

#modificar la tabla nat
iptables -t nat -A POSTROUTING -o enp0s8 -j MASQUERADE

#guardar las conexiones rechazadas con prefijo en /var/log/syslog
iptables -A INPUT -j LOG --log-prefix "Conexion rechazada: "
