import subprocess
import time
import threading
import os
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

'''

@WinchesterAge

this is first version of this app 
i made it to keep me focused while i'm reading my leasons 
OR coding other programms


'''
class focus:
    
    def __init__(self, task, dur):
        self.task = task
        self.dur = dur
        

    def process_kill(self):
        
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

    def clicked():
        root.lower()
        f = focus(task=process_name.get(), dur=time_b.get())
        f.process_kill()
        
    root = tk.Tk()
    root.geometry('400x200')
    root.resizable(False, False)
    root.title("Focus App")


    process_name = tk.StringVar()
    time_b = tk.IntVar()

    lable = ttk.Label(text="Process Name").pack()
    process_name_box = ttk.Entry(root, textvariable=process_name).pack()
    
    ttk.Label(text="Time(min)").pack()

    time_box = ttk.Entry(root,textvariable=time_b).pack()

    button = ttk.Button(root,text="Run",command=clicked,padding=10).pack(expand=True)
    
    root.mainloop()
    

