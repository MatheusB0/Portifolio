import streamlit as st
import requests as r
import time
import random
from tema1 import QUIZ,Difficulty
from tema2 import calcular
from tema3 import *
from tema4 import *
from tema5 import adicionar_entrada,filtra_por_data
from tema6 import fibonacci_lista
from tema7 import busca_binaria,busca_sequencial
from tema8 import buscar_filme
from consultar_cep import consulta_cep
from cotacao_dolar import cotar
from Extra import Busca_Poke
st.set_page_config("Portfólio de Algoritmos", layout="centered")
st.title("Portfólio - Construção Algoritmos")

menu = st.sidebar.radio(
    "Choose a Teme",
    ("Decisão e Repetição",
    "Vetores e Matrizes", 
    "Funções e Bibliotecas", 
    "Registros", 
    "Arquivos em Disco", 
    "Recursividade", 
    "Complexidade de tempo do algoritmo (Big O)", 
    "Uso de APIs externas",
    "Consultar Cep",
    "Cotação do Dolar",
    "Extra")
)

match menu:
    case "Decisão e Repetição":
        st.header("Tema 1 - Decisão e Repetição")

        if "p" not in st.session_state:
            st.session_state.p = 0
        
        if "counter" not in st.session_state:
            st.session_state.counter = 0
        if "Points" not in st.session_state:
            st.session_state.Points=0
        s = st.session_state.p
        st.divider()
        st.progress(s / 20)
        
        couter = st.session_state.counter
        Points = st.session_state.Points

        i=0
        if s < len(QUIZ[Difficulty[i]]):
            if couter>3:
                i=2
            elif couter>1:
                i=1
            else:
                i=0
            st.markdown(f"## {QUIZ[Difficulty[i]][s]['pergunta']}")   
            aswer = st.radio(
                label="",
                options=QUIZ[Difficulty[i]][s]["opcoes"],
                key=f"resp_{s}",
            )
           
            if st.button("Confirmar"):
                if aswer == QUIZ[Difficulty[i]][s]["opcoes"][QUIZ[Difficulty[i]][s]["correta"]]:
                    st.success("Correta")
                    st.session_state.counter += 1
                    st.session_state.Points +=1
                else:
                    st.error("Errou")
                    st.session_state.counter = 0

                st.session_state.p += 1
                st.rerun()

        else:
            if Points>19:
                st.balloons()
            st.success("Fim do quiz!")
            st.metric("Resultado Final", f"{Points} / 20")
            if st.button("Reiniciar Quiz"):
                st.session_state.p = 0
                st.session_state.Points = 0
                st.session_state.counter = 0
                st.rerun()
        with st.expander("Decisão e Repetição"):
            st.markdown(
                """### 1️⃣ Quiz Adaptativo (Decisão e Repetição)
**Objetivo:** Testar conhecimentos de programação usando perguntas de dificuldade variável.  
**Como funciona:** Perguntas são apresentadas sequencialmente; se o usuário acerta consecutivamente, a dificuldade aumenta; se erra, diminui. Mostra pontuação final ao terminar.  
**Conteúdos aplicados:** Estruturas de decisão (`if`), estruturas de repetição (`while`), listas e dicionários, `st.session_state`."""
            )
            
    case "Vetores e Matrizes":
        st.header("Tema 2 - Vetores e Matrizes")
        st.markdown("### Digite os valores do vetor Separados por (,)")
        vetor = st.text_input("")
        if st.button("Calcular"):
            calcular(vetor)
        with st.expander("Vetores e Matrizes"):
            st.markdown(
                """### 2️⃣ Vetores e Matrizes (Cálculos Estatísticos)
**Objetivo:** Trabalhar com vetores e matrizes e calcular estatísticas.  
**Como funciona:** Usuário entra com uma lista de números . Calcula soma, média, mediana, moda, mínimo e máximo usando NumPy.  
**Conteúdos aplicados:** Vetores e matrizes, funções e bibliotecas (`numpy`), estruturas de repetição."""
            )
        
    case "Funções e Bibliotecas":
        st.header("Tema 3 - Funções e Bibliotecas")
        
        email = st.text_input("Email:")
        cpf = st.text_input("CPF (ex: 123.456.789-10):")
        senha = st.text_input("Senha:")
        data = st.text_input("Data (dd/mm/aaaa):")
        
        if st.button("Validar"):
            if validar_email(email):
                st.success("Email válido!")
            else:
                st.error("Email inválido!")

            if validar_cpf(cpf):
                st.success("CPF válido!")
            else:
                st.error("CPF inválido!")

            if validar_senha(senha):
                st.success("Senha válida!")
            else:
                st.error("Senha inválida!")

            if validar_data(data):
                st.success("Data válida!")
            else:
                st.error("Data inválida!")
        with st.expander("Funções e Bibliotecas"):
            st.markdown(
                """### 3️⃣ Funções e Bibliotecas (Validador de Dados)
**Objetivo:** Validar informações digitadas pelo usuário.  
**Como funciona:** Usuário digita dados como nome, idade, email ou telefone. O programa valida o formato e alerta se houver erro.  
**Conteúdos aplicados:** Funções (`def`), bibliotecas como `re` (expressões regulares), condicionais."""
            )
    case "Registros":
        st.header("Tema 4 - Registros")
        aba_registro, aba_consulta, aba_remove = st.tabs(["Registrar Reserva", "Consultar Reserva","Remover Reserva"])

        with aba_registro:
            name = st.text_input("Nome:", key="reg_name")
            date = st.date_input("Data:", key="reg_date")
            hora = st.time_input("Hora:", key="reg_hora")
            n_pessoas = st.number_input("Numero de Pessoas:", 1, 20, key="reg_pessoas")
            
            if st.button("Registrar_Reserva", key="btn_registrar"):
                Adicionar_Reserva(name, date, hora, n_pessoas)
            if st.button("Listar Reservas", key="btn_listar"):
                listar_reservas()

        with aba_consulta:
            aba, aba2 = st.tabs(["Buscar Por Nome","Buscar Por data"])
            with aba:
                nome = st.text_input("Nome: ", key="cons_nome")
                if st.button("Buscar", key="btn_buscar_nome"):
                    Consultar_reservas("nome_cliente", nome)
            with aba2:
                data = st.date_input("Data: ", key="cons_data")
                if st.button("Buscar", key="btn_buscar_data"):
                    Consultar_reservas("data", str(data))

        with aba_remove:
            aba, aba2 = st.tabs(["Remover Por Nome","Remover Por data"])
            with aba:
                nome = st.text_input("Nome: ", key="rem_nome")
                if st.button("Remover", key="btn_rem_nome"):
                    Remover_reserva("nome_cliente", nome)
            with aba2:
                data = st.date_input("Data: ", key="rem_data")
                if st.button("Remover", key="btn_rem_data"):
                    Remover_reserva("data", str(data))
        with st.expander("Registros"):
            st.markdown(
                """### 4️⃣ Registros e Consultas (Sistema de Reservas)
**Objetivo:** Gerenciar reservas, permitindo registrar, consultar e remover.  
**Como funciona:** Três abas: Registrar, Consultar e Remover. Permite busca por nome ou data e mostra registros em tabela.  
**Conteúdos aplicados:** Listas de registros (dicionários), estruturas de decisão, repetição para mostrar múltiplos resultados, Streamlit (`st.tabs`, `st.button`, `st.text_input`)."""
            )

    case "Arquivos em Disco":
        st.header("Tema 5 - Arquivos em Disco")
        with st.expander("Adicionar Entrada"):
            data = st.date_input("Data:")
            texto = st.text_area("Texto")
            if st.button("Adicionar"):
                adicionar_entrada(texto,data.strftime("%d/%m/%Y"))
                st.success("Entrada Adicionada!")
        
        with st.expander("Consultar Entradas"):
            data_busca = st.date_input("Filtrar por data", key="busca_data")
            if st.button("Buscar"):
                res = filtra_por_data(data_busca.strftime("%d/%m/%Y"))
                if res:
                    for e in res:
                        st.markdown(f"**{e["data"]}**: {e["texto"]}")
                    
                else:
                    st.warning("Nenhuma Entrada Encontrada")
        with st.expander("Arquivos em Disco"):
            st.markdown(
                """### 5️⃣ Arquivos em Disco
**Objetivo:** Salvar e carregar dados em arquivos externos.  
**Como funciona:** Usuário registra informações que são salvas em arquivo `.txt` ou `.csv`. Permite ler novamente os dados para exibição ou edição.  
**Conteúdos aplicados:** Leitura e escrita de arquivos (`open`, `read`, `write`), manipulação de listas e dicionários, Streamlit."""
            )
    case "Recursividade":
        st.header("Tema 6 - Recursividade")
        n = st.slider("Quantos Termos", min_value=1, max_value=30, value=10)
        if st.button("Gerar Fibonacci"):
            seq = fibonacci_lista(n)
            st.markdown(f"Sequencia: {seq}")
            st.bar_chart(seq)
        with st.expander("Recursividade"):
            st.markdown(
                """### 6️⃣ Recursividade (Fatorial / Sequência)
**Objetivo:** Resolver problemas usando funções recursivas.  
**Como funciona:** Calcula fatorial ou sequência de Fibonacci de um número digitado. A função chama a si mesma até atingir o caso base.  
**Conteúdos aplicados:** Funções recursivas, estruturas de decisão, controle de fluxo para casos base e recursivos."""
            )
    case "Complexidade de tempo do algoritmo (Big O)":
        st.header("Tema 7 - Complexidade de tempo do algoritmo (Big O)")
        tamanho = st.slider("Tamanho da lista:", min_value=1000, max_value=100000, value=1000)
        valor = st.number_input("Valor a buscar:",max_value=tamanho)
        
        lista = random.sample(range(tamanho), tamanho)
        lista_ordenada = sorted(lista)
        if st.button("Executar Busca"):
            start = time.perf_counter() 
            _, comp_seq = busca_sequencial(lista_ordenada, valor)
            tempo_seq = time.perf_counter()  - start

            start = time.perf_counter() 
            _, comp_bin = busca_binaria(lista_ordenada, valor)
            tempo_bin = time.perf_counter() - start

            st.subheader("Resultados")
            st.write(f"Pesquisa Sequencial → Comparações: {comp_seq}, Tempo: {tempo_seq:.6f}s")
            st.write(f"Pesquisa Binária → Comparações: {comp_bin}, Tempo: {tempo_bin:.6f}s")

            st.bar_chart({"Sequencial": comp_seq, "Binária": comp_bin})
        with st.expander("Complexidade de tempo do algoritmo (Big O)"):
            st.markdown(
                """### 7️⃣ Complexidade de Algoritmo (Big O)
**Objetivo:** Comparar eficiência de diferentes algoritmos.  
**Como funciona:** Implementa pesquisa sequencial e binária, ordenação por seleção e quicksort. Mostra tempo de execução e número de comparações.  
**Conteúdos aplicados:** Estruturas de repetição, listas e funções, análise de algoritmos (tempo de execução, complexidade).
"""
            )
    case "Uso de APIs externas":
        st.header("Tema 8 - Uso de APIs externas")
        titulo = st.text_input("Digite o nome do filme:")
        if st.button("Buscar"):
            buscar_filme(titulo)
        with st.expander("Uso de APIs externas"):
            st.markdown(
                """### 8️⃣ Uso de APIs Externas (OMDb)
**Objetivo:** Buscar e exibir informações de filmes e séries em tempo real.  
**Como funciona:** Usuário digita o nome do filme ou série e o app retorna poster, sinopse, gênero, diretor, atores e avaliação IMDb. Permite múltiplos resultados e interatividade via Streamlit.  
**Conteúdos aplicados:** Requisições HTTP (`requests`), processamento de JSON, repetição para múltiplos resultados, cache de dados, tratamento de erros, Streamlit (`st.image`, `st.columns`, `st.selectbox`, `st.markdown`)."""
            )
    case "Consultar Cep":
        st.header("Consultar Cep")
        cep = st.text_input("Cep: ")
        if st.button("Consultar"):
            st.markdown(consulta_cep(cep))
    case "Cotação do Dolar":
        st.header("Cotação do Dolar")
        data = st.date_input("Data:")
        if st.button("Cotar"):
            data_formatada = data.strftime("%m-%d-%Y") 
            r=cotar(data_formatada)
            st.markdown(f"### R${r}")
            
    case "Extra":
        st.header("Extra")
        poke_name = st.text_input("Digite o nome ou número do Pokémon:").lower()
        if st.button("Buscar Pokémon"):
            Busca_Poke(poke_name)
            
    
    