import tkinter as tk
import os

class CalculatorGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x390")
        self.title("Calculator")
        self.resizable(False, False)
        self.screen()
        self.buttons()

    def calculate(self,event=None):
        expr=self.screen_value.get()
        # replacing calculator symbols with computer mathematical symbols
        expr=expr.replace("×","*")
        expr=expr.replace("÷","/")
        try:
            value=eval(expr)
            self.screen_value.set(str(value))
        except ZeroDivisionError:
            self.screen_value.set("CANNOT DIVIDE BY ZERO")
        except Exception:
            self.screen_value.set("ERROR")

    def click(self,event):
        text=event.widget.cget("text")
        
        self.operators1="+-×÷"
        self.operators2="+×÷"
        
        current=self.screen_value.get()
        
        if text in self.operators1:
            # prevent typing consecutive operators
            if current and current[-1] in self.operators1:
                return
            
        if text in self.operators2:
            # prevent typing operators (except "-") if screen is empty
            if not current:
                return
            
        if text==".":
            for operator in "+-*/":
                current=current.split(operator)[-1]
            if "." in current:
                return
            
        if text=="=":
            self.calculate()
        elif text=="AC":
            # clear screen
            self.screen_value.set("")
        elif text=="⌫":
            # deletes the last character
            self.screen_value.set(self.screen_value.get()[:-1])
        else:
            current=self.screen_value.get()
            if current in ("ERROR", "CANNOT DIVIDE BY ZERO"):
                # if error is faced, sets the screen value according to the pressed key value
                if text.isdigit() or text==".":
                    self.screen_value.set(text)
                else:
                    return
            else:
                # adds characters to the screen
                self.screen_value.set(current+text)
    
    def key_input(self,event):
        
        permitted_symbol="*/+-"
        symbol=event.char
        
        current=self.screen_value.get()

        if symbol.isdigit():
            self.screen_value.set(current+symbol)

        elif symbol in permitted_symbol:
            # replacing computer mathematical symbols with calculator symbols
            symbol = symbol.replace("*", "×")
            symbol = symbol.replace("/", "÷")

            self.keyboard_operators1 = "+-*/"
            self.keyboard_operators2 = "+*/"
            
            if symbol in self.keyboard_operators2:
                if not current:
                    return
            if current and current[-1] in self.keyboard_operators1:
                return
            
            self.screen_value.set(current+symbol)
        
        elif symbol==".":
            # split the string to isolate the current value being typed (last one in the string)
            for operator in "+-*/":
                current=current.split(operator)[-1]
            if "." in current:
                return
            self.screen_value.set(self.screen_value.get()+symbol)
        else:
            return
        
    def backspace(self,event):

        self.screen_value.set(self.screen_value.get()[:-1])
    
    def delete(self,event):
        # clear screen with delete key
        self.screen_value.set("")

    def screen(self):

        # icon
        icon_path=os.path.join(os.path.dirname(__file__),"assets","calculator_icon.ico")
        self.wm_iconbitmap(icon_path)
        
        # display screen
        self.screen_value=tk.StringVar()
        self.screen_value.set("")
        self.screen_entry=tk.Entry(self,textvariable=self.screen_value,font="Digital-7 20",justify="right",state="readonly")
        self.grid_columnconfigure(0, weight=1)
        self.screen_entry.grid(row=0,column=0,ipady=10,padx=10,pady=20,sticky="ew")
        
    def buttons(self):

        frame=tk.Frame(self)
        frame.grid(row=1,column=0)

        # row 1
        button=tk.Button(frame,text="AC",font="Helvetica 18",padx=0,bg="#4E4E50",fg="white",activebackground="#636366",activeforeground="white")  
        button.grid(row=1,column=0,padx=10)
        button.bind("<Button-1>",self.click) 

        button=tk.Button(frame,text="%",font="Helvetica 18",padx=3,bg="#4E4E50",fg="white",activebackground="#636366",activeforeground="white")
        button.grid(row=1,column=1,padx=10)
        button.bind("<Button-1>",self.click)

        button=tk.Button(frame,text="⌫",font="Helvetica 18",padx=0,bg="#4E4E50",fg="white",activebackground="#636366",activeforeground="white")
        button.grid(row=1,column=2,padx=10)
        button.bind("<Button-1>",self.click)

        button=tk.Button(frame,text="÷",font="Helvetica 18",padx=7,bg="orange",activebackground="#E08500")
        button.grid(row=1,column=3,padx=10)
        button.bind("<Button-1>",self.click)

        # row 2
        for i in range(3):
            button=tk.Button(frame,text=f"{i+7}",font="Helvetica 18",padx=7,bg="#F2F2F7")
            button.grid(row=2,column=i,padx=10,pady=10)
            button.bind("<Button-1>",self.click)

        button=tk.Button(frame,text="×",font="Helvetica 18",padx=7,bg="orange",activebackground="#E08500")
        button.grid(row=2,column=i+1,padx=10)
        button.bind("<Button-1>",self.click)

        # row 3
        for i in range(3):
            button=tk.Button(frame,text=f"{i+4}",font="Helvetica 18",padx=7,bg="#F2F2F7")
            button.grid(row=3,column=i,padx=10)
            button.bind("<Button-1>",self.click)
        
        button=tk.Button(frame,text="-",font="Helvetica 18",padx=7,bg="orange",activebackground="#E08500")
        button.grid(row=3,column=i+1,padx=10,ipadx=3)
        button.bind("<Button-1>",self.click)
        
        # row 4
        for i in range(3):
            button=tk.Button(frame,text=f"{i+1}",font="Helvetica 18",padx=7,bg="#F2F2F7")
            button.grid(row=4,column=i,padx=10,pady=10)
            button.bind("<Button-1>",self.click)
        
        button=tk.Button(frame,text="+",font="Helvetica 18",padx=7,bg="orange",activebackground="#E08500")
        button.grid(row=4,column=i+1,padx=10)
        button.bind("<Button-1>",self.click)

        # row 5
        button=tk.Button(frame,text="00",font="Helvetica 18",padx=1,bg="#F2F2F7")
        button.grid(row=5,column=0,padx=10)
        button.bind("<Button-1>",self.click)
        
        button=tk.Button(frame,text="0",font="Helvetica 18",padx=7,bg="#F2F2F7")
        button.grid(row=5,column=1,padx=10)
        button.bind("<Button-1>",self.click)
        
        button=tk.Button(frame,text=".",font="Helvetica 18",padx=10,bg="#F2F2F7")
        button.grid(row=5,column=2,padx=10)
        button.bind("<Button-1>",self.click)
        
        button=tk.Button(frame,text="=",font="Helvetica 18",padx=7,bg="orange",activebackground="#E08500")
        button.grid(row=5,column=3,padx=10)
        button.bind("<Button-1>",self.click)

        # bind keyboard key
        self.bind("<Return>",self.calculate)
        self.bind("<Key>",self.key_input)
        self.bind("<BackSpace>",self.backspace)
        self.bind("<Delete>",self.delete)
if __name__ == "__main__":
    app = CalculatorGui()
    app.mainloop()