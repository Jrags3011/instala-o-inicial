import subprocess
import os
import time
import logging

# Configuração do logging
import subprocess
import os
import time
import logging

# Configuração do logging
logging.basicConfig(filename='install_apps.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def install_apps_from_network():
    network_path = r"\\192.168.0.35\informatica\windows novo"  # Certifica de que o caminho está correto
    apps = [
        "ChromeSetup.exe",
        "Firefox Setup 59.0 W7.exe",
        "MicrosoftEdgeSetup.exe",
        "pdf24-creator-installer.exe",
        "Reader_br_install.exe",
        "Setup64.exe",
        "WithSecure Client Security Premium-16.0.exe"
    ]

    # Verifica se a pasta de rede está acessível
    while not os.path.exists(network_path):
        logging.info("Aguardando acesso à pasta de rede...")
        print("Aguardando acesso à pasta de rede...")
        time.sleep(5)  # Espera 5 segundos antes de tentar novamente

    for app in apps:
        app_path = os.path.join(network_path, app)
        if os.path.exists(app_path):
            try:
                logging.info(f"Instalando {app}...")
                print(f"Instalando {app}...")
                result = subprocess.run([app_path, "/silent"], check=True)
                logging.info(f"{app} instalado com sucesso. Código de retorno: {result.returncode}")
            except subprocess.CalledProcessError as e:
                logging.error(f"Erro ao instalar {app}: {e}")
                print(f"Erro ao instalar {app}: {e}")
        else:
            logging.warning(f"{app} não encontrado na pasta de rede.")
            print(f"{app} não encontrado na pasta de rede.")

if __name__ == "__main__":
    install_apps_from_network()
