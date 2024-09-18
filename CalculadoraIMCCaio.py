from tkinter import*
from tkinter import ttk


# cores

co0 = '#ffffff'   #branco / white
co1 = '#444466'   #preto  / black
co2 = '#295700'   #verde  / green


janela = Tk()
janela.title('')
janela.geometry('324x232')
janela.configure(bg='white')

# ------------------ dividindo a janela em duas partes --------------

frame_cima = Frame(janela, width=324, height=50, bg=co0, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=324, height=180, bg=co0, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# ------------------ configuração frame cima ------------------------

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 17 bold'), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)
  
#----------------------- função calcular ----------------------------

def calcular():

    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 16:
        l_resultado_texto['text'] = "Magreza Grau III - Desnutrição Severa"

    elif resultado >= 16 and resultado < 17:
        l_resultado_texto['text'] = "Magreza Grau II - Desnutrição Moderada"

    elif resultado >= 17 and resultado < 18.5:
        l_resultado_texto['text'] = "Magreza Grau I - Desnutrição Leve"

    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Eutrofia - Peso Saudável"

    elif resultado >= 25 and resultado < 30:
        l_resultado_texto['text'] = "Sobrepeso - Pré-obesidade"

    elif resultado >= 30 and resultado < 35:
        l_resultado_texto['text'] = "Obesidade Grau I - Obesidade Moderada"

    elif resultado >= 35 and resultado < 40:
        l_resultado_texto['text'] = "Obesidade Grau II - Obesidade Severa"

    else:
        l_resultado_texto['text'] = 'Obesidade Grau III - Obesidade Crítica'


    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

    

# ------------------ configuração frame baixo ------------------------

l_peso = Label(frame_baixo, text='Peso do Paciente', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Altura do Paciente', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)


l_resultado = Label(frame_baixo, text='-', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 26 bold'), bg=co2, fg=co0)
l_resultado.place(x=200, y=10)

l_resultado_texto = Label(frame_baixo, text='Classificação:', width=30, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivy 12 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=10, y=90)

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 11 bold'), bg=co2, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)




janela.mainloop()