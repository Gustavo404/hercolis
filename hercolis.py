from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

# Importe o caminho para o msedgedriver
webdriver_path = "C:/Program Files (x86)/msedgedriver.exe"

# Defina o serviço do Microsoft Edge com o caminho para o executável
service = webdriver.EdgeService(executable_path=webdriver_path)

# Defina as opções do Microsoft Edge
options = webdriver.EdgeOptions()
timeout = 15 # Timeout
options.set_capability("timeouts", {"implicit": timeout * 500})
driver = webdriver.Edge(service=service, options=options)
wait = WebDriverWait(driver, 10)  # Defina um tempo limite de espera de 10 segundos

try:
    driver.get("https://administrator.tipbrasil.com.br/zeus_admin/cp_zeus/login")

    # Solicite ao usuário que insira o login e a senha
    usuario = input("Login do Zeus: ")
    senha = input("Senha do Zeus: ")

    # Esperar até que o elemento com o nome "inputUsername" esteja visível
    campo_login = WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.NAME, "inputUsername"))
    )

    campo_login.send_keys(usuario)
    campo_senha = driver.find_element(By.ID, "inputPassword")
    campo_senha.send_keys(senha)

    # Localize o botão pelo atributo onclick usando XPath
    botao_entrar = driver.find_element(By.XPATH, "//button[@onclick='estaVazio();']")

    # Clique no botão
    botao_entrar.click()

    time.sleep(1)

    # Localize o botão pelo id "btnAcessar"
    botao_acessar = driver.find_element(By.ID, "btnAcessar")

    # Clique no botão
    botao_acessar.click()
    time.sleep(1)

    # Encontre "Cadastro"
    botao_cadastro = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/ul/li[2]/a"))
    )
    botao_cadastro.click()

    # Aguarde até que "clientes" esteja visivel
    botao_clientes = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/ul/li[2]/div/div/a[1]"))
    )

    # Clique em Clientes
    botao_clientes.click()

# # LOOP # #

# Abra o arquivo de texto clientes.txt
    with open("clientes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Encontre o campo de entrada e cole o texto da linha
            input_element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/input")
            input_element.clear()
            input_element.send_keys(linha.strip())
            time.sleep(4)

            try:
                elemento = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr[1]/td[2]')
            
                # Se o elemento for encontrado, escreva a variável 'linha' no arquivo 'cadastrado.txt'
                with open("cadastrado.txt", "a", encoding="utf-8") as cadastrado_file:
                    cadastrado_file.write(linha)
            
            except NoSuchElementException:
                # Se o elemento não for encontrado, escreva a variável 'linha' no arquivo 'semCadastrado.txt'
                with open("semCadastrado.txt", "a", encoding="utf-8") as sem_cadastrado_file:
                    sem_cadastrado_file.write(linha)

# # FIM do LOOP # #

    time.sleep(2)
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")



# input:    /html/body/div/div[2]/div/div/div[2]/div[1]/div[1]/div[1]/input
# output:   /html/body/div/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]
