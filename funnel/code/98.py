
import plotly.graph_objects as go
import plotly.io as pio

# Prepare the data
data = [
    dict(type="funnel", 
         y=["Recruitment","Training","Performance Evaluation","Retention","Promotion","Others"],
         x=[100,80,56,42,28,16],
         textinfo="value+percent initial"
         ),
]

# Create the figure
fig = go.Figure(data=data)

# Set the figure size
fig.update_layout(width=1000, height=800,
                  title_text="Employee Management in Human Resources in 2021",
                  font=dict(family="Courier New, monospace", size=18, color="#7f7f7f"))

# Set the chart style and the positioning of the legend
fig.update_traces(marker=dict(line=dict(width=2,color="darkblue")),
                  showlegend=False)

# Set background grid
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')

# Save the figure
pio.write_image(fig, '/cpfs01/user/chenzijun/simchart/datasets/funnel_2023-12-28_18-40-26_simulation_num100/png/33.png')