import tkinter as tk

use_ai = True

def set_game_mode():
    select_game_mode()
    return use_ai

def select_game_mode():
    window = tk.Tk()
    window.title("Modo de Jogo")

    label = tk.Label(window, text="Escolha o tipo de jogo:")
    label.pack(pady=10)

    button_keybord = tk.Radiobutton(window, text="Teclado: WSAD vs setas", variable=use_ai, value=False)
    button_keybord.pack(pady=5)

    button_ai = tk.Radiobutton(window, text="IA: A* contra busca em profundidade limitada", variable=use_ai, value=True)
    button_ai.pack(pady=5)

    button_start = tk.Button(window, text="Iniciar", command=window.destroy)
    button_start.pack(pady=10)

    window.mainloop()

    return use_ai
