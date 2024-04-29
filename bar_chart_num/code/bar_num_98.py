
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

region = ['North America', 'South America', 'Europe', 'Asia']
doctors = [20, 15, 25, 18]
hospitals = [10, 12, 14, 16]
patients = [500, 400, 600, 550]

# plot the data
p1 = ax.bar(region, doctors, color='red')
p2 = ax.bar(region, hospitals, color='blue', bottom=doctors)
p3 = ax.bar(region, patients, color='green', bottom=[x + y for x,y in zip(doctors, hospitals)])

# set the title
ax.set_title('Number of doctors, hospitals, and patients by region in 2021')

# add legend
ax.legend((p1[0], p2[0], p3[0]), ('Doctors', 'Hospitals', 'Patients'))

# auto adjust the subplot parameters to give specified padding
plt.tight_layout()

# show the values of each bar
for i, v in enumerate(patients):
    ax.text(i, v+50, str(v), color='black', va='center', fontweight='bold', rotation=90)

# set ticks for x-axis
plt.xticks(region, rotation=45)

# save the figure
plt.savefig('Bar Chart/png/55.png')

# clear current figure
plt.clf()