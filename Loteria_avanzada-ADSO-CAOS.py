from tkinter import *
from tkinter import messagebox
import random
import time
import os
dia_adso=1
dia_cocina=1
dia_multimedia=1

semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
colores=["gris", "violeta", "amarillo", "rojo", "azul", "naranja", "verde"]
numeros_adso=[]
resultados_adso=[]
colores_random_adso=[]
numeros_usuario_adso=[]
colores_usuario_adso=[]
numeros_cocina=[]
resultados_cocina=[]
colores_random_cocina=[]
numeros_usuario_cocina=[]
colores_usuario_cocina=[]
numeros_multimedia=[]
resultados_multimedia=[]
colores_random_multimedia=[]
numeros_usuario_multimedia=[]
colores_usuario_multimedia=[]
def hoy_es(day):
    if day in [7*x-6 for x in range(1, 99)]:
        return semana[0]
    elif day in [7*x-5 for x in range(1, 99)]:
        return semana[1]
    elif day in [7*x-4 for x in range(1, 99)]:
        return semana[2]
    elif day in [7*x-3 for x in range(1, 99)]:
        return semana[3]
    elif day in [7*x-2 for x in range(1, 99)]:
        return semana[4]
    elif day in [7*x-1 for x in range(1, 99)]:
        return semana[5]
    else:
        return semana[6]
