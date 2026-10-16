import logging
import os
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_data(tables: dict):
    # Fetch database credentials securely from environment variables
    DB_USER = os.getenv("DB_USER", "DB_USER") # enter ur db details 
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password") # enter ur db details 
    DB_HOST = os.getenv("DB_HOST", "host_anme") # enter ur db details 
    DB_PORT = os.getenv("DB_PORT", "port_num") # enter ur db details 
    DB_NAME = os.getenv("DB_NAME", "food_pipeline")  # enter ur db details 
    
    conn_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    
    # Create the engine once outside the loop for better performance
    try:
        engine = create_engine(conn_string)
    except Exception as e:
        logging.error(f"Failed to create database engine: {e}")
        raise

    # Iterate through and load each dataframe
    for table_name, df in tables.items():
        try:
            logging.info(f"Loading {table_name}...")
            
            # Using table_name dynamically; removed the duplicate undefined TARGET_TABLE call
            df.to_sql(name=table_name, con=engine, if_exists="replace", index=True)
            
            logging.info(f"Successfully loaded {table_name}....")
        except Exception as e:
            logging.error(f"Failed to load table {table_name}: {e}")
            raise

    logging.info("All dim and fact tables have been loaded successfully!")
