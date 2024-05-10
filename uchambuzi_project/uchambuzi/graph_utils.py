import os
import matplotlib.pyplot as plt
import seaborn as sns

def generate_scatterplot(df, x_column, y_column):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=x_column, y=y_column, data=df)
    plt.title(f'Scatterplot of {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plot_filename = f'scatter_{x_column}_{y_column}.png'
    plot_filepath = os.path.join('media', 'eda_plots', plot_filename)
    plt.savefig(plot_filepath)
    plt.close()
    return plot_filename

def generate_histogram(df, column):
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plot_filename = f'histogram_{column}.png'
    plot_filepath = os.path.join('media', 'eda_plots', plot_filename)
    plt.savefig(plot_filepath)
    plt.close()
    return plot_filename

def generate_boxplot(df, column):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=column, data=df)
    plt.title(f'Boxplot of {column}')
    plt.xlabel(column)
    plt.ylabel('Value')
    plot_filename = f'boxplot_{column}.png'
    plot_filepath = os.path.join('media', 'eda_plots', plot_filename)
    plt.savefig(plot_filepath)
    plt.close()
    return plot_filename
