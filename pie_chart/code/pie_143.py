
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(1, 1, 1)

labels = ['18-24','25-34','35-44','45-54','55-64','65+']
sizes = [25,20,15,20,15,5]
explode = (0.1, 0, 0, 0, 0, 0)

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title('Distribution of the US Population by Age Group in 2023')
ax.legend(bbox_to_anchor=(1.3, 1))

plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/418.png',dpi=500)
plt.clf()