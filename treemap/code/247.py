import plotly.express as px
import os

# Given data
data_labels = ["Research Funding (%)"]
line_labels = ["Biology", "Computer Science", "Engineering", "Physics", "Chemistry", "Earth Sciences", "Mathematics", "Environmental Science"]
data = [18, 17, 16, 15, 12, 10, 7, 5]

# Transform data into a dictionary for creating a DataFrame for use in Plotly
data_dict = {
    'Field': line_labels,
    'Research Funding (%)': data
}

# Create a DataFrame
df = pd.DataFrame(data_dict)

# Creating the treemap
fig = px.treemap(df, path=['Field'], values='Research Funding (%)',
                 title='Allocation of Research Funding by Field in Science and Engineering')

# Update layout for clarity
fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Ensure long labels are clear and not stacked
fig.update_traces(textinfo="label+percent entry", textfont_size=18, textposition='middle center')

# Absolute path to the folder where the image will be saved
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/'
os.makedirs(save_path, exist_ok=True)  # Create directory if it does not exist

# Save the figure
fig.write_image(os.path.join(save_path, "247.png"))

# Clear the current image state if using a system that requires it (e.g., matplotlib)
# Plotly does not require clearing the state
