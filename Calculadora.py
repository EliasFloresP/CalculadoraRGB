import tkinter as tk
import tkinter.font as tkFont
import math

ventana = tk.Tk()

color = mycolor = '#%02x%02x%02x' % (20, 40, 51)
ventana.title("Calculadora")
ventana.geometry("390x500")
ventana.resizable(width=False, height=False)
ventana.configure(bg=color)

#Frontend
a = 35
letra = tkFont.Font(family="Lucida Grande", size=35)
letra2 = tkFont.Font(family="Lucida Grande", size=15)
barra = tk.Label(ventana,text="",anchor="se",font=letra,bg="white",width=13)
barra.place(x=20,y=50)
barra2 =tk.Label(ventana,text="",anchor="se",fg="white",font=letra2,bg=color,width=32)
barra2.place(x=20,y=17)

#Botones limpiadores
colora= '#%02x%02x%02x' % (52, 152, 219)
colorx= '#%02x%02x%02x' % (26, 82, 118)
botonC = tk.Button(ventana,text="C",width=18,heigh=3,fg="white",bg=colora, command= lambda : eliminar())
botonC.place(x=20,y=100+a)
botonCE = tk.Button(ventana,text="CE",width=18,heigh=3,fg="white",bg=colora,command= lambda :eliminar_parcial())
botonCE.place(x=160,y=100+a)
botonBack = tk.Button(ventana,text="<--",width=9,fg="white",heigh=3,bg=colora,command = lambda : retroceder())
botonBack.place(x=300,y=100+a)

#Botones de operaciones
colorb = '#%02x%02x%02x' % (33, 97, 140)
#Horizontal
botonsqr = tk.Button(ventana,text="²√",width=11,heigh=3,bg=colorb,fg="white",command=lambda:operacion(5))
botonsqr.place(x=20,y=160+a)
botonpow = tk.Button(ventana,text="x²",width=11,heigh=3,bg=colorb,fg="white",command=lambda:operacion(6))
botonpow.place(x=115,y=160+a)
botonper = tk.Button(ventana,text="%",width=11,heigh=3,bg=colorb,fg="white",command=lambda:operacion(7))
botonper.place(x=210,y=160+a)
#Vertical
botonadd = tk.Button(ventana,text="+",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(1))
botonadd.place(x=300,y=160+a)
botonsub = tk.Button(ventana,text="-",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(2))
botonsub.place(x=300,y=220+a)
botonmul = tk.Button(ventana,text="x",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(3))
botonmul.place(x=300,y=280+a)
botondiv = tk.Button(ventana,text="÷",width=9,heigh=3,bg=colorb,fg="white",command=lambda:operacion(4))
botondiv.place(x=300,y=340+a)
botoneq = tk.Button(ventana,text="=",width=9,heigh=3,bg=colorb,fg="white",command=lambda:igual())
botoneq.place(x=300,y=400+a)

#Botones numerales
#1
boton7 = tk.Button(ventana,text="7",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(7))
boton7.place(x=20,y=220+a)
boton8 = tk.Button(ventana,text="8",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(8))
boton8.place(x=115,y=220+a)
boton9 = tk.Button(ventana,text="9",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(9))
boton9.place(x=210,y=220+a)
#2
boton4 = tk.Button(ventana,text="4",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(4))
boton4.place(x=20,y=280+a)
boton5 = tk.Button(ventana,text="5",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(5))
boton5.place(x=115,y=280+a)
boton6 = tk.Button(ventana,text="6",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(6))
boton6.place(x=210,y=280+a)
#3
boton1 = tk.Button(ventana,text="1",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(1))
boton1.place(x=20,y=340+a)
boton2 = tk.Button(ventana,text="2",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(2))
boton2.place(x=115,y=340+a)
boton3 = tk.Button(ventana,text="3",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(3))
boton3.place(x=210,y=340+a)
#4
boton0 = tk.Button(ventana,text="0",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(0))
boton0.place(x=20,y=400+a)
botonpoint = tk.Button(ventana,text=".",width=11,heigh=3,bg=colora,fg="white",command=lambda: boton(10))
botonpoint.place(x=115,y=400+a)
botonconfi = tk.Button(ventana,text="RGB",width=11,heigh=3,bg=colora,fg="white",command=lambda: pyScale2())
botonconfi.place(x=210,y=400+a)

