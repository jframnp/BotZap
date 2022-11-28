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
    # Label(app, text=f"{contatos}").place(x=10, y=220)
    print(contatos)
    listarContatos["text"] = ', '.join(contatos)
    
# criando uma função para LIMPAR os contatos, zerando a variavel


def remover_contato():
    contatos.clear()
    # Label(app, text=f"{contatos}").place(x=10, y=220)
    print(contatos)
    listarContatos["text"] = ''

# validando a entrada de dados no tkinter, no input de mensagens


def validarMensagem():
    if len(inputMensagem.get("1.0", "end-1c")) != 0:
        definir_mensagem()
    else:
        messagebox.showerror("Error", "Digite uma mensagem")
        return ()

# função que valida o ultimo botao, antes de executar o bot.


def validarEnviarMensagem():
    if len(contatos) != 0:
        if len(inputMensagem.get("1.0", "end-1c")) != 0:
            geral()
        elif len(midia) != 0:
            geral()
        else:
            messagebox.showerror("Error", "Insira uma mensagem")
    else:
        messagebox.showerror("Error", "Insira um contato")


# definindo uma função para pegar o inputMensagem e salvar na variavel  mensagem


def definir_mensagem():
    mensagem.append(inputMensagem.get("1.0", "end-1c"))
    print(mensagem)

# criando uma função para LIMPAR as mensagens, zerando a variavel


def remover_mensagem():
    mensagem.clear()
    print(mensagem)
    
# function para pegar a imagem, salvar no formato especifico e guardar na variavel midia


def definir_imagem():
    imagem = filedialog.askopenfilename(initialdir="/", title="imagemBot", filetypes=(
        ("imgfiles", [".png", "jpg", "jpeg"]), ("all files", "*.*")))
    midia.append(imagem)
    print(midia)
    listarMidia['text'] = midia

# criando uma função para LIMPAR a variavel midia


def remover_imagem():
    midia.clear()
    print(midia)
    listarMidia["text"] = ''

def reiniciar():
    remover_imagem()
    remover_contato()
    remover_mensagem()

# função que sera executada para iniciar a janela centralizada no seu monitor


def center(app):

    app.update_idletasks()
    width = app.winfo_width()
    frm_width = app.winfo_rootx() - app.winfo_x()
    win_width = width + 2 * frm_width
    height = app.winfo_height()
    titlebar_height = app.winfo_rooty() - app.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = app.winfo_screenwidth() // 2 - win_width // 2
    y = app.winfo_screenheight() // 2 - win_height // 2
    app.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    app.deiconify()

# função que sera executada para iniciar o bot, sendo chamada no ultimo botao do tkinter


def geral():

    driver = webdriver.Chrome(ChromeDriverManager().install())  # abre o chrome
    driver.get('https://web.whatsapp.com/')  # abre o Whatsapp Web
    time.sleep(20)  # 20 seg para scannear o qr code do wpp web

