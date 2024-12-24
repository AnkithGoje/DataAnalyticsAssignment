def plot_popular_dishes(popular_dishes, output_file='top_10_dishes.png'):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=popular_dishes['Orders'].head(10), y=popular_dishes['Dish Name'].head(10), palette='viridis')
    plt.title('Top 10 Popular Dishes')
    plt.xlabel('Number of Orders')
    plt.ylabel('Dish Name')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def plot_age_distribution(age_distribution, output_file='age_distribution.png'):
    plt.figure(figsize=(10, 5))
    sns.barplot(x=age_distribution['index'], y=age_distribution['Age'], palette='coolwarm')
    plt.title('User Age Distribution')
    plt.xlabel('Age Groups')
    plt.ylabel('Number of Users')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def plot_favorite_meals(favorite_meal_analysis, output_file='favorite_meal_analysis.png'):
    plt.figure(figsize=(10, 5))
    sns.barplot(data=favorite_meal_analysis, x='Favorite Meal', y='Total_Orders', palette='plasma')
    plt.title('Favorite Meals by Total Orders')
    plt.xticks(rotation=45)  # Rotate x labels for better readability
    plt.xlabel('Favorite Meal')
    plt.ylabel('Total Orders')
    plt.tight_layout()  # Adjust layout to make room for rotated x labels
    plt.savefig(output_file)
    plt.show()

def plot_cancellation_trends(cancellation_trends, output_file='cancellation_trends.png'):
    plt.figure(figsize=(8, 6))
    sns.barplot(data=cancellation_trends, x='Is Canceled', y='Total_Orders', palette='pastel')
    plt.title('Cancellation Trends')
    plt.xlabel('Is Canceled (1 = Yes, 0 = No)')
    plt.ylabel('Total Orders')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
