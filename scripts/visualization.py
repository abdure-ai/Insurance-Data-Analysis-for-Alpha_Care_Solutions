import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Data Visualization Functions
def plot_distributions(df, columns):
    """
    Plots the distribution of numerical columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list): List of numerical columns to plot
    """
    for col in columns:
        sns.histplot(df[col], kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

def plot_correlations(df):
    """
    Plots the correlation heatmap of the dataset.

    Parameters:
        df (pd.DataFrame): Input DataFrame
    """
    corr = df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()
def plot_categorical_distributions(df, columns):
    """
    Plots bar charts for categorical columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list): List of categorical columns to plot
    """
    for col in columns:
        sns.countplot(data=df, x=col, order=df[col].value_counts().index)
        plt.title(f"Frequency of {col}")
        plt.xticks(rotation=45)
        plt.show()
def plot_bivariate_relationships(df, x, y, hue=None):
    """
    Plots scatter plots to analyze relationships between two variables.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        x (str): X-axis variable
        y (str): Y-axis variable
        hue (str, optional): Variable for color encoding
    """
    sns.scatterplot(data=df, x=x, y=y, hue=hue)
    plt.title(f"{y} vs {x}")
    plt.show()
def plot_trends_over_geography(df, region_column, feature_column):
    """
    Compares trends in a feature across different geographical regions.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        region_column (str): Column representing regions (e.g., ZipCode or Province)
        feature_column (str): Feature to analyze trends for
    """
    grouped = df.groupby(region_column)[feature_column].mean().sort_values()
    grouped.plot(kind='bar', figsize=(10, 5), color='skyblue')
    plt.title(f"Average {feature_column} by {region_column}")
    plt.ylabel(feature_column)
    plt.xlabel(region_column)
    plt.xticks(rotation=45)
    plt.show()
def plot_outliers(df, columns):
    """
    Uses box plots to detect outliers in numerical columns.
    
    Parameters:
        df (pd.DataFrame): Input DataFrame
        columns (list): List of numerical columns to analyze
    """
    for col in columns:
        sns.boxplot(data=df, y=col)
        plt.title(f"Outliers in {col}")
        plt.show()
