
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
labels = ['18-24','25-34','35-44','45-54','55-64','65+']
sizes = [17,25,21,16,15,6]
explode = (0, 0, 0, 0, 0, 0.1)
plt.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%',shadow=True,startangle=90)
plt.title("Population Distribution by Age Group in the USA, 2023")
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/118.png')
plt.clf()