precio=5000
oportunidad=0
class Sorteo:
    def __init__(self, titulo_l, cantidad, again):
        global dia_adso
        global dia_cocina
        global dia_multimedia
        global resultados_adso
        global colores_random_adso
        global numeros_adso
        global numeros_cocina
        global resultados_cocina
        global colores_random_cocina
        global numeros_multimedia
        global resultados_multimedia
        self.click=0
        self.titulo_l=titulo_l
        self.cantidad=cantidad
        self.again=again
        self.numeros_usuario=[]
        self.colores_usuario=[]
        self.dia_wk=dia_adso if self.titulo_l=='Loteria ADSO' else dia_cocina if self.titulo_l=='Loteria Cocina' else dia_multimedia
        self.color_ganador=random.choice(colores)
        self.numero_ganador=str(random.choice(range(10)))+str(random.choice(range(10)))+str(random.choice(range(10)))+str(random.choice(range(10)))
        self.ventana_sorteo=Tk()
        self.ventana_sorteo.title(self.titulo_l)
        self.marco_dia=Frame(self.ventana_sorteo, bg='black')
        self.marco_dia.pack(side=TOP)
        self.marco_terminal=Frame(self.ventana_sorteo, bg='black')
        self.marco_terminal.pack(side=TOP)
        self.marco_entradas=Frame(self.ventana_sorteo, bg='black')
        self.marco_entradas.pack(side=TOP)
        self.marco_juego=Frame(self.ventana_sorteo, bg='black')
        self.marco_juego.pack(side=BOTTOM)
        self.etiqueta_dia=Label(self.marco_dia, text=f'Digite los números y colores para el dia {hoy_es(self.dia_wk)}', font=('Arial', 20, 'bold'), fg='green', bg='black')
        self.etiqueta_dia.pack()
        self.etiqueta_terminal_num=Label(self.marco_terminal, text='num---------------', font=('Arial', 20, 'bold'), fg='green', bg='black')
        self.etiqueta_terminal_num.pack(side=LEFT)
        self.etiqueta_terminal_col=Label(self.marco_terminal, text='col---------------', font=('Arial', 20, 'bold'), fg='green', bg='black')
        self.etiqueta_terminal_col.pack(side=RIGHT)
        self.entrada_num=Entry(self.marco_entradas, font=('Arial', 15, 'bold'), fg='black', bg='white')
        self.entrada_num.pack(side=TOP)
        self.entrada_col=Entry(self.marco_entradas, font=('Arial', 15, 'bold'), fg='black', bg='white')
        self.entrada_col.pack(side=BOTTOM)
        self.juego=Button(self.marco_juego, text='Jugar', font=('Arial', 11, 'bold'), fg='green', bg='black', command=self.jugar)
        self.juego.pack()
    def jugar(self):
        global dia_adso
        global dia_cocina
        global dia_multimedia
        global numeros_adso
        global colores
        if str(self.entrada_num.get()).isdigit() and self.entrada_col.get().lower() in colores and len(str(self.entrada_num.get()))==4: 
            self.click+=1
            print(f'dia de adso: {dia_adso}; dia de cocina: {dia_cocina}; dia de multimedia: {dia_multimedia}, oportunidad: {self.again}')
            print(f'Entrada de numero: {self.entrada_num.get()}; Entrada de color: {self.entrada_col.get()}, ventana: {self.titulo_l}; cantidad: {self.cantidad}; click: {self.click}; Numero ganador: {self.numero_ganador}; Color ganador: {self.color_ganador}')
            if self.click<=((self.cantidad)+(self.again)):
                 self.etiqueta_terminal_num.configure(text=self.entrada_num.get())
                 self.etiqueta_terminal_col.configure(text=self.entrada_col.get())
                 self.numeros_usuario.append(str(self.entrada_num.get()))
                 self.colores_usuario.append(self.entrada_col.get().lower())
                 self.entrada_num.delete(0, END)
                 self.entrada_col.delete(0, END)
                 print(f'Numeros ingresados: {self.numeros_usuario}; Colores: {self.colores_usuario}')
                 if self.click==((self.cantidad)+(self.again)):
                     self.click=0
                     print(f'click: {self.click}')
                     if self.numero_ganador in self.numeros_usuario and self.color_ganador in self.colores_usuario:
                         print(f'Eres el feliz ganador de $2,000,000,000')
                         self.numeros_usuario.clear()
                         self.colores_usuario.clear()
                         print(f'numeros ingresados; {self.numeros_usuario}; Colores: { self.colores_usuario}')
                         self.victory=Toplevel()
                         self.victory.title(self.titulo_l)
                         print(os.getcwd())
                         self.felicitacion=PhotoImage(file='victory.png')
                         self.duck=Label(self.victory, text=f'Eres el feliz ganador de $2,000,000,000\nNumero ganador: {self.numero_ganador}; Color: {self.color_ganador}', font=('Arial', 20, 'bold'), fg='green', bg='black', image=self.felicitacion, compound='top')
                         self.duck.pack()
                         self.ventana_sorteo.withdraw()
                     elif self.numero_ganador[-3:] in [n[-3:] for n in self.numeros_usuario]:
                         print(f'Eres el feliz ganador de $500,000,000')
                         self.numeros_usuario.clear()
                         self.colores_usuario.clear()
                         print(f'numeros ingresados; {self.numeros_usuario}; Colores: { self.colores_usuario}')
                         self.secundario=Toplevel()
                         self.secundario.title(self.titulo_l)
                         self.etiqueta_secundario=Label(self.secundario, text=f'Eres el feliz ganador de $500,000,000\nNumero ganador: {self.numero_ganador}; Color: {self.color_ganador}', font=('Arial', 20, 'bold'), fg='green', bg='black')
                         self.etiqueta_secundario.pack()
                         self.ventana_sorteo.withdraw()
                     elif self.numero_ganador[-2:] in [n[-2:] for n in self.numeros_usuario]:
                         print(f'Perdiste, pero adquieres una boleta gratuita para un proximo sorteo')
                         self.numeros_usuario.clear()
                         self.colores_usuario.clear()
                         print(f'numeros ingresados; {self.numeros_usuario}; Colores: { self.colores_usuario}')
                         self.gratuito=Toplevel()
                         self.gratuito.title(self.titulo_l)
                         self.etiqueta_gratuito=Label(self.gratuito, text=f'Perdiste, pero adquieres una boleta gratuita para un proximo sorteo\nNumero ganador: {self.numero_ganador}; Color: {self.color_ganador}', font=('Arial', 20, 'bold'), fg='green', bg='black')
                         self.etiqueta_gratuito.pack()
                         self.ventana_sorteo.withdraw()
                         self.factura=Factura(self.titulo_l, 1)
                         if self.titulo_l=='Loteria ADSO':
                             dia_adso+=1
                         elif self.titulo_l=='Loteria Cocina':
                             dia_cocina+=1
                         else:
                             dia_multimedia+=1
                     else:
                         print(f'Perdiste')
                         self.numeros_usuario.clear()
                         self.colores_usuario.clear()
                         print(f'numeros ingresados; {self.numeros_usuario}; Colores: { self.colores_usuario}')
                         self.perdedor=Toplevel()
                         self.perdedor.title(self.titulo_l)
                         self.etiqueta_perdedor=Label(self.perdedor, text=f'Perdiste\nNumero ganador: {self.numero_ganador}; Color: {self.color_ganador}', font=('Arial', 20, 'bold'), fg='green', bg='black')
                         self.etiqueta_perdedor.pack()
                         self.ventana_sorteo.withdraw()
        else:
            messagebox.showerror(title='ERROR!', message='Solo puedes ingresar números de 4 cifras y los colores de la lista: gris, violeta, amarillo, rojo, azul, naranja, verde')

        
