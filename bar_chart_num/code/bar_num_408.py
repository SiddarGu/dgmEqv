
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(9,7))
ax=fig.add_subplot()
month=['January','February','March','April']
crop=[600,650,700,750]
livestock=[400,450,500,550]
p1=ax.bar(month, crop, color='b', label='Crop')
p2=ax.bar(month, livestock, bottom=crop, color='g', label='Livestock')
ax.set_title("Crop and Livestock Production from January to April 2021")
ax.legend()
plt.xticks(month)
for c, l in zip(p1,p2):
    plt.annotate(str(l.get_height()+c.get_height()), (c.get_x() + c.get_width() / 2, c.get_height()+l.get_height()/2), ha='center', va='center', fontsize=10, color='black', rotation=90, xytext=(0, 10),
                 textcoords='offset points')
    plt.annotate(str(c.get_height()), (c.get_x() + c.get_width() / 2, c.get_height()/2), ha='center', va='center', fontsize=10, color='black', rotation=90, xytext=(0, 10),
                 textcoords='offset points')
plt.tight_layout()
plt.savefig('Bar Chart/png/286.png')
plt.clf()