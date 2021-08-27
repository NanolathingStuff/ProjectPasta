import os
"""
TODO https://stackoverflow.com/questions/1574088/plotting-time-in-python-with-matplotlib
TODO https://www.google.com/search?client=firefox-b-d&q=python+converting+%3Cclass+%27datetime.time%27%3E+to+to+NumPy+datetime
"""
##Installing packages
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
import numpy 
import datetime
import random


def main():
    df = pd.read_excel('ProjectPasta.xls', sheet_name=None) #The read_excel method of pandas lets you read all sheets in at once if you set the keyword parameter sheetname=None. 
    
    dataframes = [] #array of dataframes for every sheet in file
    for d in df:
        #print(df.get(d), type(df.get(d)), len(df.get(d)))
        dataframes.append(df.get(d))
    title = []
    x_axis, y_axis = [], []
    for d in dataframes:    #for i in len(dataframes):
        title.append(d.columns[0])   
        line_X, line_Y = [], []
        for y in range(0, len(d.columns)):
            for x in d.loc[ : , d.columns[y] ]: 
                if type(x) is datetime.time:# if not math.isnan(x):
                    #line.append( (x, y) ) 
                    try:
                        line_X.append(x.hour*3600+x.minute*60.0+x.second)
                    except: 
                        print("ERROR", x, type(x))
                    line_Y.append("cruda" if y==1 else "al dente" if y==2 else "cotta")
        #dates = matplotlib.dates.date2num(line_X)
        
        # sort by time and be sure line_X[i] correspond line_Y[i]
        #print(line_X, numpy.argsort(line_X))
        sortlist = numpy.argsort(line_X)
        X_line, Y_line = [], []
        for i in sortlist:
            X_line.append(line_X[i])
            Y_line.append(line_Y[i])

        x_axis.append(X_line)
        y_axis.append(Y_line)

    max_time=0
    for i in range(len(x_axis)):    #3):#
        plt.plot(x_axis[i], y_axis[i], label = title[i], alpha=0.7, marker='o', linewidth=random.uniform(1, 4))
        if max(x_axis[i]) > max_time:   # used for set x_axis distances later
            max_time = max(x_axis[i])
    plt.title('Cooking type pasta', fontsize=16)
    plt.xlabel('Seconds')
    plt.ylabel('Cooked grade')
    plt.xticks(numpy.arange(0, max_time+100, 60.0))   # set x_axis scale
    plt.legend()
    plt.grid(True)
    plt.show()
    
    #plt.savefig('pasta cooking time.pdf')

if __name__ == "__main__":
    # execute only if run as a script
    main()
