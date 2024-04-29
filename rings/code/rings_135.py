
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cm
import numpy as np

data_labels = ["Home Prices", "Home Sales", "Construction", "Rental Rates", "Affordability"]
data = [30, 25, 15, 20, 10]
line_labels = ["Category Ratio"]

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()
ax.pie(data, startangle=90, counterclock=False, colors=['#f4a460', '#f5f5dc', '#808080', '#00ced1', '#ee82ee'])
circle = plt.Circle(xy=(0, 0), radius=0.5, color='white')
ax.add_artist(circle)
ax.legend(data_labels, bbox_to_anchor=(0, 0))
plt.title("Real Estate and Housing Market Overview - 2023")
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_90.png')
plt.clf()