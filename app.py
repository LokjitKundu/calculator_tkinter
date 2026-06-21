import tkinter as tk
import os

class CalculatorGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x390")
        self.title("Calculator")
        self.resizable(False, False)
        self.screen()
        self.place_buttons()
        # bind keyboard key
        self.bind("<Return>",self.calculate)
        self.bind("<Key>",self.key_input)
        self.bind("<BackSpace>",self.backspace)
        self.bind("<Delete>",self.delete)

    def calculate(self,event=None):
        expr=self.screen_value.get()
        if not expr:
                return
        if expr[-1] in "+-×÷":
                return
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
        
        operators1="+-×÷%"
        operators2="+×÷%"
        
        current=self.screen_value.get()
        
        if text in operators1:
            # prevent typing consecutive operators
            if current and current[-1] in operators1:
                return
            
        if text in operators2:
            # prevent typing operators (except "-") if screen is empty
            if not current:
                return
            
        if text==".":
            # The loop keeps only the part after the last operator
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
            if current in ("ERROR", "CANNOT DIVIDE BY ZERO"):
                # if error is faced, press any key to set the screen value according to the pressed key value
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

            keyboard_operators1 = "+-*/"
            keyboard_operators2 = "+*/"
            
            if symbol in keyboard_operators2:
                if not current:
                    return
            if current and current[-1] in keyboard_operators1:
                return
            
            # replacing computer mathematical symbols with calculator symbols
            symbol = symbol.replace("*", "×")
            symbol = symbol.replace("/", "÷")
            
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

    def create_button(self,parent,text,button_padx=0,grid_padx=10,grid_pady=0,row=0,column=0,activebackground=None,activeforeground=None,bg=None,fg=None):
        
        button=tk.Button(parent,text=text,padx=button_padx,font="Helvetica 18",bg=bg,fg=fg,activebackground=activebackground,activeforeground=activeforeground)
        button.grid(row=row,column=column,padx=grid_padx,pady=grid_pady)
        button.bind("<Button-1>",self.click)
        return

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
        
    def place_buttons(self):

        frame=tk.Frame(self)
        frame.grid(row=1,column=0)

        # row 1
        self.create_button(frame,"AC",row=1,column=0,activebackground="#636366",activeforeground="white",bg="#4E4E50",fg="white") 
        self.create_button(frame,"%",button_padx=5,row=1,column=1,activebackground="#636366",activeforeground="white",bg="#4E4E50",fg="white") 
        self.create_button(frame,"⌫",row=1,column=2,activebackground="#636366",activeforeground="white",bg="#4E4E50",fg="white") 
        self.create_button(frame,"÷",button_padx=7,row=1,column=3,activebackground="#E08500",bg="orange",fg="black")

        # row 2
        for i in range(3):
            self.create_button(frame,f"{i+7}",button_padx=7,grid_pady=10,row=2,column=i,bg="#F2F2F7",fg="black")

        self.create_button(frame,"×",button_padx=7,row=2,column=i+1,activebackground="#E08500",bg="orange",fg="black")

        # row 3
        for i in range(3):
            self.create_button(frame,f"{i+4}",button_padx=7,grid_pady=0,row=3,column=i,bg="#F2F2F7",fg="black")
        
        self.create_button(frame,"-",button_padx=10,row=3,column=i+1,activebackground="#E08500",bg="orange",fg="black")
        
        # row 4
        for i in range(3):
            self.create_button(frame,f"{i+1}",button_padx=7,grid_pady=10,row=4,column=i,bg="#F2F2F7",fg="black")
        
        self.create_button(frame,"+",button_padx=7,row=4,column=i+1,activebackground="#E08500",bg="orange",fg="black")

        # row 5
        self.create_button(frame,"00",button_padx=1,grid_pady=0,row=5,column=0,bg="#F2F2F7",fg="black")
        self.create_button(frame,"0",button_padx=7,grid_pady=0,row=5,column=1,bg="#F2F2F7",fg="black")
        self.create_button(frame,".",button_padx=10,grid_pady=0,row=5,column=2,bg="#F2F2F7",fg="black")
        self.create_button(frame,"=",button_padx=7,grid_pady=0,row=5,column=3,bg="#F2F2F7",fg="black")

if __name__ == "__main__":
    app = CalculatorGui()
    app.mainloop()