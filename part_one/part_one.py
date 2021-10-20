"""
Given a CSV file, write a function that will open this file, validate the data and output a new file (good_data.csv).
"""
GOOD_DATA_FILE_NAME = "good_data.csv"

import pandas as pd
from google.colab import files
def validate_and_load_files(df):
    "In the below line of code I am filtering the data if id,email and eircode is null. Also, verifying the "@" in the mail and length of EIRCODE should me 7."
    df1 = df[(df['id']!="null") & (df['email']!="null") & (df['eircode']!="null") & (df['email'].str.contains("@")) & (df['eircode'].str.len()==7) ] 
    
    "I am converting the value of id to number and non int value will be NaN."
    df1.id = pd.to_numeric(df1.id, errors='coerce')   "It will convert any non-int value to NaN"

    "In the last I am varifying the eircode should be Alpha-numberic. Also first-name and last-name should contain only alphabets"
    df1 = df1[(df1["eircode"].str.isalnum()) & (df1["first_name"].str.isalpha()) & (df1["last_name"].str.isalpha())]
    print(df1.head(30))

    "And final step. Creating new CSV of Good_data as requested. It will help you to download the csv automatically :)"
    df1.to_csv(GOOD_DATA_FILE_NAME) 
    files.download(GOOD_DATA_FILE_NAME)

if __name__ == "__main__":
    df = pd.read_csv('mock_data_1000.csv')
    validate_and_load_files(df)