#Backend
cadena2 = 0
contador = 0
auxiliar = 1
cadena = []
resultado = "0+"
i =0
punto = 0
#Botones
def boton(num):
    global contador
    global cadena2
    global cadena
    global auxiliar
    global resultado
    global i
    global punto
    
    #Si pongo un . no puedo poner un  +  ni un  = 
    if num == 10 and punto == 1 :
        return
        
    if auxiliar == 4 and punto == 1:
        auxiliar = 0

    if auxiliar  == 2:
       resultado = "" 
       auxiliar = 1

    if auxiliar==1 or auxiliar ==3:
        cadena = []
        cadena2 = ""
        auxiliar = 0
    

    
    if i == 1:
        cadena.append("-")
        i=0
    
    if num == 10 and punto == 0 :
        cadena.append(".")
        cadena2 = "".join(map(str,cadena))
        barra["text"]=cadena2
        punto = 1
        auxiliar = 4
        return


    if (contador < 13):
        cadena.append(num)
        cadena2 = "".join(map(str,cadena))
        try:
            cadena2 = str(int(cadena2))
        except:
            cadena2=str(eval(cadena2))
        barra["text"]=cadena2
        contador = contador +1

    
def operacion(nume):
    global cadena2
    global resultado 
    global auxiliar
    global i
    global contador
    global punto

    #Para que no marque dos signos al mismo tiempo
    if punto == 1 and auxiliar == 1:
        auxiliar = 1


    if (auxiliar == 1 or auxiliar==3) and nume==2:
        i=1
        return 

    if auxiliar==1 or auxiliar ==3 or auxiliar == 4:
        return

    auxiliar =  1
    punto = 0
    contador = 0

    resultado = resultado + cadena2

    try:
        barra["text"] = round(eval(resultado),11)
        resultado = str(eval(resultado))
        barra2["text"] = resultado
    except:
        barra["text"] = "No divida para 0"
        resultado = "0+0"

    if nume == 1:
        resultado = resultado + "+"

    if nume == 2:
        resultado = resultado +"-"

    if nume == 3:
        resultado = str(eval(resultado))
        resultado = resultado +"*"

    if nume == 4:
        resultado = str(eval(resultado))
        resultado = resultado +"/"
    if nume == 5:
        resultado = eval(resultado)
        try:
            resultado = str(round(math.sqrt((resultado)),11))
        except:
            barra["text"]="Raiz negativa"
            resultado = "0+0"
            cadena2=""
            auxiliar = 0
            return
        cadena2 = ""
        auxiliar = 0
        igual()
    if nume == 6:
        resultado = eval(resultado)
        resultado = str((resultado**2))
        cadena2 = ""
        auxiliar = 0
        igual()

    if nume == 7:
        resultado = str(eval(resultado))
        resultado = resultado +"%"


    barra2["text"] = resultado


def igual():
    global resultado
    global auxiliar
    global cadena2
    global contador
    global colora
    global color
    global colorb
    global punto

    if auxiliar == 1 or auxiliar == 3 or auxiliar == 4:
        return 

    resultado = resultado + cadena2 

    try:
        barra["text"] = round(eval(resultado),11)
        barra2["text"] = resultado

    except:
        barra["text"] = "No divida para 0"
        resultado = "0+0"

    if round(eval(resultado),11)== 0.00031818182:
        l = [230, 126, 34]
        m = [244, 208, 63]
        #cambia_color(l[0],l[1],l[2],m[0],m[1],m[2])
        personalizacion(1)


    auxiliar = 2
    cadena2=""
    punto = 0
    resultado = str(eval(resultado))
    contador = 0

def eliminar():
    global cadena
    global cadena2
    global resultado
    global auxiliar
    global contador
    global punto

    cadena = []
    cadena2 = ""
    resultado ="0+"
    auxiliar = 1
    contador = 0
    barra["text"]="0"
    barra2["text"]= ""
    punto = 0   



def eliminar_parcial():

    global auxiliar
    global contador
    global punto


    if auxiliar == 2:
        eliminar()

    contador = 0
    auxiliar = 3
    punto=0
    barra["text"]="0"

def retroceder():
    global auxiliar
    global cadena2
    global contador
    global cadena
    global punto

    if auxiliar == 2:
        eliminar()
    else:
        if contador > 0:
            contador = contador -1
        if len(cadena) != 0:
            dato = cadena.pop()

            if dato == ".":
                punto = 0

            cadena2 = "".join(map(str,cadena))
            barra["text"]=cadena2

