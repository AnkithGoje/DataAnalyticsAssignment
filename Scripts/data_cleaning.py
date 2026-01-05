import pandas as pd

def load_and_clean_data(excel_file):
    # Load datasets from specific sheets
    user_details = pd.read_excel(excel_file, sheet_name='UserDetails.csv')
    cooking_sessions = pd.read_excel(excel_file, sheet_name='CookingSessions.csv')
    order_details = pd.read_excel(excel_file, sheet_name='OrderDetails.csv')
    
    # Merge datasets
    merged_data = order_details.merge(cooking_sessions, on=['Session ID', 'User ID'], how='inner')
    merged_data = merged_data.merge(user_details, on='User ID', how='inner')
    
    # Handle missing values
    merged_data.fillna({'Rating': 0, 'Session Rating': 0, 'Order Status': 'Unknown'}, inplace=True)
    
    # Add derived columns
    merged_data['Order Amount per Minute'] = merged_data['Amount (USD)'] / merged_data['Duration (mins)']
    merged_data['Is Canceled'] = merged_data['Order Status'].apply(lambda x: 1 if x == 'Canceled' else 0)
    
    # Droping duplicate columns
    merged_data.drop(columns=['Dish Name_y', 'Meal Type_y'], inplace=True, errors='ignore')
    merged_data.rename(columns={'Dish Name_x': 'Dish Name', 'Meal Type_x': 'Meal Type'}, inplace=True)

    return merged_data
