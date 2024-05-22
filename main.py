import winsound
import threading
import tkinter as tk

def stop_program():
    root.destroy()

def play_sound(sound):
    winsound.PlaySound(sound, winsound.SND_ALIAS)

root = tk.Tk()
bouton = tk.Button(root, text="N'appuie pas sur ce bouton", width=40)
bouton.pack(padx=10, pady=10)
compteClics = 0

# Jouer le 4ème effet sonore à chaque clic
threading.Thread(target=play_sound, args=("SystemAsterisk",)).start()

def quandClique(event):
    global compteClics
    compteClics += 1
    print("Score de compteClics:", compteClics)  # Commande de débogage
    if compteClics == 1:
        bouton.configure(text="T'es fou, arrête")
        print("Son joué : T'es fou, arrête")
        threading.Thread(target=play_sound, args=("SystemExclamation",)).start()
    elif compteClics == 2:
        bouton.configure(text="Arrête ou je te tue")
        print("Son joué : Arrête ou je te tue")
        threading.Thread(target=play_sound, args=("SystemHand",)).start()
    elif compteClics == 3:
        bouton.configure(text="Tu veux vraiment ?")
        print("Son joué : Tu veux vraiment ?")
        threading.Thread(target=play_sound, args=("SystemQuestion",)).start()
    elif compteClics == 4:
        bouton.configure(text="Ok j'ai compris")
        print("Son joué : Ok j'ai compris")
        threading.Thread(target=play_sound, args=("SystemAsterisk",)).start()
        stop_program()  # Arrêter le programme après le quatrième clic

bouton.bind("<ButtonRelease-1>", quandClique)
root.mainloop()

