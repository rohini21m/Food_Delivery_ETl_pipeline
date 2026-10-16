import pandas as pd 
import numpy as np 

def transform_data(df):
    dim_customers = df[['customer_id','customer_loyalty_tier',
                        'customer_acquisition_channel',
                        'customer_signup_date']].drop_duplicates().reset_index(drop=True) 
    dim_menu= df[['menu_item_id','menu_item_name','menu_item_category']].drop_duplicates().reset_index(drop=True) 
   # resetindex(True) to prevent transformed column into old regular column again 
    dim_restaurants= df[['restaurant_id',
                         'restaurant_cuisine',
                         'restaurant_city',
                         'restaurant_rating',
                         'restaurant_avg_prep_time']].drop_duplicates().reset_index(drop=True)  
    dim_discounts = df[['discount_code','discount_type','discount_value']].drop_duplicates().reset_index(drop=True)  
    dim_weather = df[['weather_temperature',
                      'weather_precipitation',
                      'is_weekend',
                      'is_holiday']].drop_duplicates().reset_index(drop=True) 
    dim_weather['weather_id']= dim_weather.index # Foreign Key pointing to a Surrogate Key (weather_id):
#Because weather_id did not exist in the raw file, you had to merge dim_weather back into df. This allowed fact_orders to use weather_id as a 
#foreign key to link each order to its respective weather conditions.   
    df= df.merge(dim_weather,on=['weather_temperature',
                      'weather_precipitation',
                      'is_weekend',
                      'is_holiday'], 
                      how='left')
    fact_orders = df[['order_id',
                      'customer_id',
                      'item_price',
                      'quantity',
                      'order_timestamp',
                      'restaurant_id',
                      'delivery_timestamp',
                      'delivery_duration_actual',
                      'delivery_duration_estimated',
                      'delivery_fee',
                      'tip',
                      'total_amount',
                      'order_status','weather_id']].drop_duplicates().reset_index(drop=True) 
    
    return {
                              'dim_customers':dim_customers,
                              'dim_menu':dim_menu,
                              'dim_resturants' : dim_restaurants,
                              'dim_discounts':dim_discounts,
                              'dim_weather': dim_weather,
                              'dim_discounts': dim_discounts,
                              'fact_orders' : fact_orders
                            } 



 
