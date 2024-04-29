
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7, 5))

age = np.array([18, 19, 20, 21, 22, 23, 24])
happiness = np.array([8, 7, 8, 6, 7, 9, 7])
satisfaction = np.array([6, 7, 6, 9, 7, 5, 7])

plt.plot(age, happiness, label="Happiness Index", color="blue", linestyle="solid")
plt.plot(age, satisfaction, label="Satisfaction Index", color="red", linestyle="dashed")

plt.xticks(age)
plt.xlabel('Age')
plt.ylabel('Index')
plt.title('Happiness and Satisfaction Index of 18-24 year olds')

for a, h, s in zip(age, happiness, satisfaction):
    plt.annotate(str(h), xy=(a, h))
    plt.annotate(str(s), xy=(a, s))

plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig('line chart/png/566.png')
plt.clf()