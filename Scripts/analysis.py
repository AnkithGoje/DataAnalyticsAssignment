# Analyze popular dishes
def analyze_popular_dishes(merged_data):
    # Filter out canceled orders
    valid_orders = merged_data[merged_data['Order Status'] != 'Canceled'].copy()
    
    # Normalize dish names to title case to handle inconsistencies
    valid_orders['Dish Name'] = valid_orders['Dish Name'].astype(str).str.title()
    
    return valid_orders.groupby('Dish Name').agg(
        Orders=('Order ID', 'count'),
        Average_Rating=('Rating', 'mean'),
        Total_Amount=('Amount (USD)', 'sum')
    ).reset_index().sort_values(by='Orders', ascending=False)

# Age distribution of users
def analyze_user_demographics(merged_data):
    df = merged_data['Age'].value_counts(bins=5).reset_index()
    df.columns = ['Age_Group', 'User_Count']
    return df

# Cancellation trends analysis
def calculate_cancellation_trends(merged_data):
    # Ensure Is Canceled is consistently calculated
    merged_data['Is Canceled'] = merged_data['Order Status'].apply(lambda x: 1 if x == 'Canceled' else 0)
    
    cancellation_trends = merged_data.groupby('Is Canceled').agg(
        Total_Orders=('Order ID', 'count'),
        Average_Order_Amount=('Amount (USD)', 'mean')
    ).reset_index()
    return cancellation_trends

# Favorite meal analysis
def analyze_favorite_meal(merged_data):
    # Filter out canceled orders for accurate preference analysis
    valid_orders = merged_data[merged_data['Order Status'] != 'Canceled']
    
    favorite_meal_analysis = valid_orders.groupby('Favorite Meal').agg(
        Total_Orders=('Order ID', 'count'),
        Average_Session_Rating=('Session Rating', 'mean')
    ).reset_index().sort_values(by='Total_Orders', ascending=False)
    return favorite_meal_analysis

# analyze cancellaion trends
def analyze_cancellation_trends(merged_data):
    return merged_data.groupby('Order Status')['Order ID'].count().reset_index()