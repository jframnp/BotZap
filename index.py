# importando todas as dependencias para o projeto rodar

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

# criando variaveis setado como um array vazio para guardar os dados

contatos = []
mensagem = []
midia = []

# validando a entrada de dados no tkinter

def validarContato():
    # se tiver alguma informação na entrada de dados, chamar a definição do contato
    if len(inputContato.get()) != 0:
        definir_contato()
    else:
        # senao, aparecer uma mensagem de erro
        messagebox.showerror("Error", "Digite um contato")
        return ()

# buscando os dados do input e setando para o array vazio
def definir_contato():
    contatos.append(inputContato.get())
    inputContato.delete(0, "end")
    print(contatos)

#criando uma função para LIMPAR os contatos, zerando a variavel
def remover_contato():
    contatos.clear()
    print(contatos)

# validando a entrada de dados no tkinter, no input de mensagens
def validarMensagem():
    if len(inputMensagem.get("1.0", "end-1c")) != 0:
        definir_mensagem()
    else:
        messagebox.showerror("Error", "Digite uma mensagem")
        return ()


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


def center(app):
    # :param app: the main window or Toplevel window to center

    # Apparently a common hack to get the window size. Temporarily hide the
    # window to avoid update_idletasks() drawing the window in the wrong
    # position.
    app.update_idletasks()  # Update "requested size" from geometry manager

    # define window dimensions width and height
    width = app.winfo_width()
    frm_width = app.winfo_rootx() - app.winfo_x()
    win_width = width + 2 * frm_width

    height = app.winfo_height()
    titlebar_height = app.winfo_rooty() - app.winfo_y()
    win_height = height + titlebar_height + frm_width

    # Get the window position from the top dynamically as well as position from left or right as follows
    x = app.winfo_screenwidth() // 2 - win_width // 2
    y = app.winfo_screenheight() // 2 - win_height // 2

    # this is the line that will center your window
    app.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # This seems to draw the window frame immediately, so only call deiconify()
    # after setting correct window position
    app.deiconify()


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

        enviar_mensagem(mensagem)

        enviar_midia(midia)
        time.sleep(2)


app = Tk()
app.iconbitmap('img/Logo.png')
app.resizable(width=False, height=False)
app.title("BotZap")
app.attributes('-alpha', 0.0)
app.geometry("800x800")
center(app)
app.attributes('-alpha', 1.0)
app.config(bg='#ffffff')
logo = PhotoImage(file="img/Logo.png")
logo = logo.subsample(3, 3)
figura1 = Label(image=logo, bg='#ffffff')

figura1.grid(row=0, column=0, padx=(50, 0))
figura1.place(x=180, y=0)
Label(app, text="ChatBot do WhatsApp", font=(
    "Poppins", 20), bg="#ffffff").place(x=260, y=120)
Label(app, text="Digite o seu contato:", bg="#ffffff",
      font=("Poppins", 11)).place(x=10, y=197)
inputContato = Entry(app, highlightcolor='#000',
                     highlightthickness=1, text="digite seu contato")
inputContato.place(x=150, y=200)
# Label(app, text=f"{validarContato()}", font=("Poppins", 11) ).place(x=10, y=220)

botao1 = Button(app, text="Adicionar", bg="#ffffff", fg='#009000',
                command=validarContato).place(x=280, y=197)
botao2 = Button(app, text="Remover", command=remover_contato,
                bg="#ffffff", fg='#f00').place(x=350, y=197)

Label(app, text="Digite a sua mensagem:", bg="#ffffff",
      font=("Poppins", 11)).place(x=10, y=250)
inputMensagem = Text(app, highlightcolor='#000', highlightthickness=1)
inputMensagem.place(x=10, y=280, width=550, height=250)
botao3 = Button(app, text="Adicionar mensagem",
                command=validarMensagem, bg="#ffffff", fg='#009000').place(x=10, y=535)
botao4 = Button(app, text="Remover mensagem",
                command=remover_mensagem, bg="#ffffff", fg='#f00').place(x=150, y=535)

Label(app, text="Adicionar imagem:", bg="#ffffff",
      font=("Poppins", 11)).place(x=10, y=620)
botao5 = Button(app, text="Adicionar mídia", command=definir_imagem,
                bg="#ffffff", fg='#009000').place(x=140, y=620)
botao6 = Button(app, text="Remover mídia", command=remover_imagem,
                bg="#ffffff", fg='#f00').place(x=250, y=620)

botao6 = Button(app, text="Enviar mensagem", command=geral, bg="#009000",
                fg='#ffffff').place(x=300, y=700, width=200, height=40)
app.mainloop()
