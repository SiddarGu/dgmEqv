
import matplotlib.pyplot as plt
import numpy as np

# data
Country = ['USA', 'UK', 'Germany', 'France']
Literature = [100, 120, 140, 160]
Philosophy = [150, 170, 190, 210]
History = [200, 220, 240, 260]

# create figure
fig, ax = plt.subplots(figsize=(15, 8))

# plot
width = 0.2
x = np.arange(len(Country))
ax.bar(x - width, Literature, width, label='Literature')
ax.bar(x, Philosophy, width, label='Philosophy')
ax.bar(x + width, History, width, label='History')

# labels
ax.set_title('Number of publications in Social Sciences and Humanities in four countries in 2021')
ax.set_xticks(x)
ax.set_xticklabels(Country)
ax.legend()

# annotate
for i, j in enumerate(Literature):
    ax.annotate(str(j), xy=(i - width, j + 5))
for i, j in enumerate(Philosophy):
    ax.annotate(str(j), xy=(i, j + 5))
for i, j in enumerate(History):
    ax.annotate(str(j), xy=(i + width, j + 5))

# adjust
plt.tight_layout()

# save
plt.savefig('Bar Chart/png/51.png')

# clear
plt.clf()