#RGB
def pyScale2():
    root = tk.Tk()
    root.geometry("350x410")
    color_fon = '#%02x%02x%02x' % (67, 30, 250)
    root.configure(bg=color_fon)
    root.resizable(width=False, height=False)

    
    def ver(i,j,k):
        color_c='#%02x%02x%02x' % (i, j, k)
        caja_rgb2=tk.Label(root,text="",bg=color_c,width=25,height=5)
        caja_rgb2.place(x=90,y=210)

    def click(self):
        i=0
        j=0
        k=0
        try:
            s1.set(int(rojo_F.get()))
            i=int(rojo_F.get())
            if i > 250 : i = 250
            if i < 0 :  i = 0
        except:
            s1.set(0)
            i=0
        try:
            s2.set(int(verde_F.get()))
            j=int(verde_F.get())
            if j > 250 : j = 250
            if j < 0 :  j = 0
        except:
            s2.set(0)
            j=0
        try:
            s3.set(int(azul_F.get()))
            k=int(azul_F.get())
            if k > 250 : k = 250
            if k < 0 :  k = 0
        except:
            s3.set(0)
            k=0
        ver(i,j,k)


    def formularios(auxiliar,num):
        if auxiliar == 1:
            rojo_F.delete(0,tk.END)
            rojo_F.insert(0,num)
        if auxiliar == 2:
            verde_F.delete(0,tk.END)
            verde_F.insert(0,num)
        if auxiliar == 3:
            azul_F.delete(0,tk.END)
            azul_F.insert(0,num)
        click("Hola")
    
    def recoger(labe):
        lista = [s1.get(),s2.get(),s3.get()]
        labe["text"]=lista

    def enviar_datos(tipo):
        listo = ""
        color_ui= 1
        color_ue= 1
        archivo = open("Colores.txt","w")
        if tipo == 0:
            listo = (fondo["text"]+" "+color_bo["text"])
            archivo_lis = listo
            listo = listo.split(' ')
            if((int(listo[0])+int(listo[1])+int(listo[2]))>=250):
                color_ue = 0
            if((int(listo[3])+int(listo[4])+int(listo[5]))>=250):
                color_ui = 0
            archivo.write(archivo_lis+" "+str(color_ue)+" "+str(color_ui))
            cambia_color(int(listo[0]),int(listo[1]),int(listo[2]),int(listo[3]),int(listo[4]),int(listo[5]),color_ue,color_ui)
        if tipo == 1:
            cambia_color(230, 126, 34,244, 208, 63,0,0)
            archivo.write("230 126 34 244 208 63 0 0")
        if tipo == 2:
            cambia_color(33, 97, 140,52, 152, 219,1,1)
            archivo.write("33 97 140 52 152 219 63 1 1")
        if tipo == 3:
            cambia_color(17, 122, 101,69, 179, 157,0,0)
            archivo.write("17 122 101 69 179 157 63 0 0")
        if tipo == 4:
            archivo.write("3 2 1 0 2 3 12 1 1")
            personalizacion()
        if tipo == 5:
            archivo.write("6 2 1 0 2 6 18 1 1")
            personalizacion(1)

        archivo.close()
    
    color_back = '#%02x%02x%02x' % (71, 76, 250)
    letra2 = tkFont.Font(family="Lucida Grande", size=15)
    tema = tk.Label(root,text="Colores de la Calculadora (RGB)",fg="white",bg=color_fon,font=letra2,width=32)
    tema.place(x=0,y=10)

    caja_rbg=tk.Label(root,text="",bg=color_back,width=46,height=17)
    caja_rbg.place(x=10,y=45)

    ver(250,250,250)
    #Rojo
    rojo = tk.Label(root,text="R:",font=letra2,fg="white",bg=color_back,width=2)
    rojo.place(x=10,y=55)
    rojo_F = tk.Entry(root,text="",bg="white",width=5,font=letra2)
    rojo_F.place(x=50,y=55)
    s1 = tk.Scale(root, from_=0, to=250, tickinterval=0, bg="red",fg="white", orient=tk.HORIZONTAL, length=200,command=lambda x: formularios(1,s1.get()))
    s1.place(x=120,y=50)

    #Verde
    verde = tk.Label(root,text="G:",font=letra2,fg="white",bg=color_back,width=2)
    verde.place(x=10,y=105)
    verde_F = tk.Entry(root,text="",bg="white",width=5,font=letra2)
    verde_F.place(x=50,y=105)
    s2 = tk.Scale(root, from_=0, to=250, tickinterval=0, bg="green",fg="white", orient=tk.HORIZONTAL, length=200,command=lambda x: formularios(2,s2.get()))
    s2.place(x=120,y=100)

    #Azul
    azul = tk.Label(root,text="B:",font=letra2,fg="white",bg=color_back,width=2)
    azul.place(x=10,y=155)
    azul_F = tk.Entry(root,text="",bg="white",width=5,font=letra2)
    azul_F.place(x=50,y=155)
    s3 = tk.Scale(root, from_=0, to=250, tickinterval=0, bg="blue",fg="white", orient=tk.HORIZONTAL, length=200,command=lambda x: formularios(3,s3.get()))
    s3.place(x=120,y=150)

    #N1 Guardar color de backgroung
    n1 = tk.Button(root,text="Color fondo",width=10,fg="white",heigh=1,bg=color_back ,command= lambda : recoger(fondo))
    n1.place(x=10,y=310)
    fondo = tk.Label(root,text="0 0 0",bg="white",width=9,height=1)
    fondo.place(x=95,y=312)

    #N2 Guardar Colores de los Botones
    n2 = tk.Button(root,text="Color Botones",width=10,fg="white",heigh=1,bg=color_back,command= lambda : recoger(color_bo))
    n2.place(x=180,y=310)
    color_bo = tk.Label(root,text="0 0 0",bg="white",width=9,height=1)
    color_bo.place(x=265,y=312)

    
    #Calido
    calido = tk.Button(root,text="Calido",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(1))
    calido.place(x=10,y=345)
    #Frio
    frio = tk.Button(root,text="Frio",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(2))
    frio.place(x=90,y=345)
    #Bosque
    bosque = tk.Button(root,text="Bosque",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(3))
    bosque.place(x=10,y=375)
    #Rainbow
    rainbow = tk.Button(root,text="Rainbow",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(4))
    rainbow.place(x=90,y=375)
    Tri = tk.Button(root,text="Tricolor",width=9,fg="white",heigh=1,bg=color_back,command= lambda: enviar_datos(5))
    Tri.place(x=170,y=375)
    #enviar
    enviar = tk.Button(root,text="Enviar",width=9,fg="white",heigh=2,bg=color_back,command= lambda: enviar_datos(0))
    enviar.place(x=268,y=360)

    
    #rojo_F.bind('<FocusIn>',click)
    rojo_F.bind("<KeyRelease>",click)
    verde_F.bind("<KeyRelease>",click)
    azul_F.bind("<KeyRelease>",click)
    
    
    tk.mainloop()






