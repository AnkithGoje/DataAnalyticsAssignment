# Analyze popular dishes
def analyze_popular_dishes(merged_data):
    return merged_data.groupby('Dish Name').agg(
        Orders=('Order ID', 'count'),
        Average_Rating=('Rating', 'mean'),
        Total_Amount=('Amount (USD)', 'sum')
    ).reset_index().sort_values(by='Orders', ascending=False)

# Age distribution of users
def analyze_user_demographics(merged_data):
    return merged_data['Age'].value_counts(bins=5).reset_index()

# Cancellation trends analysis
def calculate_cancellation_trends(merged_data):
    cancellation_trends = merged_data.groupby('Is Canceled').agg(
        Total_Orders=('Order ID', 'count'),
        Average_Order_Amount=('Amount (USD)', 'mean')
    ).reset_index()
    return cancellation_trends

# Favorite meal analysis
def analyze_favorite_meal(mergerd_data):
    favorite_meal_analysis = merged_data.groupby('Favorite Meal').agg(
        Total_Orders=('Order ID', 'count'),
        Average_Session_Rating=('Session Rating', 'mean')
    ).reset_index().sort_values(by='Total_Orders', ascending=False)
    return favorite_meal_analysis

# analyze cancellaion trends
def analyze_cancellation_trends(merged_data):
    return merged_data.groupby('Order Status')['Order ID'].count().reset_index()