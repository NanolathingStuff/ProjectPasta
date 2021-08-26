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
    xlabel, ylabel = numpy.arange(0, 16), numpy.array(["raw", "undercocked", "coocked", "overcoocked"])
    #print(xlabel, type(xlabel))
    #print(ylabel, type(ylabel))
    for d in dataframes:    #for i in len(dataframes):
        title = d.columns[0]
        data = plot_values(d.drop(d.columns[0], axis=1))
        #TODO test data
        zip(*data)
        plt.plot(*zip(*data), label = title)#plt.scatter(*zip(*data), label = title)
        #plt.plot(data[0], data[1], label = title) ###some error here   
    # naming the axis 
    plt.xlabel('time to cook') #TODO problems with  x label
    plt.xticks(xlabel, rotation='vertical') # 
    plt.ylabel('type') 
    #yval = [ylabel[i] for i in data[1]] 
    yval = []
    #print(len(data), type(data))
    for i in range(0, len(data)):
        #print(data[i][1], ylabel[data[i][1]])
        #print(i)
        yval.append(ylabel[data[i][1]])
    plt.yticks(numpy.arange(4), ylabel) #plt.yticks(data[1], yval) 
    #print(len(data[1]), len(ylabel))
    # giving a title to my graph 
    plt.title = 'Pastas time cooking' 
    #TODO single scale for y and y axis
    ##try>>> plot('xlabel', 'ylabel', data=obj)
    plt.axis = [0, 16, 0, 3] #axis constains
    # show a legend on the plot and show it
    #for d in dataframes:
        #plt.plot(xlabel, ylabel, data=d)
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
    #return [x, y]
    ####TEST
    d = []
    for i in range(0, len(y_axis)):
        d.append(tuple((x[i], y[i])) )
    #print(d)
    return d
    

def main():
    df = pd.read_excel('ProjectPasta.xls', sheet_name=None) #The read_excel method of pandas lets you read all sheets in at once if you set the keyword parameter sheetname=None. 
    #print(type(df), len(df), df) #This returns a dictionary - the keys are the sheet names, and the values are the sheets as dataframes. 
    #df1 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio1")
    #df2 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio2")
    #df3 = pd.read_excel('ProjectPasta.xls', sheet_name="Foglio3")
    #print(df1.to_string(),"\n", df2.to_string()) 
    #graph(df1) #it works
    #graphs([df1, df2]) #has TODOs #, df3
    #testList =[(0, 6), (1, 2), (2, 7), (3, 5), (4, 3), (5, 4)]
    #plt.plot(testList)
    #plt.show()
    dataframes = [] #array of dataframes for every sheet in file
    for d in df:
        #print(df.get(d), type(df.get(d)), len(df.get(d)))
        dataframes.append(df.get(d))
    title = []
    #data = []
    x_axis = []
    y_axis = []
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
        
        # TODO: sort by time and be sure line_X[i] correspond line_Y[i]

        x_axis.append(line_X)
        y_axis.append(line_Y)
        #print(line_X, line_Y, len(line_X) == len(line_Y), type(line_X), type(line_Y))
        #data.append(line)
    #print(x_axis[0], y_axis[0], type(x_axis[0]), type(y_axis[0]), len(x_axis[0]) == len(y_axis[0]))
    #plt.plot(x_axis[0], y_axis[0], label = "line 1", marker='o')
    for i in range(3):#len(x_axis)):
        plt.plot(x_axis[i], y_axis[i], label = title[i], marker='o')
    plt.title('Cooking type pasta', fontsize=16)
    plt.xlabel('Seconds')
    plt.ylabel('Cooked grade')
    plt.legend()
    plt.grid(True)
    plt.show()
    #print(title, data)
    #print(title[0], data[0])
    #matplotlib.pyplot.plot_date(dates, y_axis)


if __name__ == "__main__":
    # execute only if run as a script
    main()
# %%
#TODO finish for 1 and many graph
# vedi fin quando diventa incasinato
# impara a scorrere tutti gli sheet nel xml