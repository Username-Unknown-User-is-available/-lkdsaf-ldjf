import socket
from threading import Thread
from tkinter import *



# nickname=input("Enter name ")

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipadress="127.0.0.1"
port=8000

client.connect((ipadress, port))
print("connected with server. :)")

class GUI:
    def __init__(self):

        self.window=Tk()
        self.window.withdraw()

        self.login=Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)

        self.lable=Label(self.login, text="Please login to continue", justify=CENTER, font="Helvetica 14 bold")
        self.lable.place(relheight=0.15, relx=0.2, rely=0.07)

        self.lablename=Label(self.login, text="Name", font="Helvetica 12 bold")
        self.lablename.place(relheight=0.2, relx=0.1, rely=0.2)

        self.entry=Entry(self.login, font="Helvetica 14")
        self.entry.place(relwidth=0.4, relheight=0.12, relx=0.35, rely=0.2)
        self.entry.focus()

        self.button=Button(self.login, text="contine", font="Helvetica 12 bold", command=lambda:self.goahead(self.entry.get()))
        self.button.place(relx=0.4, rely=0.55)

        self.window.mainloop()

    def goahead(self,name):
        self.login.destroy()
        self.name=name
        rcv=Thread(target=self.recieve)
        rcv.start()

        

    def recieve(self):
        while True:
            try:
                message=client.recv(2048).decode("utf-8")
                if message=="NICKNAME":
                    client.send(self.name.encode("utf-8"))
                else:
                    pass
            except:
                print("Error 404")
                client.close()
                break

g=GUI()

# def write():
#     while True:
#         message="{}:{}".format(nickname, input(""))
#         client.send(message.encode("utf-8"))

# recievethread=Thread(target=recieve)
# recievethread.start()

# writethread=Thread(target=write)
# writethread.start()