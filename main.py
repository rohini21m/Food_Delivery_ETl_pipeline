import sys
import os

# This line fixes the path so your terminal can find the ETL folder instantly
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 2. Import using the lowercase folder name 'ETL'
from ETL.Extract import extract_data 
from ETL.Transform import transform_data 
from ETL.Load import load_data 

def run_pipeline():
    df = extract_data()
    tables = transform_data(df)
    load_data(tables)
    print('pipeline completed')

if __name__ == '__main__':
    run_pipeline()
