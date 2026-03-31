import pandas as pd

# 1. Sample Data Create Pannuvom (Intha 2026 market trends padi)
data = {
    'Job_Title': ['Data Analyst', 'Python Developer', 'Data Scientist', 'AI Engineer', 'Data Analyst'],
    'Location': ['Coimbatore', 'Bangalore', 'Chennai', 'Bangalore', 'Coimbatore'],
    'Salary_LPA': [5, 8, 12, 15, 6],
    'Skills': ['SQL, Python', 'Python, Django', 'Python, ML', 'GenAI, Python', 'Excel, SQL']
}

df = pd.DataFrame(data)

# 2. Data-va display panna
print("--- Job Market Analysis Data ---")
print(df)

# 3. Average Salary calculate panna
avg_salary = df['Salary_LPA'].mean()
print(f"\nAverage Salary in Market: {avg_salary} LPA")
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Setting the style
sns.set_theme(style="whitegrid")

# 2. Bar Plot: Job Title vs Salary
plt.figure(figsize=(10, 6))
sns.barplot(x='Job_Title', y='Salary_LPA', data=df, palette='viridis')

# 3. Customizing the labels
plt.title('Job Roles vs Salary (2026 Trend)', fontsize=15)
plt.xlabel('Job Role', fontsize=12)
plt.ylabel('Salary in LPA', fontsize=12)

# 4. Show the magic!
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Real-time maari oru CSV file create panrom
raw_data = {
    'Job_Title': ['Data Analyst', 'Python Dev', 'Data Scientist', 'AI Engineer', 'ML Engineer', 'Data Analyst'],
    'Location': ['Coimbatore', 'Bangalore', 'Chennai', 'Bangalore', 'Hyderabad', 'Coimbatore'],
    'Salary_LPA': [5.5, 8.2, 12.5, 15.0, 14.5, 6.0]
}

new_df = pd.DataFrame(raw_data)
new_df.to_csv('my_job_market_project.csv', index=False)
print("CSV File 'my_job_market_project.csv' created successfully!")

# 2. Ippo antha CSV-la irunthu data-va read panni graph varaiyalaam
df_from_file = pd.read_csv('my_job_market_project.csv')

plt.figure(figsize=(10,6))
sns.lineplot(x='Job_Title', y='Salary_LPA', data=df_from_file, marker='o', color='red')
plt.title('Salary Growth Trend - 2026')
plt.show()
