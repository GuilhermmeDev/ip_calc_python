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
print("Formato: ")
print("Ex: 127.0.0.1/24")
network = input('Digite a rede que queres mapear: ').strip()
print("-" * 50)
calc_infos(network)