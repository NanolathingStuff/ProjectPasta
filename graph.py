import os

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


def main():
    #print("Installing packages")
    df1 = pd.read_excel('ProjectPasta.xls','Foglio1')
    df2 = pd.read_excel('ProjectPasta.xls','Foglio2')
    print(df1.to_string(), df2.to_string()) 


if __name__ == "__main__":
    # execute only if run as a script
    main()