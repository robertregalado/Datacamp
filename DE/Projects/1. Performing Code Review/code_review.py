import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def prepare_smartphone_data(file_path):
    """
    To prepare the smartphone data for visualization, a number of transformations 
    will be applied after reading in the raw DataFrame to memory, including:
        - reducing the number of columns to only those needed for later analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount
    
    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """
    
    # Check to see if the path exists, and then return the pandas DataFrame
    if os.path.exists(file_path):
        raw_data = pd.read_csv(file_path)
        
    # Provide a detailed exception if the path does not exist
    else:
        raise Exception(f"File containing smartphone data not found at path {file_path}")

    # Reducing the number of columns to only those needed for later analysis
    feature_set = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]
    clean_data = raw_data.loc[:, feature_set]
    
    # Remove records without a battery_capacity value
    clean_data = clean_data.dropna(subset=["battery_capacity", "os"])
    
    # Divide the price column by 100 to find the dollar amount
    clean_data["price"] = clean_data["price"]/ 100
    
    return clean_data
  

# Call the prepare_smartphone_data function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")


def column_to_label(column_name):
    """
    Converts a column name in a pandas DataFrame to a string that can be
    used as a label in a plot.
    
    :param column_name: string containing original column name
    :return: string that is ready to be presented on a plot
    """
    
    # Validate that column_name is a string
    if isinstance(column_name, str):
        return " ".join(column_name.split("_")).title()
    
    # If the value provided is not a string, raise an Exception
    else:
        raise Exception("Please makes sure to pass a value of type 'str'.")


def visualize_versus_price(clean_data, x):
    """
    Use seaborn and matplotlib to identify a pattern between avg_rating and 
    battery_capacity.
    
    :param clean_data: a pandas DataFrame containing cleaned smartphone data
    :param x: variable to be plotted on the x-axis
    :return: None
    """
    
    # Create an cleaned x label to present on the plot
    x_title = column_to_label(x)
    
    # Create the scatterplot, and add labels and a title
    sns.scatterplot(x=x, y="price", data=clean_data, hue="os")
    
    # Add x and y labels
    plt.xlabel(x_title)
    plt.ylabel("Price ($)")
    
    # Add a title to the plot
    plt.title(f"{x_title} vs. Price")
    

# Call the visualize_versus_price function
visualize_versus_price(cleaned_data, "processor_speed")

# Install required packages
!pip3 install pytest ipytest
import pytest
import ipytest

ipytest.config.rewrite_asserts = True
__file__ = "notebook.ipynb"


# Create a clean DataFrame fixture
@pytest.fixture()
def clean_smartphone_data():
    return prepare_smartphone_data("./data/smartphones.csv")
    
    
def test_nan_values(clean_smartphone_data):
    """
    Test for no NaN value for "battery_capacity" or "os"
    """
    
    # Assert there are no NaN value in "battery_capacity" or "os"
    assert clean_smartphone_data["battery_capacity"].isnull().sum() == 0
    assert clean_smartphone_data["os"].isnull().sum() == 0
    
ipytest.run("-qq")