
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.set_title("Number of Judges, Jurors and Lawyers in four countries in 2021")

country = ['USA', 'UK', 'Germany', 'France']
judges = [1000, 1200, 1500, 1800]
jurors = [4000, 4500, 4800, 5000]
lawyers = [10000, 11000, 12000, 13000]

x_pos = np.arange(len(country))

ax.bar(x_pos + 0.00, judges, width=0.25, color='#EE3224', label='Judges')
ax.bar(x_pos + 0.25, jurors, width=0.25, color='#F78F1E', label='Jurors')
ax.bar(x_pos + 0.50, lawyers, width=0.25, color='#FFC222', label='Lawyers')

plt.xticks(x_pos, country, rotation=0, wrap=True)
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('bar chart/png/175.png')
plt.clf()