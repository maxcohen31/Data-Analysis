import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['weight'] / ((df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# Normalize data
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['glucos'] = df['glucos'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    
    # Create DataFrame for cat plot using `pd.melt` 
    # using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    # You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'glucos', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = pd.DataFrame(df_cat.groupby(['variable', 'value', 'cardio'])['value']
                          .count()).rename(columns={'value': 'total'}).reset_index()
    
    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    
    #Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) & 
            (df['weight'] <= df['weight'].quantile(0.975))]
                 
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10, 10))             
    
    # Draw the heatmap with 'sns.heatmap()'
    fig = sns.heatmap(corr, annot=True, square=True, fmt='.1f', vmax = .3, center=0, mask=mask, linewidths=1, cbar_kws={'shrink': .5})
    
    
    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig             
        