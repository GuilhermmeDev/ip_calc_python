import ipaddress
class Calculadora:
    def calc_infos(self, ip_rede):
        rede = ipaddress.ip_network(ip_rede, strict=False)
        return rede
