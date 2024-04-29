

import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.title('Average Height and Weight of People in Different Age Groups')

x_labels = ['0-5','6-10','11-15','16-20','21-25','26-30','31-35','36-40']

heights = [90,115,140,160,175,185,180,170]
plt.plot(x_labels, heights, label='Height')

weights = [10,20,35,50,60,70,75,70]
plt.plot(x_labels, weights, label='Weight')

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)

plt.xticks(x_labels)
plt.grid(True)
plt.tight_layout()

plt.savefig('line chart/png/101.png')
plt.clf()