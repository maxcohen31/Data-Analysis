import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['CSIRO Adjusted Sea Level']
    y = df['Year']
    plt.figure(figsize=(15, 7))
    plt.scatter(x, y)
    
    # Create first line of best fit
    regression = linregress(x, y)
    line_x = pd.Series([x for x in range(1880, 2051)])
    line_y = regression.slope * line_x + regression.intercept
    plt.plot(line_x, line_y, color='red', label='Line 1')
    
    
    # Create second line of best fit
    df_since_2000 = df[df['Year'] >= 2000]
    x1 = df_since_2000['CSIRO Adjusted Sea Level']
    y2= df_since_2000['Year']
    new_regression = linregress(x1, y2)
    line_x1 = pd.Series([x for x in range(2000, 2051)])
    line_x2 = new_regression.slope * line_x1 + new_regression.intercept
    plt.plot(line_x1, line_x2, color='green', label='Line2')
    
    # Add labels and titles
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
       
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

print(draw_plot())