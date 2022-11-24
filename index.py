from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from tkinter import *
from tkinter import filedialog

contatos = []
mensagem = []
midia = []


def definir_contato():
    contatos.append(inputContato.get())
    print(contatos)

    inputContato.delete(0, "end")


def remover_contato():
    contatos.clear()
    print(contatos)


def definir_mensagem():
    mensagem.append(inputMensagem.get("1.0", "end-1c"))
    print(mensagem)


def remover_mensagem():
    mensagem.clear()
    print(mensagem)


def definir_imagem():
    imagem = filedialog.askopenfilename(initialdir="/", title="imagemBot", filetypes=(
        ("imgfiles", [".png", "jpg", "jpeg"]), ("all files", "*.*")))
    midia.append(imagem)
    print(midia)


def remover_imagem():
    midia.clear()
    print(midia)
# Funcao que pesquisa o Contato/Grupo


def geral():

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')  # abre o site Whatsapp Web
    time.sleep(20)  # da um sleep de 15 segundos, tempo para scannear o QRCODE'

    def buscar_contato(contatos):
        campo_pesquisa = driver.find_element(
            By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
        time.sleep(2)
        campo_pesquisa.click()
        campo_pesquisa.send_keys(contatos)
        campo_pesquisa.send_keys(Keys.ENTER)

    # Funcao que envia a mensagem
    def enviar_mensagem(mensagem):
        for variasMsg in mensagem:
            mensagem_formatada = variasMsg.split('\n')
            campo_mensagem = driver.find_element(
                By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]')
            campo_mensagem.click()
            time.sleep(3)
            for msg in mensagem_formatada:
                campo_mensagem.send_keys(msg)
                campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)

            campo_mensagem.send_keys(Keys.ENTER)
    # Funcao que envia midia como mensagem

    def enviar_midia(midia):
        for variasMidias in midia:
            driver.find_element(
                By.CSS_SELECTOR, "span[data-icon='clip']").click()
            attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            attach.send_keys(variasMidias)
            time.sleep(3)
            send = driver.find_element(
                By.XPATH, "//div[contains(@class, '_165_h _2HL9j')]")
            send.click()
            time.sleep(1)

    # Percorre todos os contatos/Grupos e envia as mensagens
    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(midia)
        time.sleep(2)


app = Tk()
app.title = "BotZap"
app.geometry("800x800")
app.config(bg='#ffffff')
logo = PhotoImage(file="img/logo.png")
logo = logo.subsample(3,3)
figura1 = Label(image=logo, bg='#ffffff')

figura1.grid(row=0, column=0, padx=(50,0))
figura1.place(x=180, y=0)
Label(app, text="ChatBot do WhatsApp", font=("Poppins", 20), bg="#ffffff" ).place(x=260, y=120)
Label(app, text="Digite o seu contato:", bg="#ffffff", font=("Poppins", 11) ).place(x=10, y=197)
inputContato = Entry(app, highlightcolor= '#000', highlightthickness=1)
inputContato.place(x=150, y=200)

botao1 = Button(app, text="Adicionar", bg="#ffffff" , fg= '#009000',command=definir_contato).place(x=280, y=197)
botao2 = Button(app, text="Remover", command=remover_contato, bg="#ffffff" , fg= '#f00').place(x=350, y=197)

Label(app, text="Digite a sua mensagem:", bg="#ffffff", font=("Poppins", 11) ).place(x=10, y=250)
inputMensagem = Text(app, highlightcolor= '#000', highlightthickness=1)
inputMensagem.place(x=10, y=280, width=550, height=250)
botao3 = Button(app, text="Adicionar mensagem",
       command=definir_mensagem, bg="#ffffff" , fg= '#009000').place(x=10, y=535)
botao4 = Button(app, text="Remover mensagem",
       command=remover_mensagem, bg="#ffffff" , fg= '#f00').place(x=150, y=535)

Label(app, text="Adicionar imagem:", bg="#ffffff", font=("Poppins", 11) ).place(x=10, y=620)
botao5 = Button(app, text="Adicionar mídia", command=definir_imagem, bg="#ffffff" , fg= '#009000').place(x=140, y=620)
botao6 = Button(app, text="Remover mídia", command=remover_imagem, bg="#ffffff" , fg= '#f00').place(x=250, y=620)

botao6 = Button(app, text="Enviar mensagem", command=geral, bg="#009000" , fg= '#ffffff').place(x=300, y=700, width=200, height=40)
app.mainloop()


