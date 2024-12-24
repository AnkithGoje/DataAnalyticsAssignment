from data_cleaning import load_and_clean_data
from analysis import analyze_popular_dishes, analyze_user_demographics, analyze_cancellation_trends, calculate_cancellation_trends, analyze_favorite_meal
from visualizations import plot_popular_dishes, plot_age_distribution, plot_cancellation_trends, plot_favorite_meals

# File paths
user_file = 'data/Data Analyst Intern Assignment - Excel.xlsx', sheet_name='UserDetails.csv'
cooking_file = 'data/Data Analyst Intern Assignment - Excel.xlsx', sheet_name='CookingSessions.csv'
order_file = 'data/Data Analyst Intern Assignment - Excel.xlsx', sheet_name='OrderDetails.csv'

# Load and clean data
print("Loading and cleaning data...")
merged_data = load_and_clean_data(user_file, cooking_file, order_file)

# Analyze data
print("Analyzing data...")
popular_dishes = analyze_popular_dishes(merged_data)
age_distribution = analyze_user_demographics(merged_data)
calculate_cancellation_trends = calculate_cancellation_trends(merged_data)
analyze_favorite_meals = analyze_favorite_meals(merged_data)
analyze_cancellation_trends = analyze_cancellation_trends(merged_data)


# Visualize data
print("Generating visualizations...")
plot_popular_dishes(popular_dishes)
plot_age_distribution(age_distribution)
plot_cancellation_trends(calculate_cancellation_trends)
plot_favorite_meals(favorite_meals)

# Save cleaned data
merged_data.to_excel('data/Cleaned_Merged_Dataset.xlsx', index=False)
print("Cleaned data saved to 'data/Cleaned_Merged_Dataset.xlsx'.")

# Summary of findings and recommendations
print("Summary of Insights:")
print(f"Most popular dish: {popular_dishes.iloc[0]['Dish Name_x']} with {popular_dishes.iloc[0]['Orders']} orders.")
print("Users in the age group 25-35 are the most active.")
print("Dinner is the most frequently ordered meal type.")
