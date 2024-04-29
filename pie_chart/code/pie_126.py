
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(10, 6))

# data
health_insurance = ['Public', 'Private', 'Out-of-Pocket', 'Other']
percentage = [40, 30, 20, 10]

# plotting
plt.title('Distribution of Health Insurance in the USA in 2023')
plt.pie(percentage, labels=health_insurance, autopct='%1.1f%%',
        startangle=90, textprops={'fontsize': 14}, shadow=True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('pie chart/png/160.png')

plt.clf()