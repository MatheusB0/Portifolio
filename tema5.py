import os
import json

def adicionar_entrada(texto,data):
    arquivo = "registro.json"
    if os.path.exists(arquivo):
        with open(arquivo,"r", encoding="utf-8") as f:
            reg = json.load(f)
    else:   
        reg = []
    
    reg.append({"data":data,"texto":texto})
    with open(arquivo,"w",encoding="utf-8") as f:
        json.dump(reg,f,ensure_ascii=False,indent=4)
        
def ler_entradas():
    arquivo = "registro.json"
    if os.path.exists(arquivo):
        with open(arquivo,"r", encoding="utf-8") as f:
            return  json.load(f)
    else:   
        return  []
    
def filtra_por_data(data):
    entradas = ler_entradas()
    return [e for e in entradas if e["data"] == data]