# função para buscar o contato no wpp web
    def buscar_contato(contatos):
        campo_pesquisa = driver.find_element(
            By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')  # class do chrome que fica a aba de "Digite o seu contato"
        time.sleep(2)
        campo_pesquisa.click()  # clicar para digitar
        # colocar os valores da var contatos
        campo_pesquisa.send_keys(contatos)
        campo_pesquisa.send_keys(Keys.ENTER)  # dar enter e entrar na conversa

    # Funcao que envia a mensagem
    def enviar_mensagem(mensagem):
        # loop para formatar as mensagens
        for variasMsg in mensagem:
            mensagem_formatada = variasMsg.split('\n')
            campo_mensagem = driver.find_element(
                By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]')
            campo_mensagem.click()
            time.sleep(3)
            # loop para enviar as mensagens formatadas
            for msg in mensagem_formatada:
                campo_mensagem.send_keys(msg)
                campo_mensagem.send_keys(Keys.SHIFT, Keys.ENTER)
            # enter para a ultima linha, para mandar a mensagem(fora do for)
            campo_mensagem.send_keys(Keys.ENTER)

    # Funcao que envia arquivo midia como mensagem

    def enviar_midia(midia):
        for variasMidias in midia:
            driver.find_element(
                By.CSS_SELECTOR, "span[data-icon='clip']").click()  # selecionar a class do "clipes" do wpp web para entrarmos no finder da mídia
            attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            attach.send_keys(variasMidias)
            time.sleep(3)
            send = driver.find_element(
                By.XPATH, "//div[contains(@class, '_165_h _2HL9j')]")  # selecionar a class da seta para enviar a midia
            send.click()  # clicar na class selecionada
            time.sleep(1)

    # entra em todos os contatos, envia as mensagens e midias...
    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(mensagem)
        enviar_midia(midia)
        time.sleep(2)


# interface do bot com a lib TKinter


# instanciando e configurando nome, tamanho e centralizando a janela...
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

sendIcon = PhotoImage(file="img/send.png")

# logo do bot
figura1 = Label(image=logo, bg='#ffffff')
figura1.grid(row=0, column=0, padx=(50, 0))
figura1.place(x=180, y=0)

# titulo do bot
Label(app, text="ChatBot do WhatsApp", font=(
    "Poppins", 20), bg="#ffffff").place(x=260, y=120)

# entrada de dados para o contato do bot
Label(app, text="Digite o seu contato:", bg="#ffffff",
      font=("Poppins", 11)).place(x=10, y=197)
inputContato = Entry(app, highlightcolor='#000',
                     highlightthickness=1, text="digite seu contato")
inputContato.place(x=150, y=200)

# botao para adicionar os contatos, chamando a função de validação para guardar os dados na variavel
botao1 = Button(app, text="Adicionar", bg="#ffffff", fg='#009000',
                command=validarContato).place(x=280, y=197)
# botao para zerar a variavel de contatos
botao2 = Button(app, text="Remover", command=remover_contato,
                bg="#ffffff", fg='#f00').place(x=350, y=197)

# entrada de dados para as mensagens
Label(app, text="Digite a sua mensagem:", bg="#ffffff",
      font=("Poppins", 11)).place(x=10, y=250)
inputMensagem = Text(app, highlightcolor='#000', highlightthickness=1)
inputMensagem.place(x=10, y=280, width=550, height=250)

# botao para adicionar as mensagens, chamando a função de validação para guardar os dados na variavel
botao3 = Button(app, text="Adicionar mensagem",
                command=validarMensagem, bg="#ffffff", fg='#009000').place(x=10, y=535)
# botao para zerar a variavel de mensagens
botao4 = Button(app, text="Remover mensagem",
                command=remover_mensagem, bg="#ffffff", fg='#f00').place(x=150, y=535)

# botao para adicionar as midias
Label(app, text="Adicionar imagem:*", bg="#ffffff",
      font=("Poppins", 11)).place(x=10, y=620)
botao5 = Button(app, text="Adicionar mídia", command=definir_imagem,
                bg="#ffffff", fg='#009000').place(x=140, y=620)
# excluindo as midias // zerando os dados da variavel
botao6 = Button(app, text="Remover mídia", command=remover_imagem,
                bg="#ffffff", fg='#f00').place(x=250, y=620)

# botao final para instanciar a função geral e rodar o bot!
botao6 = Button(app, text="Enviar mensagem", command=validarEnviarMensagem, bg="#009000",
                fg='#ffffff', image=sendIcon,
                compound=LEFT)
botao6.place(x=300, y=700, width=200, height=40)
Label(app, text="* (Arquivos aceitos: jpeg, jpg, png.)", bg="#ffffff",
      font=("Poppins", 8)).place(x=10, y=650)

listarContatos = Label(app, text="", bg="#ffffff", font=("Poppins", 8))
listarContatos.place(x=10, y=220)

listarMidia = Label(app, text="", bg="#ffffff", font=("Poppins", 8))
listarMidia.place(x=10, y=680)
app.mainloop()
