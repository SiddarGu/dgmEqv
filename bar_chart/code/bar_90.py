
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1, 1, 1)
ax.set_title('Total Production Output of Machinery, Metals, Chemicals, and Textiles in 2021')
Category = ['Machinery','Metals','Chemicals','Textiles']
Production_Output = [3000,4000,6000,5000]
ax.bar(Category, Production_Output, width=0.5, align='center', bottom=0)
ax.set_xticklabels(Category, rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/560.png')
plt.clf()