import tkinter as tk
from tkinter import messagebox

# Taxas fixas
TAXA_DOLAR = 5.00
TAXA_EURO = 6.00

def converter():
    try:
        valor_reais = float(entrada_valor.get())
        valor_em_dolar = valor_reais / TAXA_DOLAR
        valor_em_euro = valor_reais / TAXA_EURO
        resultado.set(f"USD: ${valor_em_dolar:.2f} | EUR: €{valor_em_euro:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido!")

# Janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")
janela.geometry("300x200")

# Widgets
tk.Label(janela, text="Conversor de Moedas", font=("Arial", 16)).pack(pady=10)

entrada_valor = tk.Entry(janela, font=("Arial", 14), justify="center")
entrada_valor.pack(pady=5)

tk.Button(janela, text="Converter", command=converter, font=("Arial", 12)).pack(pady=10)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, font=("Arial", 14)).pack(pady=5)

janela.mainloop()
