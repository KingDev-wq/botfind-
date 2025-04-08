
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
from datetime import datetime

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(r"""
╔════════════════════════════════════════════════╗
║         █▄▀ █ █▄█ █▄█ ▀█▀ █▀▀ █░█ █▀█         ║
║         █░█ █ ░█░ ░█░ ░█░ ██▄ █▀█ █▄█         ║
║            OSINT TOOL - KingSearch v1.0       ║
║          Data: {}      ║
╚════════════════════════════════════════════════╝
""".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

def menu():
    print("1. Buscar username (Instagram, Twitter, GitHub, etc)")
    print("2. Verificar e-mail (vazamentos)")
    print("3. Buscar telefone (busca reversa)")
    print("4. Rastrear carteira crypto (BTC/ETH)")
    print("5. Buscar no Telegram")
    print("6. Busca simulada na Dark Web")
    print("7. Super Busca via IA (@username)")
    print("8. Sair")
    escolha = input("\n>>> Escolha: ")
    match escolha:
        case '1': buscar_username()
        case '2': verificar_email()
        case '3': buscar_telefone()
        case '4': rastrear_crypto()
        case '5': buscar_telegram()
        case '6': buscar_darkweb()
        case '7': super_ia()
        case '8': sair()
        case _: print("Opção inválida."); time.sleep(1); main()

def buscar_username():
    usuario = input("Digite o nome de usuário: @")
    print(f"Buscando por @{usuario} em redes sociais...")
    print(f"[+] Instagram: https://instagram.com/{usuario}")
    print(f"[+] GitHub: https://github.com/{usuario}")
    print(f"[+] Twitter: https://twitter.com/{usuario}")
    print(f"[+] TikTok: https://tiktok.com/@{usuario}")
    input("\n[Enter] para voltar")
    main()

def verificar_email():
    email = input("Digite o e-mail: ")
    print(f"Verificando se o e-mail '{email}' está em vazamentos...")
    print("[Simulado] Vazamento encontrado: Netflix - 2020")
    print("[Simulado] Vazamento encontrado: Mercado Livre - 2021")
    input("\n[Enter] para voltar")
    main()

def buscar_telefone():
    telefone = input("Digite o telefone com DDD: ")
    print(f"Buscando dados públicos para {telefone}...")
    print("[Simulado] Nome: Lucas S.")
    print("[Simulado] Localização: São Paulo - SP")
    print("[Simulado] Operadora: Claro")
    input("\n[Enter] para voltar")
    main()

def rastrear_crypto():
    wallet = input("Digite o endereço da carteira (BTC/ETH): ")
    print(f"Consultando transações da carteira {wallet}...")
    print("[Simulado] Última transação: 0.083 BTC recebidos - 03/03/2024")
    print("[Simulado] Total movimentado: 0.72 BTC")
    input("\n[Enter] para voltar")
    main()

def buscar_telegram():
    username = input("Digite o username do Telegram: @")
    print(f"Buscando informações públicas do Telegram para @{username}...")
    print("[Simulado] Nome: Lucas Hacker")
    print("[Simulado] Última vez online: 2 dias atrás")
    input("\n[Enter] para voltar")
    main()

def buscar_darkweb():
    termo = input("Digite o termo (e-mail, user, telefone): ")
    print(f"Buscando em dumps da dark web por '{termo}'...")
    print("[Simulado] Encontrado em 3 dumps:")
    print("- breach_compilation_2023")
    print("- leaks_collection #1")
    print("- netshoes_2021")
    input("\n[Enter] para voltar")
    main()

def super_ia():
    user = input("Digite o @username: @")
    print(f"Rastreando tudo sobre @{user} com ajuda da IA...
")
    time.sleep(1)
    print(f"[+] Nome: Lucas S.")
    print(f"[+] Instagram: https://instagram.com/{user}")
    print(f"[+] Conta: PRIVADA")
    print(f"[+] Localização provável: São Paulo, SP")
    print(f"[+] Número vazado: (11) 9****-2281")
    print(f"[+] E-mail: lucas.s****@gmail.com")
    print(f"[+] Vazamentos: Netflix, Mercado Livre, Deezer")
    print(f"[+] Contas associadas: TikTok, Twitter")
    print(f"[+] Avatar: https://instagram.com/{user}/profile.jpg")
    print(f"[+] Dark Web: Match em 3 bancos de dados")
    print("\n[KinG IA] Recomendo verificação completa no Collection #1")
    input("\n[Enter] para voltar")
    main()

def sair():
    print("Saindo do KingSearch...")
    sys.exit()

def main():
    clear()
    banner()
    menu()

if __name__ == "__main__":
    main()
