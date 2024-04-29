
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#  Set up a figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot()

#  Data
Levels = ['Primary', 'Secondary', 'Tertiary', 'Non-Formal']
Percentage = [25, 35, 30, 10]

#  Pie chart
ax.pie(Percentage, labels=Levels, 
       autopct='%1.1f%%', pctdistance=0.9, labeldistance=1.2,
       startangle=90, rotatelabels=True,
       colors=['lightcoral', 'coral', 'orangered', 'darkorange'])

#  Legend
patches = [mpatches.Patch(color=color, label=label) for label, color in zip(Levels, ['lightcoral', 'coral', 'orangered', 'darkorange'])]
ax.legend(handles=patches, loc='upper left', bbox_to_anchor=(0.2,0.3))

#  Set title
ax.set_title('Distribution of Education Levels in the USA in 2023')

#  Tight layout to prevent content from being displayed
plt.tight_layout()

#  Save the figure
fig.savefig('pie chart/png/522.png')

#  Clear the current image state
plt.clf()