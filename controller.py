import tkinter as tk

class Controller:
    def __init__(self, game):
        self.game = game
        return self
    

    def process_input(self, e, add_txt):
        message = e.get()
        e.delete(0, tk.END)
        add_txt(message, "Protagoniste")
        protagonist = self.game.get_player()
        protagonist.advance_event(message)