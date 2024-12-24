# **Data Analytics Assignment** #

## Objective ##
The goal of this assignment is to analyze datasets related to user behavior, cooking preferences, and order trends. This project focuses on:

  * Cleaning and merging data from three datasets: UserDetails, CookingSessions, and OrderDetails.
  * Exploring the relationship between cooking sessions and user orders.
  * Identifying popular dishes and uncovering demographic factors that influence user behavior.
  * Creating visualizations to showcase insights.
  * Writing a report summarizing findings and providing business recommendations.

## Project Structure ##
### 1. Data
The project utilizes three datasets:

  * **UserDetails.csv**: Contains user demographic information.
  * **CookingSessions.csv**: Logs details of cooking sessions.
  * **OrderDetails.csv**: Includes order-related information.

### 2. Scripts
The project code is split into modular scripts for better organization:

  * ```data_cleaning.py```: Contains functions to load, clean, and merge the datasets.
  * ```analysis.py```: Includes functions for analyzing the merged dataset (e.g., popular dishes, demographic insights).
  * ```visualizations.py```: Generates visualizations such as bar plots and age distributions.
  * ```main.py```: The entry point script that orchestrates the workflow by calling functions from the above scripts.

### 3. Outputs
  * Cleaned Dataset: A cleaned and merged dataset is saved as ```Cleaned_Merged_Dataset.csv```.

#### Visualizations:
  * ```top_10_dishes.png```: Visualizing the top 10 most popular dishes.
  * ```age_distribution.png```: Age group distribution of users.
* Report: Key findings and business recommendations in a structured format.

## How to Run the Project

### 1. Prerequisites
Ensure the following are installed:
 * Python 3.8 or later
 * Required Python libraries (see ```requirements.txt```)

Install dependencies using:
```
pip install -r requirements.txt
````

### 2. Directory Structure
Ensure the following directory structure:

```
Data Analytics Assignment/
│
├── data/
|   ├── Data Analyst Intern Assignment - Excel.xlsx/
│       ├── UserDetails.csv
│       ├── CookingSessions.csv
│       ├── OrderDetails.csv
│   └── Cleaned_Merged_Dataset.xlsx
│
├── scripts/
│   ├── data_cleaning.py
│   ├── analysis.py
│   ├── visualizations.py
│   └── main.py
│
├── visualizations/
│   ├── popular_dishes_plot.png
|   ├── cancellation_trends_plot.png
|   ├── favorite_meals.png
│   └── age_distribution.png
│
├── README.md
└── requirements.txt
```
### 3. Execution
Run the project using the ```main.py``` script:

```
python scripts/main.py
```
### 4. Outputs
  * The cleaned dataset is saved in the data folder.
  * Visualizations are saved in the visualizations folder.

## Key Insights and Recommendations
The following will be covered in the final report:
* 1. **Popular Dishes**: Identify top dishes by the number of orders, ratings, and revenue generated.
* 2. **User Behavior Analysis**: Explore how demographics (age groups, geographic regions) influence cooking preferences and orders.
* 3. **Order Trends**: Investigate seasonal trends or order cancellations to identify improvement opportunities.

#### Business Recommendations:
* Leverage insights into popular dishes to design targeted marketing campaigns.
* Adjust pricing and promotions based on demographic preferences.
* Focus on reducing cancellations by analyzing cancellation trends.

## Dependencies
The project uses the following libraries:
* **pandas**: For data manipulation and cleaning.
* **matplotlib**: For creating visualizations.
* **seaborn**: For advanced visualization styling.

## Contact
For any questions or feedback, please reach out to:
* **Name**: Ankith Goje
* **Email**: ankithgoje25@gmail.com
* **Phone**: +91-8498866536