#Fin RGB
def cambia_color(a,b,c,d,e,f,c_letras,c_letras2):
    color_e =  '#%02x%02x%02x' % (a, b, c)
    color_i =  '#%02x%02x%02x' % (d, e, f)

    if set([3,2,1,0,2,3,12,1,1]) == set([a,b,c,d,e,f,c_letras,c_letras2]):
       personalizacion(0)
       return 
    if set([6,2,1,0,2,6,18,1,1]) == set([a,b,c,d,e,f,c_letras,c_letras2]):
       personalizacion(1)
       return  

    ventana.configure(bg=color_e)
    ventana.title("Calculadora _Premium_")
    if c_letras == 1:
        c_letras = "white"
    else:
        c_letras = "black"

    if c_letras2 == 1:
        c_letras2 = "white"
    else:
        c_letras2 = "black"
    
    barra2["bg"]=color_e
    barra2["fg"]=c_letras

    #Color_i
    botonC["bg"]=color_i
    botonCE["bg"]=color_i
    botonBack["bg"]=color_i
    boton9["bg"]=color_i
    boton8["bg"]=color_i
    boton7["bg"]=color_i
    boton6["bg"]=color_i
    boton5["bg"]=color_i
    boton4["bg"]=color_i
    boton3["bg"]=color_i
    boton2["bg"]=color_i
    boton1["bg"]=color_i
    boton0["bg"]=color_i
    botonconfi["bg"]=color_i
    botonpoint["bg"]=color_i

    #Color_e
    botonsqr["bg"]=color_e
    botonpow["bg"]=color_e
    botonper["bg"]=color_e
    botonadd["bg"]=color_e
    botondiv["bg"]=color_e
    botonmul["bg"]=color_e
    botonsub["bg"]=color_e
    botoneq["bg"]=color_e


    #Letras
        #Color_i
    botonC["fg"]=c_letras2
    botonCE["fg"]=c_letras2
    botonBack["fg"]=c_letras2
    boton9["fg"]=c_letras2
    boton8["fg"]=c_letras2
    boton7["fg"]=c_letras2
    boton6["fg"]=c_letras2
    boton5["fg"]=c_letras2
    boton4["fg"]=c_letras2
    boton3["fg"]=c_letras2
    boton2["fg"]=c_letras2
    boton1["fg"]=c_letras2
    boton0["fg"]=c_letras2
    botonconfi["fg"]=c_letras2
    botonpoint["fg"]=c_letras2

    #Color_e
    botonsqr["fg"]=c_letras
    botonpow["fg"]=c_letras
    botonper["fg"]=c_letras
    botonadd["fg"]=c_letras
    botondiv["fg"]=c_letras
    botonmul["fg"]=c_letras
    botonsub["fg"]=c_letras
    botoneq["fg"]=c_letras

