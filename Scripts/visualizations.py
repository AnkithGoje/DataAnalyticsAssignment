import matplotlib.pyplot as plt
import seaborn as sns

# Set global theme for eye-catchy visualizations
sns.set_theme(style="whitegrid", context="talk")

def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart."""
    for p in ax.patches:
        if p.get_height() > 0:  # For vertical bars
            ax.annotate(f'{int(p.get_height())}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        xytext=(0, spacing), 
                        textcoords='offset points',
                        fontsize=10, color='black', fontweight='bold')
        elif p.get_width() > 0: # For horizontal bars (if any)
            ax.annotate(f'{int(p.get_width())}', 
                        (p.get_width(), p.get_y() + p.get_height() / 2.), 
                        ha='left', va='center', 
                        xytext=(spacing, 0), 
                        textcoords='offset points',
                        fontsize=10, color='black', fontweight='bold')

def plot_popular_dishes(popular_dishes, output_file='top_10_dishes.png'):
    plt.figure(figsize=(14, 8), dpi=300)
    ax = sns.barplot(
        x=popular_dishes['Orders'].head(10), 
        y=popular_dishes['Dish Name'].head(10), 
        palette='viridis', 
        hue=popular_dishes['Dish Name'].head(10), 
        legend=False
    )
    
    plt.title('Top 10 Most Popular Dishes', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Number of Orders', fontsize=14, labelpad=10)
    plt.ylabel('Dish Name', fontsize=14, labelpad=10)
    
    # Add value annotations (horizontal bars)
    for p in ax.patches:
        width = p.get_width()
        if width > 0:
            ax.annotate(f'{int(width)}', 
                        (width, p.get_y() + p.get_height() / 2.), 
                        ha='left', va='center', 
                        xytext=(10, 0), 
                        textcoords='offset points',
                        fontsize=12, fontweight='bold', color='#333333')
            
    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight')
    # plt.show()
    print(f"Saved: {output_file}")

def plot_age_distribution(age_distribution, output_file='age_distribution.png'):
    plt.figure(figsize=(12, 7), dpi=300)
    ax = sns.barplot(
        x=age_distribution['Age_Group'], 
        y=age_distribution['User_Count'], 
        palette='magma', 
        hue=age_distribution['Age_Group'], 
        legend=False
    )
    
    plt.title('User Demographics: Age Distribution', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Age Group', fontsize=14, labelpad=10)
    plt.ylabel('Count of Users', fontsize=14, labelpad=10)
    
    add_value_labels(ax)
    sns.despine()
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight')
    # plt.show()
    print(f"Saved: {output_file}")

def plot_favorite_meals(favorite_meal_analysis, output_file='favorite_meal_analysis.png'):
    plt.figure(figsize=(12, 7), dpi=300)
    ax = sns.barplot(
        data=favorite_meal_analysis, 
        x='Favorite Meal', 
        y='Total_Orders', 
        palette='crest', 
        hue='Favorite Meal', 
        legend=False
    )
    
    plt.title('Favorite Meal Types by Order Volume', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Meal Type', fontsize=14, labelpad=10)
    plt.ylabel('Total Orders', fontsize=14, labelpad=10)
    plt.xticks(rotation=0)
    
    add_value_labels(ax)
    sns.despine()
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight')
    # plt.show()
    print(f"Saved: {output_file}")

def plot_cancellation_trends(cancellation_trends, output_file='cancellation_trends.png'):
    plt.figure(figsize=(10, 7), dpi=300)
    
    # Map 0/1 to readable labels for plotting
    plot_data = cancellation_trends.copy()
    plot_data['Status'] = plot_data['Is Canceled'].map({0: 'Completed', 1: 'Canceled'})
    
    ax = sns.barplot(
        data=plot_data, 
        x='Status', 
        y='Total_Orders', 
        palette='rocket', 
        hue='Status', 
        legend=False
    )
    
    plt.title('Order Cancellation Trends', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Order Status', fontsize=14, labelpad=10)
    plt.ylabel('Number of Orders', fontsize=14, labelpad=10)
    
    add_value_labels(ax)
    sns.despine()
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight')
    # plt.show()
    print(f"Saved: {output_file}")
