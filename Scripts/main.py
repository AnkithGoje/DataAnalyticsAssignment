from data_cleaning import load_and_clean_data
from analysis import analyze_popular_dishes, analyze_user_demographics, analyze_cancellation_trends, calculate_cancellation_trends, analyze_favorite_meal
from visualizations import plot_popular_dishes, plot_age_distribution, plot_cancellation_trends, plot_favorite_meals

# File paths
# File paths
excel_file = 'data/Data Analyst Intern Assignment - Excel.xlsx'

# Load and clean data
print("Loading and cleaning data...")
merged_data = load_and_clean_data(excel_file)

# Analyze data
print("Analyzing data...")
popular_dishes = analyze_popular_dishes(merged_data)
age_distribution_data = analyze_user_demographics(merged_data)
cancellation_trends_data = calculate_cancellation_trends(merged_data)
favorite_meals_data = analyze_favorite_meal(merged_data)
cancellation_status_data = analyze_cancellation_trends(merged_data)


# Visualize data
print("Generating visualizations...")
plot_popular_dishes(popular_dishes)
plot_age_distribution(age_distribution_data)
plot_cancellation_trends(cancellation_trends_data)
plot_favorite_meals(favorite_meals_data)

# Save cleaned data
merged_data.to_excel('data/Cleaned_Merged_Dataset.xlsx', index=False)
print("Cleaned data saved to 'data/Cleaned_Merged_Dataset.xlsx'.")

# Summary of findings and recommendations
print("Summary of Insights:")
print(f"Most popular dish: {popular_dishes.iloc[0]['Dish Name']} with {popular_dishes.iloc[0]['Orders']} orders.")
print("Users in the age group 25-35 are the most active.")
print("Dinner is the most frequently ordered meal type.")
