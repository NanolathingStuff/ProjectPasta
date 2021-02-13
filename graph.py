import os

##Installing packages##
#packages = os.system('pip freeze') #list')
#print(type(packages)) 
try:        
    import pandas as pd
except ImportError as e: #if 'pandas' not in packages:
    os.system('pip install pandas')
    import pandas as pd
try:        
    import xlrd
except ImportError as e: #if 'xlrd' not in packages:
    os.system('pip install xlrd')
try:
    import tkinter #remember to install 'tkinter' from python installation or you have to modify it
    import matplotlib # if bugs out seems '('pip uninstall package name' and reinstall fix this
    #matplotlib.use('GTK3Agg')
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg') 
except ImportError as e: #if 'matplotlib' not in packages or dependency failed:
    import tkinter #remember to install 'tkinter' from python installation or you have to modify it
    #os.system('pip install pycairo')
    #os.system('pip install PyGObject')
    os.system('pip install matplotlib')
    import matplotlib
    #matplotlib.use('GTK3Agg')
    import matplotlib.pyplot as plt
    matplotlib.use('TkAgg')

try:
    from IPython import get_ipython
    #get_ipython().run_line_magic('matplotlib', 'qt') #get_ipython().run_line_magic('matplotlib', 'inline')
except ImportError as e:
    os.system('pip install IPython')
    from IPython import get_ipython
    #get_ipython().run_line_magic('matplotlib', 'qt')

#import control libraries
import math 
import datetime
import array
#
from PIL import Image

def graph(dataframe): 
    title = dataframe.columns[0]
    print(title)
    #print(len(dataframe))
    data = dataframe.drop(dataframe.columns[0], axis=1)
    #print(dataframe, type(dataframe))
    #print(data, type(data))
    #print(data.columns, len(data.columns))
    value = {} #dictionary
    x_axis = []
    y_axis = []
    for y in range(0, len(data.columns)):
        for x in data.loc[ : , data.columns[y] ]:
            x_axis.append(str(x)) #apparently datetime type is unsupported; TypeError: float() argument must be a string or a number, not 'datetime.time'
            y_axis.append(y)
            #value[x] = y;#assign key = x = time : value = y = cooking grade
            #TODO check for empty value and sort dictionary
            #if isinstance(x, datetime.date) and (not math.isnan(x)):
            #sorted(value)
    for k, v in value.items(): #debug
        print(k, v)
    plt.plot(x_axis, y_axis)
    plt.title = title
    plt.show()

def graphs(dataframes): 
    for d in dataframes:    #for i in len(dataframes):
        title = d.columns[0]
        data = plot_values(d.drop(d.columns[0], axis=1))
        plt.plot(data[0], data[1], label = title) 
    # naming the axis 
    plt.xlabel('time to cook')  
    plt.ylabel('type') 
    # giving a title to my graph 
    plt.title = 'Pastas time cooking' 
    # show a legend on the plot and show it
    plt.legend() 
    plt.show() 
        

def plot_values(data):
    x_axis = []
    y_axis = []
    for y in range(0, len(data.columns)):
        for x in data.loc[ : , data.columns[y] ]:
            x_axis.append(str(x)) 
            y_axis.append(y)
            #TODO check for empty value and sort
            #TODO cut the first 2 '00'
    return [x_axis, y_axis]
    

def main():
    df1 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio1")
    df2 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio2")
    df3 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio3")
    #print(df1.to_string(),"\n", df2.to_string()) 
    #graph(df1) #it works
    graphs([df1, df2, df3]) #has TODOs


if __name__ == "__main__":
    # execute only if run as a script
    main()