import streamlit as st
from calc import Calculadora

st.set_page_config(page_title="Calculadora de IP")

"""
# Calculadora de IP
Esta calculadora de rede em Python permite obter informações importantes de uma **sub-rede, como o endereço da rede, a máscara de sub-rede, o endereço de broadcast e a faixa de endereços IP válidos**, facilitando a configuração e análise de redes.
"""
calc = Calculadora()
def calculaRede(ip, mask):
    rede = ip.strip() + mask.strip()
    results = calc.calc_infos(rede)
    st.write("Endereço da rede: ", results.network_address)
    st.write("Máscara da rede: ", results.netmask)
    st.write("Endereço Broadcast: ", results.broadcast_address)
    hosts = list(results.hosts())
    st.write('First host: ', hosts[0])
    st.write('Last host: ', hosts[-1])
    st.write('Faixa de endereços disponíveis: ', results.num_addresses - 2)
    

ip = st.text_input(label="Digite o IP desejado para mapear:", placeholder="Ex: 127.0.0.1")
mask = st.text_input(label="Digite a máscara da rede:", placeholder="Ex: /24")

if (st.button(label="Mapear IP")):
    calculaRede(ip,mask)