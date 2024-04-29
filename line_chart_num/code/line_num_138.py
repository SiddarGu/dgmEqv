
import matplotlib.pyplot as plt 
import pandas as pd 

# Read data 
data = [[2020, 3000, 400, 90, 3.5], [2021, 3500, 480, 88, 3.9], [2022, 4000, 550, 85, 4.2], [2023, 4500, 620, 82, 4.6]] 
df = pd.DataFrame(data, columns = ['Year', 'Employees (thousands)', 'New Hires (thousands)','Retention Rate (%)', 'Satisfaction Rating']) 

# Create figure and plot
fig = plt.figure(figsize=(10, 6)) 
ax = fig.add_subplot(111)

ax.plot(df['Year'], df['Employees (thousands)'], color ='blue', marker='o', linestyle='solid', label="Employees (thousands)")
ax.plot(df['Year'], df['New Hires (thousands)'], color ='red', marker='o', linestyle='solid', label="New Hires (thousands)")
ax.plot(df['Year'], df['Retention Rate (%)'], color ='green', marker='o', linestyle='solid', label="Retention Rate (%)")
ax.plot(df['Year'], df['Satisfaction Rating'], color ='black', marker='o', linestyle='solid', label="Satisfaction Rating")

for i, txt in enumerate(df['Employees (thousands)']):
    ax.annotate(txt, (df['Year'][i], df['Employees (thousands)'][i]), xytext=(-20, 10), textcoords='offset points')
for i, txt in enumerate(df['New Hires (thousands)']):
    ax.annotate(txt, (df['Year'][i], df['New Hires (thousands)'][i]), xytext=(-20, 10), textcoords='offset points')
for i, txt in enumerate(df['Retention Rate (%)']):
    ax.annotate(txt, (df['Year'][i], df['Retention Rate (%)'][i]), xytext=(-20, 10), textcoords='offset points')
for i, txt in enumerate(df['Satisfaction Rating']):
    ax.annotate(txt, (df['Year'][i], df['Satisfaction Rating'][i]), xytext=(-20, 10), textcoords='offset points')

ax.set_xticks([2020, 2021, 2022, 2023])
ax.set_title('Employee Engagement and Retention Rate at XYZ Company') 
ax.legend()
plt.tight_layout() 

plt.savefig(r'line chart/png/382.png', dpi=300) 
plt.clf()