class Factura:
    def __init__(self, titulo, chance):
        self.x0=IntVar()
        self.x1=IntVar()
        self.x2=IntVar()
        self.x3=IntVar()
        self.x4=IntVar()
        self.x5=IntVar()
        self.titulo=titulo
        self.chance=chance
        self.ventana_pagos=Tk()
        self.ventana_pagos.title(self.titulo)
        self.boletas_marco=Frame(self.ventana_pagos, bg='black')
        self.marco_cantidad=Frame(self.ventana_pagos, bg='black')
        self.marco_cantidad.pack(side=BOTTOM)
        self.etiqueta_boletas=Label(self.ventana_pagos, bg='black', text=f'Seleccione la cantidad de boletas\n($5000 cada una)', font=('Arial', 20, 'bold'), fg='green')
        self.etiqueta_boletas.pack()
        self.cantidad_0=Checkbutton(self.marco_cantidad, text='0', font=('Arial', 15, 'bold'), variable= self.x0, onvalue=1, offvalue=0, command=lambda: self.x0.set(not self.x0.get()))
        self.cantidad_0.pack(side=LEFT)
        self.cantidad_1=Checkbutton(self.marco_cantidad, text='1', font=('Arial', 15, 'bold'), variable= self.x1, onvalue=1, offvalue=0, command=lambda: self.x1.set(not self.x1.get()))
        self.cantidad_1.pack(side=LEFT)
        self.cantidad_2=Checkbutton(self.marco_cantidad, text='2', font=('Arial', 15, 'bold'), variable= self.x2, onvalue=1, offvalue=0, command=lambda: self.x2.set(not self.x2.get()))
        self.cantidad_2.pack(side=LEFT)
        self.cantidad_3=Checkbutton(self.marco_cantidad, text='3', font=('Arial', 15, 'bold'), variable= self.x3, onvalue=1, offvalue=0, command=lambda: self.x3.set(not self.x3.get()))
        self.cantidad_3.pack(side=LEFT)
        self.cantidad_4=Checkbutton(self.marco_cantidad, text='4', font=('Arial', 15, 'bold'), variable= self.x4, onvalue=1, offvalue=0, command=lambda: self.x4.set(not self.x4.get()))
        self.cantidad_4.pack(side=LEFT)
        self.cantidad_5=Checkbutton(self.marco_cantidad, text='5', font=('Arial', 15, 'bold'), variable= self.x5, onvalue=1, offvalue=0, command=lambda: self.x5.set(not self.x5.get()))
        self.cantidad_5.pack(side=LEFT)
        if self.chance==1:
            self.cantidad_5.pack_forget()
        self.permiso=Button(self.ventana_pagos, text='Aceptar', command=self.seleccionar)
        self.permiso.pack(side=BOTTOM)
    def seleccionar(self):
            print(f'{self.titulo}, 0: {self.x0.get()}; 1: {self.x1.get()}; 2: {self.x2.get()}; 3: {self.x3.get()}; 4: {self.x4.get()}, 5: {self.x5.get()}')
            if sum([self.x0.get(), self.x1.get(), self.x2.get(), self.x3.get(), self.x4.get(), self.x5.get()])>1:
                messagebox.showerror(title='ERROR!', message='Solo puedes elegir una opción')
            elif self.x0.get()==1:
                if self.chance==0:
                    print('No podras jugar esta loteria')
                else:
                    comienzo=Sorteo(self.titulo, 0, self.chance)
                self.ventana_pagos.destroy()
            elif self.x1.get()==1:
                print('jugaras con 1 boleta')
                comienzo=Sorteo(self.titulo, 1, self.chance)
                self.ventana_pagos.destroy()
            elif self.x2.get()==1:
                print('jugaras con 2 boletas')
                comienzo=Sorteo(self.titulo, 2, self.chance)
                self.ventana_pagos.destroy()
            elif self.x3.get()==1:
                print('jugaras con 3 boletas')
                comienzo=Sorteo(self.titulo, 3, self.chance)
                self.ventana_pagos.destroy()
            elif self.x4.get()==1:
                print('jugaras con 4 boletas')
                comienzo=Sorteo(self.titulo, 4, self.chance)
                self.ventana_pagos.destroy()
            elif self.x5.get()==1:
                print('jugaras con 5 boletas')
                comienzo=Sorteo(self.titulo, 5, self.chance)
                self.ventana_pagos.destroy()
            else:
                messagebox.showerror(title='ERROR!', message='No has realizado la selección')
