import tkinter as tk

#GUIを表示するクラス
class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.master.geometry("600x400")
        self.master.title("TEST GUI")

        self.create_widgets()

    def create_widgets(self):
        #テキストボックスの作成
        self.textBox = tk.Entry(self.master, width="25")
        self.textBox.place(x=220, y=80)

        self.btnMessageDisp = tk.Button(self.master, text="メッセージ表示", width="20", command=self.clickMessage)
        self.btnMessageDisp.place(x=220, y=160)

        self.lblMessage = tk.Label(self.master, text="")
        self.lblMessage.place(x=220, y=240)

    def clickMessage(self):
        self.lblMessage["text"] = self.textBox.get()
