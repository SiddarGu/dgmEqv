
import matplotlib.pyplot as plt
import matplotlib

# set figure size
plt.figure(figsize=(10,10))

# add subplot
ax = plt.subplot(111)

# set data
Crops = ['Cereal Crops','Vegetables','Fruit','Nuts and Seeds','Dairy Products','Livestock']
Percentage = [50,20,15,7,3,5]

# draw pie chart
ax.pie(Percentage, labels=Crops, autopct='%1.1f%%',startangle=90, textprops={'fontsize': 12})

# set title
ax.set_title('Distribution of Agricultural Production in the USA, 2023', fontsize=20)

# set legend
ax.legend(title='Crops', loc='upper right', bbox_to_anchor=(1.2,0.8))

# prevent the labels from overlapping
matplotlib.rc('xtick', labelsize=10) 
matplotlib.rc('ytick', labelsize=10) 
ax.axis('equal')

# adjust figure
plt.tight_layout()

# save figure
plt.savefig('pie chart/png/125.png')

# clear current image state
plt.clf()