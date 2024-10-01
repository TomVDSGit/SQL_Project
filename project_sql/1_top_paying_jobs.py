import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Set the style to dark background
plt.style.use('dark_background')

# Load the CSV data into a pandas DataFrame
csv_file = '/Users/tom/Documents/SQL_Project/csv_files/Q1.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Extract necessary columns: job_title_short and salary_year_avg
# Ensure that salary_year_avg is numeric
data['salary_year_avg'] = pd.to_numeric(data['salary_year_avg'], errors='coerce')

# Group by job title to calculate the average salary for each job_title_short
job_salaries = data.groupby('job_title')['salary_year_avg'].mean().reset_index()

# Truncate job titles to 28 characters
job_salaries['job_title'] = job_salaries['job_title'].apply(lambda x: x[:28] + '...' if len(x) > 28 else x)

# Sort the data by salary and select the top 10 highest-paying jobs
top_10_jobs = job_salaries.sort_values(by='salary_year_avg', ascending=False).head(10)

# Create a color map based on the number of bars
colors = cm.Purples(top_10_jobs['salary_year_avg'] / top_10_jobs['salary_year_avg'].max())

# Plotting the top 10 jobs with colormap
plt.figure(figsize=(10, 6))
plt.barh(top_10_jobs['job_title'], top_10_jobs['salary_year_avg'], color=colors)
plt.xlabel('Average Yearly Salary (USD)', color='white')
#plt.ylabel('Job Title', color='white')
plt.title('Top 10 Data Analyst Jobs by Average Yearly Salary', color='white')
plt.tight_layout()

# Show the plot
plt.show()
