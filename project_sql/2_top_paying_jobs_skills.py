import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Set the style to dark background
plt.style.use('dark_background')

# Load the CSV data into a pandas DataFrame
csv_file = '/Users/tom/Documents/SQL_Project/csv_files/Q2.csv'  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

# Count the occurrences of each skill
skill_counts = data['skills'].value_counts().reset_index()
skill_counts.columns = ['skill', 'count']  # Rename the columns for clarity

# Sort by count and select the top 10 skills
top_10_skills = skill_counts.sort_values(by='count', ascending=False).head(10)

# Create a color map based on the number of bars
colors = cm.Purples(top_10_skills['count'] / top_10_skills['count'].max())

# Plotting the skill counts as a bar chart with a colormap
plt.figure(figsize=(10, 6))
plt.barh(top_10_skills['skill'], top_10_skills['count'], color=colors)
plt.xlabel('Number of Occurrences', color='white')
#plt.ylabel('Skills', color='white')
plt.title('Top Skills for Data Analysts by Occurrences', color='white')
plt.tight_layout()

# Show the plot
plt.show()