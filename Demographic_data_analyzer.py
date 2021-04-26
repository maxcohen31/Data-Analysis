import pandas as pd

def calculate_demographic_data(print_data = True):

    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    race_count = df.groupby('race')['race'].count()
    
    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1))
    
    # What is the percentage of people who have a Bachelor's degree?
    people_with_bachelor = len(df[df['education'] == 'Bachelors'])
    lenght_of_df = len(df)
    percentage_bachelors = round(people_with_bachelor / lenght_of_df * 100, 1) 
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    num_of_high_ed = higher_education[higher_education['salary'] == '>50K'].count()
    num_of_low_ed = lower_education[lower_education['salary'] == '>50K'].count()
    
    # Percentage with salary > 50K
    higher_education_rich = round(num_of_high_ed / higher_education * 100, 1)
    lower_education_rich = round(num_of_low_ed / lower_education * 100, 1)
    
    # What is the minum numbers of hour a person works per week?
    min_work_hours = df['hour-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hour-per-week'] == min_work_hours]
    rich_percentage = round(len(num_min_workers.salary == '>50K') / len(num_min_workers) * 100, 1)
    
    # What country has the highest percentage of people that earn >50K
    number_of_countries = df.groupby('native-country').count()
    highest_earning_country = df[df['salary'] == '50K'].groupby('native-country').max()
    highest_earning_country_percentage = round(highest_earning_country / number_of_countries * 100, 1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby('occupation')['occupation'].count().max()
    
    
