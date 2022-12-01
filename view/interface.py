import tkinter as tk

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class InterfaceWindow:

    def __init__(self, controller_process):
        self.controller_process = controller_process
        self.txt = ""

        self.root = tk.Tk()
        width= self.root.winfo_screenwidth()
        height= self.root.winfo_screenheight()
        #setting tkinter window size
        self.root.geometry("%dx%d" % (width, height))


        self.lable1 = tk.Label(self.root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)

        self.txt = tk.Text(self.root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
        self.txt.grid(row=1, column=0, columnspan=10)

        self.scrollbar = tk.Scrollbar(self.txt)
        self.scrollbar.place(relheight=1, relx=0.974)

        self.e = tk.Entry(self.root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        self.e.grid(row=2, column=0)

        self.send = tk.Button(self.root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
        command=lambda: self.controller_process(self.e, self.add_text))
        self.send.grid(row=2, column=1)

        self.root.mainloop()


    def add_text(self, txt, speaker):
        self.txt.insert(tk.END, "\n%s : %s" % (speaker, txt))



def send_controller(e, add_txt):
    message = e.get()
    e.delete(0, tk.END)
    add_txt(message, "Protagoniste")





if __name__ == "__main__":
    window = InterfaceWindow(send_controller)
    