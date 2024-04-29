import plotly.express as px

# Given data
dataset = {
    "HR Category": [
        "Talent Acquisition",
        "Training and Development",
        "Employee Relations",
        "Performance Management",
        "Compensation and Benefits",
        "Diversity and Inclusion",
        "Workplace Safety",
        "HR Compliance"
    ],
    "Percentage (%)": [
        20, 18, 15, 15, 14, 10, 5, 3
    ]
}

# Transforming the data into three variables
data_labels = ['Percentage (%)']
line_labels = dataset['HR Category']
data = dataset['Percentage (%)']

# Creating a DataFrame
import pandas as pd

df = pd.DataFrame({'HR Category': line_labels, 'Percentage': data})

# Creating treemap
fig = px.treemap(df, path=['HR Category'], values='Percentage',
                 title='Human Resources Management: Key Focus Areas in Employee Lifecycle Management')

fig.update_traces(textinfo="label+percent entry", textfont_size=18)
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/220.png'
fig.write_image(save_path)

# Clear the current image state if using matplotlib
# This step is not required for plotly as it does not maintain state in the same manner.
