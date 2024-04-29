
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
sports = ['Football', 'Basketball', 'Baseball', 'Hockey', 'Tennis', 'Golf', 'Other']
percentage = [30, 25, 15, 10, 10, 5, 5]
plt.pie(percentage, labels=sports, autopct='%1.1f%%', startangle=90, explode=[0.1, 0, 0, 0, 0, 0, 0])
plt.title('Popular Sports in the USA in 2023')
plt.tight_layout()
plt.savefig('pie chart/png/69.png')
plt.clf()