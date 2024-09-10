import tkinter as tk

class ButtonManager:
    def update_button(self, button, symbol):
        button.config(text=symbol)

    def disable_button(self, button):
        button.config(state=tk.DISABLED)

    def enable_button(self, button):
            button.config(state=tk.NORMAL)

    def disable_all_buttons(self, buttons):
        for button in buttons.values():
            button.config(state=tk.DISABLED)
    
    def reset_buttons(self, buttons):
        for button in buttons.values():
            button.config(state=tk.NORMAL)
            button.config(text='')