def enviar():
    global pagos_adso
    global pagos_cocina
    global pagos_multimedia
    global felicitacion
    if all([x.get(), y.get(), z.get()]):
        pagos_adso=Factura('Loteria ADSO', 0)
        pagos_cocina=Factura('Loteria Cocina', 0)
        pagos_multimedia=Factura('Loteria Multimedia', 0)
        loterias.destroy()
    elif all([x.get(), y.get()]):
        pagos_adso=Factura('Loteria ADSO', 0)
        pagos_cocina=Factura('Loteria Cocina', 0)
        loterias.destroy()
    elif all([x.get(), z.get()]):
        pagos_adso=Factura('Loteria ADSO', 0)
        pagos_multimedia=Factura('Loteria Multimedia', 0)
        loterias.destroy()
    elif all([y.get(), z.get()]):
        pagos_cocina=Factura('Loteria Cocina', 0)
        pagos_multimedia=Factura('Loteria Multimedia', 0)
        loterias.destroy()
    elif x.get()==1:
        pagos_adso=Factura('Loteria ADSO', 0)
        loterias.destroy()
    elif y.get()==1:
        pagos_cocina=Factura('Loteria Cocina', 0)
        loterias.destroy()
    elif z.get()==1:
        pagos_multimedia=Factura('Loteria Multimedia', 0)
        loterias.destroy()
    else:
        print('No has seleccionado ninguna loteria')
        messagebox.showerror(title='ERROR!', message='No has realizado la selección')

loterias=Tk()
marco_guia=Frame(loterias, bg='black')
marco_guia.pack(side=TOP)
marco_loterias=Frame(loterias, bg='black')
marco_loterias.pack(side=TOP)
marco_enviar=Frame(loterias, bg='black')
marco_enviar.pack(side=BOTTOM)
x=IntVar()
y=IntVar()
z=IntVar()
guia=Label(marco_guia, text='Elige alguno de los 3 sorteos para jugar', font=('Arial', 20, 'bold'), fg='green', bg='black')
guia.pack()
adso=Checkbutton(marco_loterias, text="ADSO", font=('Arial', 20, 'bold'), fg='green', variable=x, onvalue=1, offvalue=0)
adso.pack(side=LEFT)
cocina=Checkbutton(marco_loterias, text="Cocina", font=('Arial', 20, 'bold'), fg='green', variable=y, onvalue=1, offvalue=0)
cocina.pack(side=LEFT)
multimedia=Checkbutton(marco_loterias, text="Multimedia", font=('Arial', 20, 'bold'), fg='green', variable=z, onvalue=1, offvalue=0)
multimedia.pack(side=LEFT)
send=Button(marco_enviar, text='Enviar', font=('Arial', 10, 'bold'), command=enviar)
send.pack()
input()
loterias.mainloop()
input()

    
