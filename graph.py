import os

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
import math
import array

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
        #try>>> plot('xlabel', 'ylabel', data=obj)
        plt.plot(data[0], data[1], label = title) ###some error here   
    # naming the axis 
    plt.xlabel('time to cook')  
    plt.ylabel('type') 
    # giving a title to my graph 
    plt.title = 'Pastas time cooking' 
    #TODO single scale for y and y axis
    plt.xticks = numpy.linspace(0, 16, 16)
    plt.yticks = numpy.linspace(0, 3, 3)
    plt.axis = [0, 16, 0, 3] #axis constains
    # show a legend on the plot and show it
    plt.legend() 
    plt.show() 
        

def plot_values(data):
    x_axis = []
    y_axis = []
    for y in range(0, len(data.columns)):
        for x in data.loc[ : , data.columns[y] ]: 
            if type(x) is datetime.time:# if not math.isnan(x):
                x_axis.append(x) 
                y_axis.append(y) #cooking grade
                #print(type(x), x)
        #sorted_index_pos = [index for index, num in sorted(enumerate(x_axis), key=lambda x: x[-1])] #from https://stackoverflow.com/questions/50849300/sort-array-and-return-original-indexes-of-sorted-array/50849428
        sort_index = numpy.argsort(x_axis) 
        #print(sort_index) #debug

        #[str(i) for i in x_axis]
        x, y = [], [] #convert sorted x_axis to strings
        for t in x_axis:
            x.append(t.strftime("%M:%S")) #%H:
        #sort (y to sort_index)
        for i in sort_index:
            y.append(y_axis[i])
    return [x, y]
    

def main():
    df1 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio1")
    df2 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio2")
    df3 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio3")
    #print(df1.to_string(),"\n", df2.to_string()) 
    #graph(df1) #it works
    graphs([df1, df2]) #has TODOs #, df3


if __name__ == "__main__":
    # execute only if run as a script
    main()
# %%
