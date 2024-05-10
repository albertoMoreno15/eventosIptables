#!/usr/bin/env python3

import requests
import re 

idBot='7196173462:AAFaNlrNnuhbHOmsu9nppRKwsFiXE0P6gyM'
idChat='2013519417'
ruta_conexiones_rechazadas="/home/admin1/Escritorio/conexiones_rechazadas.txt"

def borrarContenido(ruta_archivo):
    with open(ruta_archivo,'w') as archivo:
        archivo.write("Conexiones rechazadas:\n")

with open(ruta_conexiones_rechazadas,'r') as archivo:
    mensaje=archivo.read()
    borrarContenido(ruta_conexiones_rechazadas) 
    
    
url= f"https://api.telegram.org/bot{idBot}/sendMessage"
data={"chat_id":idChat,"text":mensaje}
requests.post(url,data)