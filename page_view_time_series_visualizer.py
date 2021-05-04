import pandas
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025))) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.figure(figsize=(6, 3))
    ax.plot(df.index, df['value'], 'r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar_grouped = df_bar.groupby(["year","month"])["value"].mean().unstack()

    # Draw bar plot
    fig = df_bar_grouped.plot.bar(figsize=(10, 7), xlabel='Years', ylabel='Average Page Views', legend=True)
    fig.figure()
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'Semptember', 'October', 'Nobember', 'December'])
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(3, 3)
    sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0]).set(xlabel='Year',ylabel='Page Views')
    sns.boxplot(x=df_box['month'], y=df_box['value'], order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], ax=axes[1]).set(xlabel='Month',ylabel='Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
      