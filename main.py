from tkinter import Tk, Button, Entry

def agregar_valor(valor):
    pantalla.insert("end", valor)

def operar(operacion):
    global operacion_global, primer_numero
    primer_numero = float(pantalla.get())
    operacion_global = operacion
    pantalla.delete(0, "end")

def resultado():
    segundo_numero = float(pantalla.get())
    pantalla.delete(0, "end")
    
    if operacion_global == "+":
        pantalla.insert("end", primer_numero + segundo_numero)
    elif operacion_global == "-":
        pantalla.insert("end", primer_numero - segundo_numero)
    elif operacion_global == "*":
        pantalla.insert("end", primer_numero * segundo_numero)
    elif operacion_global == "/":
        if segundo_numero == 0:
            pantalla.insert("end", "Error")
        else:
            pantalla.insert("end", primer_numero / segundo_numero)

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0, 0)
root.geometry("350x300")  # Ajusta el tamaño de la ventana

# Configuración pantalla de salida 
pantalla = Entry(root, width=33, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky="nsew")

# Configuración botones
Button(root, text="1", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(1)).grid(row=1, column=0, sticky="nsew",padx=1,pady=1)
Button(root, text="2", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(2)).grid(row=1, column=1, sticky="nsew",padx=1,pady=1)
Button(root, text="3", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(3)).grid(row=1, column=2, sticky="nsew",padx=1,pady=1)
Button(root, text="+", bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operar("+")).grid(row=1, column=3, sticky="nsew",padx=1,pady=1)

Button(root, text="4", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(4)).grid(row=2, column=0, sticky="nsew",padx=1,pady=1)
Button(root, text="5", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(5)).grid(row=2, column=1, sticky="nsew",padx=1,pady=1)
Button(root, text="6", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(6)).grid(row=2, column=2, sticky="nsew",padx=1,pady=1)
Button(root, text="-", bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operar("-")).grid(row=2, column=3, sticky="nsew",padx=1,pady=1)

Button(root, text="7", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(7)).grid(row=3, column=0, sticky="nsew",padx=1,pady=1)
Button(root, text="8", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(8)).grid(row=3, column=1, sticky="nsew",padx=1,pady=1)
Button(root, text="9", bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: agregar_valor(9)).grid(row=3, column=2, sticky="nsew",padx=1,pady=1)
Button(root, text="*", bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operar("*")).grid(row=3, column=3, sticky="nsew",padx=1,pady=1)

Button(root, text="=", bg="red", fg="white", borderwidth=0, cursor="hand2", command=resultado).grid(row=4, column=0, columnspan=2, sticky="nsew",padx=1,pady=1)
Button(root, text=".", bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=lambda: agregar_valor(".")).grid(row=4, column=2, sticky="nsew",padx=1,pady=1)
Button(root, text="/", bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=lambda: operar("/")).grid(row=4, column=3, sticky="nsew",padx=1,pady=1)

# Configuración para expandir columnas y filas uniformemente
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)


root.mainloop()
