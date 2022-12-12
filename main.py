from tkinter import *
import random
from difflib import SequenceMatcher
import sys
import os


class TypingTest(Tk):
    def __init__(self):
        super().__init__()
        self.title("Typing Speed Test")
        self.geometry("650x500")  # Define the geometry of the window
        self.configure(bg='#002800')
        self.widget()

    def get_sentence(self):
        lines = open('sentence.txt').read().splitlines()
        my_line = random.choice(lines)
        return my_line

    def widget(self):
        title = Label(width=25, text="Typing Speed Test", font=("Playfair", 25), fg="yellow", bg='#002800')
        title.grid(column=1, row=1, columnspan=5, sticky=W+E, padx=50)
        rule = Label(width=50, text="Click start, type sentence in white below and hit enter to get result.",
                     font=("Playfair", 11),
                     fg="yellow", bg='#002800')
        rule.grid(column=1, row=2, columnspan=5)
        self.my_line = self.get_sentence()
        self.sentence = Label(width=80, text=self.my_line, font=("Playfair", 10), fg='white', bg='#002800')
        self.sentence.grid(column=1, row=3, columnspan=4, pady=50)
        start_button = Button(text="Start Timer", width=10, command=self.start_timer)
        start_button.grid(column=1, row=5, columnspan=1, sticky=W, padx=40)
        self.user_typing = Entry(width=80, font=("Playfair", 10))
        self.user_typing.focus()
        self.user_typing.bind('<Return>', self.parser)
        self.user_typing.grid(column=1, row=6, columnspan=5, pady=30)

    def clear_text(self):
        self.user_typing.delete(0, 'end')

    def parser(self, event):
        self.accuracy()
        self.result()
        self.reset()

    def accuracy(self):
        self.user_type = self.user_typing.get()
        ratio = SequenceMatcher(None, self.my_line, self.user_type).ratio()
        accuracy = round(ratio * 100, 2)
        accuracy_label = Label(width=80, text=f"Result: \nAccuracy = {accuracy}%",
                               font=("Playfair", 10, 'bold'), fg='white', bg='#002800')
        accuracy_label.grid(column=1, row=7, columnspan=5)
        self.cancel()

    def result(self):
        self.user_time = str(self.timer).split('after#')[1]
        self.len_words = len(str(self.user_typing.get()).split(" "))
        wpm = round((int(self.len_words) / (int(self.user_time)/60)), 2)
        wpm_label = Label(width=80, text=f"Average {wpm} words/ minute", font=("Playfair", 10, 'bold'),
                          fg='white', bg='#002800')
        wpm_label.grid(column=1, row=8, columnspan=5)
        self.cancel()

    def reset(self):
        reset_button = Button(text="Restart", width=10, command=self.restart_program)
        reset_button.grid(column=1, row=9, columnspan=5, sticky=E, padx=40, pady=40)

    def start_timer(self):
        self.count_up(0)

    def count_up(self, count):
        self.count = count
        self.count_label = Label(width=25, text=f"{self.count}", font=("Playfair", 15), fg="yellow", bg='#002800')
        self.count_label.grid(column=2, row=5, columnspan=1, sticky=W)
        self.timer = self.after(1000, self.count_up, count + 1)

    def cancel(self):
        if self.timer is not None:
            self.after_cancel(self.timer)

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        os.execl(sys.executable, os.path.abspath(r"C:\Users\manda\portfolio\CODING\85_TKINTERTYPING\main.py"), *sys.argv)


App = TypingTest()
App.mainloop()
