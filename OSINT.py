#enseñanzas con claude
import whois
import requests
import re
from datetime import datetime


def consultar_whois(dominio):
    datos = whois.whois(dominio)
    return {
        "registrar": datos.registrar,
        "creacion": datos.creation_date,
        "expiracion": datos.expiration_date,
        "servidores_dns": datos.name_servers
    }

def headers(dominio):
    headers_info = requests.get(f"https://{dominio}", timeout= 5)
    return {
        "servidor": headers_info.headers.get("Server", "Desconocido"),
        "tecnologia": headers_info.headers.get("X-Powered-By", "No detectado"),
        "status": headers_info.status_code
    }

def correos(dominio):
    pagina = requests.get(f"https://{dominio}", timeout=5)
    emails = re.findall(r"[\w.-]+@[\w.-]+\.[\w.-]+", pagina.text)
    return list(set(emails))

def generar_reporte(dominio,whois_info,headers_info,emails):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("reporte.txt","w") as f:
        f.write(f"REPORTE OSINT - {dominio}\n")
        f.write(f"fecha: {fecha}\n")
        f.write("\n[WHOIS]\n")
        for clave, valor in whois_info.items():
            f.write(f"{clave}: {valor}\n")
        f.write("\n[HEADERS]\n")
        for clave, valor in headers_info.items():
            f.write(f"{clave}: {valor}\n")
        f.write("\n[CORREOS]\n")
        if emails:
            for email in emails:
                f.write(f"{email}\n")
        else:
            f.write("Ninguno encontrado\n")


dominio = input("dominio sin (https://): ")
try:
    whois_info = consultar_whois(dominio)
    header_info = headers(dominio)
    emails = correos(dominio)

    generar_reporte(dominio,whois_info,header_info,emails)
except Exception as e:
    print("hubo un error al completar la operacion:\n")
    print(f"{e}")