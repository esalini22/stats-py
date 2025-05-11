# import pandas lib as pd
import pandas as pd
import sys
import os
import statistics
import math

import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions

filename=None
dataframe=None

#regresion multiple no va
#inferencia no va
#calcular promedio por mes y estacion
#mediana y desviacion estandar por estacion
#histograma p2.5 y pm10 (coeficiente correlacion Pearson)

def clear():
    if sys.platform=='win32':
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')

def openFile():
    fn = askopenfilename(
        title="Select a file",
        filetypes=(
            ("All suported files", "*.xls *.xlsx *.txt *.csv"),
            ("Excel files", "*.xls *.xlsx"),
            ("Csv files", "*.csv"),
            ("Text files", "*.txt"))
    )
    if fn:
        global dataframe
        global filename
        filename = fn
        print("File: ", filename)
        table = {}
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            dataframe = pd.read_excel(filename, header=None)
            for i in range(len(dataframe.columns)):
                key = ""
                skip = False
                li = []
                for val in dataframe[i].tolist():
                    if val is None or val=="" or (isinstance(val, (int, float)) and math.isnan(val)):
                        if skip==True:
                            break
                    elif isinstance(val,str):
                        key = val
                        skip=True
                    else:
                        li.append(val)
                if len(li)>1:
                    table[key]=li
        elif filename.endswith('.txt'):
            dataframe = pd.read_table(filename, delimiter=" ", header=None)
            for i in range(len(dataframe.columns)):
                dataframe[i] = pd.to_numeric(dataframe[i].str.replace(',', '.'), errors='coerce')
                table.append(dataframe[i].tolist())
        elif filename.endswith('.csv'):
            dataframe = pd.read_csv(filename)
            for i in range(len(dataframe.columns)):     
                dataframe[i] = pd.to_numeric(dataframe[i].str.replace(',', '.'), errors='coerce')
                table.append(dataframe[i].tolist())
        dataframe = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in table.items() ]))
    print()

def mean():
    print("mean")
    if filename.endswith('.txt'):
        print(dataframe[0].mean())
    elif filename.endswith('.xls') or filename.endswith('.xlsx'):
        print("PM2.5: "+dataframe["PM2.5"].mean())
    print()

def main():
    clear()
    while True:
        print("Insert an option:")
        print("1. Select file")
        print("2. Print current file")
        print("3. Calculate mean")
        print("4. Calculate median")
        print("5. Calculate mean")
        print("Q. Exit program")
        option = input("Enter option ")
        if option=='Q' or option=='q':
            clear()
            exit()
        elif option=='1':
            clear()
            print("option "+option+"\n")
            openFile()
        elif option=='2':
            clear()
            print("option "+option+"\n")
            print("File: ", filename)
            print(dataframe)
        elif option=='3':
            clear()
            print("option "+option+"\n")
            mean()
        else:
            clear()
            print("option "+option+"\n")
            print("Enter a valid option\n")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
