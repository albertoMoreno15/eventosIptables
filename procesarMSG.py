#!/usr/bin/env python3

import sys
import re 
 
def procesar_log(log): 
    # Usamos expresiones regulares para extraer la información relevante 
    pattern = r"Paquete filtrado:.*SRC=(\S+) DST=(\S+).*SPT=(\d+) DPT=(\d+)" 
    match = re.search(pattern, log) 
 
    if match:  
        src = match.group(1) 
        dst = match.group(2) 
        spt = match.group(3) 
        dpt = match.group(4) 
 
        return f"{src}:{spt} to {dst}:{dpt}" 
    else: 
        return "" 
 

log = sys.stdin.readline()
mensaje=procesar_log(log)
print(mensaje)