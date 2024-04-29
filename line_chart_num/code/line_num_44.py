
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(['USA', 'Canada', 'Germany', 'France'], [45, 50, 67, 45], label='Donation A(million dollars)', marker='o')
ax.plot(['USA', 'Canada', 'Germany', 'France'], [67, 78, 45, 78], label='Donation B(million dollars)', marker='D')
ax.plot(['USA', 'Canada', 'Germany', 'France'], [34, 35, 89, 34], label='Donation C(million dollars)', marker='*')
ax.plot(['USA', 'Canada', 'Germany', 'France'], [89, 97, 34, 87], label='Donation D(million dollars)', marker='s')
ax.legend(loc='upper left')

for i, txt in enumerate(['USA', 'Canada', 'Germany', 'France']):
    ax.annotate(txt, (['USA', 'Canada', 'Germany', 'France'][i], [45, 50, 67, 45][i]))
    ax.annotate(txt, (['USA', 'Canada', 'Germany', 'France'][i], [67, 78, 45, 78][i]))
    ax.annotate(txt, (['USA', 'Canada', 'Germany', 'France'][i], [34, 35, 89, 34][i]))
    ax.annotate(txt, (['USA', 'Canada', 'Germany', 'France'][i], [89, 97, 34, 87][i]))

ax.set_xticks(['USA', 'Canada', 'Germany', 'France'])
ax.set_title('International donations to charity and nonprofit organizations in 2020')
plt.tight_layout()
plt.savefig('line chart/png/153.png')
plt.clf()