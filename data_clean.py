import pandas as pd
import numpy as np
#loading dataset
df = pd.read_csv(r'C:\Users\Smita\Downloads\indian_employee_data.csv')
print(df.head())
#checking missing values
print("missing values in each column")
print(df.isnull().sum())
df["salary(INR)"].fillna(df["salary(INR)"].mean(), inplace = True)
df["perf.Rating"].fillna(df["perf.Rating"].median(), inplace = True)
df.replace([np.inf, -np.inf], np.nan, inplace = True)
df.fillna(df.select_dtypes(include = 'number').mean(), inplace = True)
#remove duplicate records
df.drop_duplicates(inplace = True)
#replace negative salaries
df['salary(INR)'] = np.where(df['salary(INR)']< 0 , df['salary(INR)'].mean(), df['salary(INR)'])
salary_mean = df["salary(INR)"].mean()
salary_std = df['salary(INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)

# remove rows where salary is too high or too low
df = df[(df['salary(INR)'] >= lower_bound)]
df = df[(df['salary(INR)'] <= upper_bound)]
df.to_csv('C:/Users/Smita/Downloads/cleaned_indian_employee_data.csv', index= False)
print('data cleaning completed!! saved as "cleaned_indian_employee_data.csv"')

