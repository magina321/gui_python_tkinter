#-*- coding: utf-8 -*-
"""
Created on Thu Sep 2020

@author: Magno Efren
https://www.youtube.com/c/MagnoEfren
"""

from tkinter import Tk, Canvas, Label, Button, Entry
import time

raiz = Tk()
raiz.title("PROCESO LLENADO DE UN TANQUE DE 25000 L")

raiz.resizable(0,0)
raiz.geometry("500x300")
raiz.config(bg="black")
  
tanque=Canvas(raiz,width=200,height=200,bg="black", highlightthickness=0)
tanque.place(x=50,y=50)

tanque.create_rectangle(140,20,10,180, fill="#E4E4E4")
tanque.create_oval(10,170,140,190, fill= "#CAC6BE")
tanque.create_rectangle(100,55,50,165, fill="white")
tanque.create_rectangle(100,165,50,165, fill="blue")       
tanque.create_oval(10,0,140,50, fill= "#CAC6BE")


nombre1= Label(raiz, text="25000 L",bg="black",fg="white", font="Helvetica 12 bold" )    
nombre1.place(x=190,y=65)    
        
nombre2= Label(raiz, text="0 L",bg="black",fg="white", font="Helvetica 12 bold" )    
nombre2.place(x=190,y= 210)


def llenado(): 
    num=165     
    for i in range(55,num):
                   
        tanque.create_rectangle(100,55,50,165, fill="white")
        tanque.create_rectangle(100,num,50,165, fill="blue")       
        tanque.update()

        time.sleep(0.04) 
        num = num - 1
        N = int((i-64)*250)
        
        flecha= Label(raiz, text="←",bg="black",fg="white", font="Helvetica 18 bold" )    
        flecha.place(x=190, y= num + 30)   
       
        indicadorN= Label(raiz, text= (f"Nivel actual = {N}"),bg="black",fg="white", font="Helvetica 10 bold" )   
        indicadorN.place(x=300, y= 70)

def vaciado():  

    for a in range(55,165):
            
        tanque.create_rectangle(100,55,50,165, fill="white")
        tanque.create_rectangle(100,a,50,165, fill="blue")     
        tanque.update()
        
        time.sleep(0.04)  
        l = int(25000 - (a-64)*250)
        
        flecha= Label(raiz, text="←",bg="black",fg="white", font="Helvetica 18 bold" )    
        flecha.place(x=190, y= a+30)
        
        indicadorN= Label(raiz, text= (f" Nivel actual = {l}"), bg="black",fg="white", font="Helvetica 10 bold" )
        indicadorN.place(x=300,y= 70)


def salir():
    raiz.destroy()
    raiz.quit()

boton = Button(raiz, bg ="magenta", text ="LLENAR ",font="Helvetica 10 bold", command =llenado, width = 15)
boton.place(x=300,y=120)

boton2 = Button(raiz, bg ="aqua", text ="  VACIAR  ",font="Helvetica 10 bold", command =vaciado,width =15)
boton2.place(x=300,y=170)

boton3 = Button(raiz, bg ="red", text ="  SALIR ",font="Helvetica 10 bold", command =salir,width =15)
boton3.place(x=300,y=220)    

raiz.mainloop()
