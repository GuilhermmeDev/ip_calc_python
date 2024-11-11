import ipaddress

def calc_infos(ip_rede):
    rede = ipaddress.ip_network(ip_rede, strict=False)
    print(f"Endereço da rede: {rede.network_address}")
    print(f"Máscara da rede: {rede.netmask}")
    print(f"Endereço broadcast: {rede.broadcast_address}\n")
    hosts = list(rede.hosts())
    print(f"First Host: {hosts[0]}")
    print(f"Last Host: {hosts[-1]}")

    print(f"Faixa de endereços válidos: {hosts[0]} - {hosts[-1]}")
    print(f"Total de endereços disponíveis: {rede.num_addresses - 2}") # -2, pois tira o endereço da rede e o broadcast
print("Calculadora de IP")
print("-="*25)
calc_infos("192.168.1.0/24")