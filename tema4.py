import streamlit as st

registros=[
    {"nome_cliente": "João","data": "08/11/2025","hora": "19:00","numero_pessoas": 4}
    
    ]

def Adicionar_Reserva(nome,data,hora,numero_pessoas):
    registros.append({"nome_cliente":nome,"data":data ,"hora":hora,"numero_pessoas": numero_pessoas})
    
def listar_reservas():
   st.dataframe(registros)
   
def Consultar_reservas(chave, value):
    d=[r for r in registros if value.lower() in str(r[chave]).lower()]
    st.dataframe(d)

def Remover_reserva(chave,value):
    global registros 
    inicial = len(registros)
    registros = [r for r in registros if value.lower() not in str(r[chave]).lower()]
    removidos = inicial - len(registros)
    if removidos:
        st.success(f"{removidos} reserva(s) removida(s)!")
    else:
        st.warning("Nenhuma reserva encontrada para remoção.")