import plotly.express as px
import os

# Data setup
data_labels = ['Expenditure (%)']
line_labels = ['Legislative', 'Judicial', 'Executive', 'Law Enforcement']
data = [25, 35, 15, 25]

# Preparing the DataFrame for Plotly
df = {
    'Legal Branch': line_labels,
    'Expenditure (%)': data
}

# Converting the dictionary to a DataFrame
data_frame = pd.DataFrame(df)

# Creating the treemap
fig = px.treemap(
    data_frame,
    path=['Legal Branch'],
    values='Expenditure (%)',
    title='Allocation of Expenditure Across Legal Branches'
)

# Update the layout to make it fancy as per your specifications
fig.update_layout(
    margin=dict(t=50, l=25, r=25, b=25) # Adjust margins to ensure title and labels fit
)

# Save the figure
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/1052.png"
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure the directory exists
fig.write_image(save_path)

# Clear the current image state (if using Plotly, this step isn't necessary as each figure is independent)
