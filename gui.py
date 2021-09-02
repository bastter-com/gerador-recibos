import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from doc_maker import create_doc


root = tk.Tk()
root.geometry("300x250")
root.resizable(False, False)
root.title("Gerador de recibos")

name = tk.StringVar()
value = tk.StringVar()
service = tk.StringVar()

def button_clicked():
    name_input = name.get()
    value_input = value.get()
    service_input = service.get()
    create_doc(name_input, value_input, service_input)
    msg = f"Recibo foi criado com sucesso! Dados enviados: Nome: {name_input}/ Valor: {value_input}/ Serviço: {service_input}"
    showinfo(
        title="Sucesso",
        message=msg
    )


frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Nome
name_label = ttk.Label(frame, text="Nome:")
name_label.pack(fill="x", expand=True)

name_entry = ttk.Entry(frame, textvariable=name)
name_entry.pack(fill="x", expand=True)

# Valor
value_label = ttk.Label(frame, text="Valor:")
value_label.pack(fill="x", expand=True)

value_entry = ttk.Entry(frame, textvariable=value)
value_entry.pack(fill="x", expand=True)

# Serviço
service_label = ttk.Label(frame, text="Serviço:")
service_label.pack(fill="x", expand=True)

service_entry = ttk.Entry(frame, textvariable=service)
service_entry.pack(fill="x", expand=True)

# Botão
submit_btn = ttk.Button(frame, text="Criar recibo", command=button_clicked)
submit_btn.pack(fill='x', expand=True, pady=10)

root.mainloop()
