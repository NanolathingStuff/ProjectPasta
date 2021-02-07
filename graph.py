import pandas as pd

def main():
    print("Hello World!")
    df = pd.read_csv('ProjectPasta.csv')
    print(df.to_string()) 


if __name__ == "__main__":
    # execute only if run as a script
    main()