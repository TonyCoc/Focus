import subprocess
import time
import threading
import os
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
import threading

'''

@WinchesterAge


i made this app to keep me focused while i'm reading my leasons 
OR coding other programms

'''
class focus:
    
    def __init__(self, task, dur):
        self.task = task
        self.dur = dur
        

    def process_kill(self):

        if " " in self.task:
            
            clear_task = ""

            for char in self.task:

                if char != " ":
                    clear_task += char
            self.task = clear_task
        
        passed_time = 0   #sec

        
        while passed_time < self.dur * 60:
            
                command = subprocess.Popen(['powershell.exe','ps',self.task],stdout=subprocess.PIPE,shell=False)

                pure_output = []      #with out spaces,'/' & '-'

                for _ in command.communicate()[0].decode().split(" "):
                    if ' ' not in _ and '-' not in _ and '\r' not in _ and _ != '':
                        pure_output.append(_)


                if "Cannot" not in pure_output:
                    for ind,item in enumerate(pure_output):
                        if item.lower() == self.task.lower():
                            command = subprocess.run(['powershell.exe','kill',pure_output[ind-2]],shell=False)    #index of pId == process name index - 2
                            os.system("cls")
        
                time.sleep(1.0)
                passed_time += 1





if __name__ == "__main__":

    is_running = False

    def clicked():

        

        def count():
            Min = time_b.get()
            while Min > 0:
                l.config(text=f"{Min} minutes left",foreground="Red")
                time.sleep(60.0)
                Min -= 1
            
            l.config(foreground="Green")
            
            time.sleep(1)

            root.destroy()

            exit()
            

            
                
        
        
        f = focus(task=process_name.get(), dur=time_b.get())
        t1 = threading.Thread(target=f.process_kill).start()
        l = ttk.Label(text="")
        l.pack()
        
        t2 = threading.Thread(target=count).start()
        
        
     
        
        

        
        
        
    root = tk.Tk()
    root.geometry('400x200')
    root.resizable(False, False)
    root.title("Focus App")


    process_name = tk.StringVar()
    time_b = tk.IntVar()

    lable = ttk.Label(text="Programm Name").pack()
    process_name_box = ttk.Entry(root, textvariable=process_name).pack()
    
    ttk.Label(text="Time(min)").pack()

    time_box = ttk.Entry(root,textvariable=time_b).pack()

    button = ttk.Button(root,text="Run",command=clicked,padding=10)
    button.pack(expand=True)
    
    
    root.mainloop()
    

