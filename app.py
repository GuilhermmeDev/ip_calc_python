import pandas as pd
import streamlit as st
from calc import Calculadora

st.set_page_config(page_title="Calculadora de IP")

"""
# Calculadora de IP
Esta calculadora de rede em Python permite obter informações importantes de uma **sub-rede, como o endereço da rede, a máscara de sub-rede, o endereço de broadcast e a faixa de endereços IP válidos**, facilitando a configuração e análise de redes.
"""

calc = Calculadora()


def classeRede(ip):
    first_oct = int(ip.split('.')[0])
    if (1 <= first_oct <= 127):
        network_class = 'Classe A'
    elif (128 <= first_oct <= 191):
        network_class = 'Classe B'
    elif (192 <= first_oct <= 223):
        network_class = 'Classe C'
    elif (224 <= first_oct <= 239):
        network_class = 'Classe D'
    else:
        network_class = 'Classe E'

    return network_class

def calculaRede(ip, mask):
    rede = ip.strip() + mask.strip()
    results = calc.calc_infos(rede)

    network_class = classeRede(ip)
    hosts = list(results.hosts())

    results_view = [
        {'Descrição': 'Endereço da Rede', 'Valor': str(results.network_address)},
        {'Descrição': 'Máscara da Rede', 'Valor': str(results.netmask)},
        {'Descrição': 'Endereço Broadcast', 'Valor': str(results.broadcast_address)},
        {'Descrição': 'Primeiro Host', 'Valor': str(hosts[0])},
        {'Descrição': 'Último Host', 'Valor': str(hosts[-1])},
        {'Descrição': 'Classe de Rede', 'Valor': network_class},
        {'Descrição': 'Qtd. SubRedes', 'Valor': results.num_addresses},
        {'Descrição': 'Hosts por SubNet', 'Valor': results.num_addresses - 2},
        {'Descrição': 'Endereço Público/Privado', 'Valor': "Público" if results.is_private else "Privado"}
    ]
    st.dataframe(results_view, width=1000)

ip = st.text_input(label="Digite o IP desejado para mapear:", placeholder="Ex: 127.0.0.1")
mask = st.text_input(label="Digite a máscara da rede:", placeholder="Ex: /24")

if st.button(label="Mapear IP"):
    calculaRede(ip, mask)
