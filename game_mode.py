import tkinter as tk

use_ai = False

def set_game_mode():
    select_game_mode()
    return use_ai

def select_game_mode():
    window = tk.Tk()
    window.title("Modo de Jogo")

    label = tk.Label(window, text="Bem vindo ao Labirinto:")
    label.pack(pady=10)

    button_ai = tk.Label(window, text="    IA: A* contra busca em profundidade limitada    ")
    button_ai.pack(pady=5)

    button_start = tk.Button(window, text="Iniciar", command=window.destroy)
    button_start.pack(pady=10)

    window.mainloop()

    return use_ai
