import pandas as pd 
import numpy as np  

def extract_data():
 df = pd.read_csv("/Users/name/Desktop/data/synthetic_food_delivery_transactions.csv")  
# 1. Non-null value count per column (Fixed: properly assign .columns)
 columns_count = df.notnull().sum().reset_index()
 columns_count.columns = ['column_name', 'non_null_count'] 
 print(columns_count)

# 2. Displaying null value count per column  
 null_counts = df.isnull().sum().reset_index()
 null_counts.columns = ['column_name', 'null_values_count']
 print(null_counts) 

# 3. Display duplicates per column 
 duplicate_count = df.apply(lambda x:x.duplicated()).sum().reset_index()
 duplicate_count.columns = ['column_name', 'duplicate_count']
 print(duplicate_count)

# 4. Correct way to combine and display them together
 summary_df = pd.merge(columns_count, null_counts, on='column_name').merge(duplicate_count, on='column_name')
 print("\n--- Column Health Summary ---")
 print(summary_df) 
 col = ['order_timestamp','delivery_timestamp'] 
 df[col] = df[col].apply(pd.to_datetime)
 df['discount_code']= df['discount_code'].fillna('No_discount_code') 
 df['discount_type']= df['discount_type'].fillna('No_discount_type') 
 df.drop_duplicates()
 return df

df = extract_data()

