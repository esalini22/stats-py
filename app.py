# import pandas lib as pd
import pandas as pd
import sys
import os

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

def mean():
    print("mean")
    print(dataframe)
    return

def menu():
    clear()
    while True:
        print("File: "+filename)
        print("Insert an option:")
        print("1. Calculate mean")
        print("2. Calculate median")
        print("3. Calculate mean")
        print("Q. Exit program")
        option = input("Enter option ")
        if option=='Q' or option=='q':
            clear()
            exit()
        elif option=='1':
            mean()
        else:
            clear()
            print("Enter a valid option\n")

# Defining main function
def main():
    if len(sys.argv)==1:
        print("You need to specify a .xsls file")
    elif len(sys.argv)==1:
        print("Too many arguments")
    else:
        global filename
        filename = sys.argv[1]
        if os.path.exists(filename):
            # read by default 1st sheet of an excel file
            global dataframe
            dataframe = pd.read_excel(filename)
            menu()
        else:
            print("File doesn't exist")

# Using the special variable 
# __name__
if __name__=="__main__":
    main()