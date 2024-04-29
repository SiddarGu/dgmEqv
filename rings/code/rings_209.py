
import matplotlib.pyplot as plt 
import numpy as np 

data_labels = ['Mortgage Rates', 'Property Prices', 'Rental Rates', 'House Supply'] 
data = [22, 35, 25, 18] 
line_labels = ['Category', 'Ratio'] 

fig = plt.figure(figsize=(7, 7)) 
ax = fig.add_subplot(111) 
ax.pie(data, labels=data_labels, colors=['red', 'blue', 'green', 'purple'], startangle=90, counterclock=False) 
circle = plt.Circle((0, 0), 0.7, color='white') 
ax.add_artist(circle) 
ax.legend(data_labels, loc='upper left') 
plt.title('Real Estate and Housing Market Overview - 2023', fontsize=15) 
plt.tight_layout() 
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-075221_62.png') 
plt.clf()