def personalizacion(pride=0):
    ventana.configure(bg="black")
    barra2["bg"]="black"
    barra2["fg"]="white"

    color_fila1 = "red"
    color_fila2 = "orange"
    color_fila3 = "yellow"
    color_fila4 = "green"
    color_fila5 = "cyan"
    color_fila6 = "purple"


    if pride == 1:
        color_fila1 = "yellow"
        color_fila2 = "yellow"
        color_fila3 = "blue"
        color_fila4 = "blue"
        color_fila5 = "red"
        color_fila6 = "red"

    #Primera Fila
    botonC["bg"]=color_fila1
    botonCE["bg"]=color_fila1
    botonBack["bg"]=color_fila1
    #FG
    if pride == 1:
        botonC["fg"]="black"
        botonCE["fg"]="black"
        botonBack["fg"]="black"
    #segunda Fila
    botonsqr["bg"]=color_fila2
    botonpow["bg"]=color_fila2
    botonper["bg"]=color_fila2
    botonadd["bg"]=color_fila2
    #FG
    botonsqr["fg"]="black"
    botonpow["fg"]="black"
    botonper["fg"]="black"   
    botonadd["fg"]="black"
    #Tercera Fila
    boton9["bg"]=color_fila3
    boton8["bg"]=color_fila3
    boton7["bg"]=color_fila3
    botonsub["bg"]=color_fila3
    #FG
    if pride == 0:
        boton9["fg"]="black"
        boton8["fg"]="black"
        boton7["fg"]="black"   
        botonsub["fg"]="black"

    #Cuarta fila
    boton6["bg"]=color_fila4
    boton5["bg"]=color_fila4
    boton4["bg"]=color_fila4
    botonmul["bg"]=color_fila4
    #quinta Fila
    boton3["bg"]=color_fila5
    boton2["bg"]=color_fila5
    boton1["bg"]=color_fila5
    botondiv["bg"]=color_fila5
    #FG
    if pride == 0:
        boton3["fg"]="black"
        boton2["fg"]="black"
        boton1["fg"]="black"   
        botondiv["fg"]="black"
    #Sexta Fila
    boton0["bg"]=color_fila6
    botonconfi["bg"]=color_fila6
    botonpoint["bg"]=color_fila6
    botoneq["bg"]=color_fila6
    if pride == 1:
        boton3["fg"]="white"
        boton2["fg"]="white"
        boton1["fg"]="white" 
        botondiv["fg"]="white"
        boton9["fg"]="white"
        boton8["fg"]="white"
        boton7["fg"]="white"   
        botonsub["fg"]="white"
        boton4["fg"]="white"
        boton5["fg"]="white"
        boton6["fg"]="white" 
        botonmul["fg"]="white"
        boton0["fg"]="white"
        botonpoint["fg"]="white"
        botonconfi["fg"]="white"   
        botoneq["fg"]="white"

'''archivo2 = open("Colores.txt","r")
tamano=archivo2.readlines()
tamano = "".join(map(str,tamano))
tamano = tamano.split(' ')'''
try:
    archivo2 = open("Colores.txt","r")
    tamano=archivo2.readlines()
    tamano = "".join(map(str,tamano))
    tamano = tamano.split(' ')
    cambia_color(int(tamano[0]),int(tamano[1]),int(tamano[2]),int(tamano[3]),int(tamano[4]),int(tamano[5]),int(tamano[6]),int(tamano[7]))
    archivo2.close()
except:
    archivo2 = open("Colores.txt","w")
    cambia_color(33, 97, 140,52, 152, 219,1,1)
    archivo2.write("33 97 140 52 152 219 63 1 1")
    archivo2.close()


ventana.mainloop()