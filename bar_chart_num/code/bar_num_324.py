
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Manufacturing_Cost = [70, 65, 60, 55]
Manufacturing_Output = [100, 90, 80, 70]

fig, ax = plt.subplots(figsize=(9,6))
ax.bar(Country, Manufacturing_Cost, width=0.4, label='Manufacturing Cost (USD)', color='chocolate')
ax.bar(Country, Manufacturing_Output, width=0.4, bottom=Manufacturing_Cost, label='Manufacturing Output (million)', color='skyblue')

plt.title('Manufacturing Cost and Output of Four Countries in 2021')
plt.xlabel('Country')
plt.ylabel('Amount')
plt.xticks(Country)

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), shadow=True, ncol=2)

for i in range(len(Country)):
    ax.annotate('{}\n{}\n{}'.format(Manufacturing_Cost[i], Manufacturing_Output[i], Manufacturing_Cost[i]+Manufacturing_Output[i]),
                xy=(Country[i], Manufacturing_Cost[i]+Manufacturing_Output[i]/2),
                xytext=(0,-10),
                textcoords='offset points',
                ha='center',
                va='center',
                wrap=True,
                rotation=90)

plt.tight_layout()
plt.savefig('Bar Chart/png/210.png')
plt.clf()