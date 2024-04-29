
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))

x_labels = ['USA', 'UK', 'Germany', 'France']
start_ups = [500, 600, 400, 450]
finance = [3.2, 2.8, 4.0, 2.5]

ax = plt.subplot()
ax.bar(x_labels, start_ups, bottom=0, label='Start-ups')
ax.bar(x_labels, finance, bottom=start_ups, label='Finance Investment(billion)')

ax.set_title('Number of start-ups and finance investments in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize='large')
ax.set_xticklabels(x_labels, rotation=0, wrap=True)

plt.tight_layout()
plt.savefig('bar chart/png/5.png')
plt.clf()