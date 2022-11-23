from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 
import time

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web
time.sleep(20) #da um sleep de 15 segundos, tempo para scannear o QRCODE

#Contatos/Grupos - Informar o nome(s) de Grupos ou Contatos que serao enviadas as mensagens
contatos = ['Informações curso técnico']
contatos2 = ['Vagas de emprego']

#Mensagem - Mensagem que sera enviada
mensagem = ['Bom dia! O Senai Suiço-Brasileira está com vagas abertas para a inscrição dos cursos técnicos para o primeiro semestre de 2023. Confira os cursos:', '✅ Desenvolvimento de Sistemas (tarde)' , '✅ Redes de computadores (manhã) ' , '✅ Qualidade de vida (noite)' ,
'Para mais informações acesse o link abaixo ou escaneie o QR code.' ,  'https://suicobrasileira.sp.senai.br']


mensagem2 = ['Olá!! Procurando vagas de emprego? O Senai-SP tem as melhores oportunidades de trabalho para todos os cargos e áreas, conheça alguns de nossos beneficios:',
'✅ Vale Transporte',
'✅ Auxilio Creche',
'✅ Seguro de vida',
'✅ Plano de Previdência Privada',
'Ficou interessado? Para mais informações acesse nosso link:' , 'https://sesisenaisp.jobs.recrut.ai/ ou escaneie o QR code abaixo']

#Midia = imagem, pdf, documento, video (caminho do arquivo, lembrando que mesmo no windows o caminho deve ser passado com barra invertida */* ) 
midia = "C:/Users/Aluno/Documents/codeSenai.png"
midia2 = "C:/Users/Aluno/Documents/vagas.png"

#Funcao que pesquisa o Contato/Grupo
def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH,'//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

#Funcao que envia a mensagem
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.XPATH,'//p[contains(@class,"selectable-text copyable-text")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys((mensagem[0]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem[1]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER,)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER,)
    campo_mensagem.send_keys((mensagem[2]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem[3]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem[4]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem[5]))
    campo_mensagem.send_keys(Keys.ENTER)

def enviar_mensagem2(mensagem2):
    campo_mensagem = driver.find_element(By.XPATH,'//p[contains(@class,"selectable-text copyable-text")]')
    campo_mensagem.click()
    time.sleep(3)
    campo_mensagem.send_keys((mensagem2[0]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem2[1]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER,)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER,)
    campo_mensagem.send_keys((mensagem2[2]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem2[3]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem2[4]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem2[5]))
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
    campo_mensagem.send_keys((mensagem2[6]))
    campo_mensagem.send_keys(Keys.ENTER)

#Funcao que envia midia como mensagem
def enviar_midia(midia):
    driver.find_element(By.CSS_SELECTOR , "span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element(By.XPATH,"//div[contains(@class, '_165_h _2HL9j')]")
    send.click()   

def enviar_midia2(midia2):
    driver.find_element(By.CSS_SELECTOR , "span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
    attach.send_keys(midia2)
    time.sleep(3)
    send = driver.find_element(By.XPATH,"//div[contains(@class, '_165_h _2HL9j')]")
    send.click()    

#Percorre todos os contatos/Grupos e envia as mensagens
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)       
    enviar_midia(midia) 
    time.sleep(2)

for contato in contatos2:
    buscar_contato(contato)
    enviar_mensagem2(mensagem2)  
    enviar_midia2(midia2)      
    time.sleep(2)

    # vitor777