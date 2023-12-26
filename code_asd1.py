import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """
    Load the dataset from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: The loaded dataset.
    """
    return pd.read_csv(file_path)

def create_and_show_plot(data, plot_type, x_col=None, y_col=None):
    """
    Create and display a specified type of plot using Seaborn and Matplotlib.

    Parameters:
    - data (pd.DataFrame): The dataset.
    - plot_type (str): The type of plot to create ('line', 'scatter', 'histogram', 'box', 'pie', 'bar').
    - x_col (str): The column for the x-axis (required for scatter and box plots).
    - y_col (str): The column for the y-axis (required for scatter and box plots).
    """
    plt.figure(figsize=(8, 6))

    if plot_type == 'line':
        plt.plot(data['Availability'])
        plt.title('Line Plot of Availability')
        plt.xlabel('Index')
        plt.ylabel('Availability')

    elif plot_type == 'scatter':
        plt.scatter(data[x_col], data[y_col])
        plt.title(f'Scatter Plot of {x_col} vs {y_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)

    elif plot_type == 'histogram':
        plt.hist(data['Stock levels'], bins=20)
        plt.title('Histogram of Stock Levels')
        plt.xlabel('Stock levels')
        plt.ylabel('Frequency')

    elif plot_type == 'box':
        sns.boxplot(x=data[x_col], y=data[y_col])
        plt.title(f'Box Plot of {y_col} by {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)

    elif plot_type == 'pie':
        data[x_col].value_counts().plot.pie(autopct='%1.1f%%')
        plt.title(f'Pie Chart of {x_col}')
        plt.ylabel('')

    elif plot_type == 'bar':
        data[x_col].value_counts().plot(kind='bar')
        plt.title(f'Bar Chart of {x_col}')
        plt.xlabel(x_col)
        plt.ylabel('Count')
        plt.xticks(rotation=45)

    plt.show()

# Load the dataset
file_path = r'C:\Users\anilk\Downloads\Desktop\supply_chain_data.csv'
data = load_data(file_path)

# Plotting examples
create_and_show_plot(data, 'line')
create_and_show_plot(data, 'scatter', x_col='Number of products sold', y_col='Revenue generated')
create_and_show_plot(data, 'histogram')
create_and_show_plot(data, 'box', x_col='Shipping carriers', y_col='Shipping costs')
create_and_show_plot(data, 'pie', x_col='Customer demographics')
create_and_show_plot(data, 'bar', x_col='Supplier name')