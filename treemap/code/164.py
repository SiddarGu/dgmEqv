import plotly.express as px

# Input data given in the question
data_str = """Category,Revenue Share (%)
Accommodation,25
Food Services,20
Travel Agencies,15
Air Travel,15
Recreational Activities,10
Tourism Retail,8
Cultural Attractions,5
Business Events,2"""

# Parsing the input data into three different lists
data_rows = data_str.split('\n')
data_labels = data_rows[0].split(',')[1:]  # Revenue Share (%)
line_labels = [row.split(',')[0] for row in data_rows[1:]]  # Categories
data = [float(row.split(',')[1]) for row in data_rows[1:]]  # Revenue share values

# Creating a DataFrame to hold the processed data
import pandas as pd
df = pd.DataFrame(list(zip(line_labels, data)), columns=["Category", data_labels[0]])

# Create the treemap
fig = px.treemap(df, path=['Category'], values='Revenue Share (%)',
                 title='Revenue Distribution within the Tourism and Hospitality Industry')

# Optional: Customize your treemap colors, layout, etc.
fig.update_traces(textinfo="label+value", textfont_size=20)

# Save the figure
fig.write_image("/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/164.png")
