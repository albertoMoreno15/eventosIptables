#!/usr/bin/env python3

import requests
import re 
import sys

idBot=''
idChat=''
ruta_conexiones_filtradas="/home/admin1/paquetesFiltrados.txt"

def borrarContenido(ruta_archivo):
    with open(ruta_archivo,'w') as archivo:
        archivo.write("Conexiones filtradas:\n")

with open(ruta_conexiones_filtradas,'r') as archivo:
    mensaje=archivo.read()
    borrarContenido(ruta_conexiones_filtradas) 
    
    
url= f"https://api.telegram.org/bot{idBot}/sendMessage"
if len(mensaje)>4096:
    for i in range(0,len(mensaje),4096):
        fragmento=mensaje[i:i+4096]
        data={"chat_id":idChat,"text":fragmento}
        requests.post(url,data)
else:
    data={"chat_id":idChat,"text":mensaje}
    requests.post(url,data)
