import pandas as pd
import os


folder_path = '../csvFiles'

def read_customer_file():
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    print(csv_files)
    for file in csv_files:
        print(f"\nProcessing file: {file}")
        
        
        
        
read_customer_file()