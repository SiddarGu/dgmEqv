
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
labels = ['Automotive', 'Electronics', 'Industrial Machinery', 'Food & Beverage', 'Chemicals', 'Textiles', 'Plastics', 'Metals', 'Other']
sizes = [30,20,15,10,10,10,5,5,5]
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.title("Distribution of Manufacturing and Production Output in 2023")
plt.xticks(rotation=90, wrap=True)
plt.tight_layout()
plt.savefig('pie chart/png/175.png')
plt.clf()