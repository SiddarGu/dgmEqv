
import matplotlib.pyplot as plt
data_labels = ['Donations', 'Fundraising', 'Volunteering', 'Administrative Costs', 'Research and Development']
data = [35, 25, 15, 15, 10]
line_labels = ['Category', 'ratio']

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
ax.pie(data, labels=data_labels, startangle=90, counterclock=False, colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
inner_circle = plt.Circle((0,0), 0.70, color='white')
ax.add_artist(inner_circle)
plt.title('Nonprofit Organization Performance - 2023', fontname='Helvetica')
ax.legend(data_labels, loc='upper right', bbox_to_anchor=(1, 0.9))
plt.grid(True, axis='y')
plt.tight_layout()
plt.savefig('/cpfs01/user/yanxiangchao/code0/gpt_chart/structchart_simulation/simulated_data_corner_cases/rings/png/20231227-021402_140.png')
plt.clf()