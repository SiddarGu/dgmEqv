

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(10,6)) 
ax = fig.add_subplot(111) 

# data
year = [2019,2020,2021]
enrolment = [50,45,43]
graduates = [25,30,32]

# plot
plt.bar(year, enrolment, width=0.3, label='Enrolment', bottom=graduates)
plt.bar(year, graduates, width=0.3, label='Graduates')

# axis
plt.xticks(year, rotation=0, fontsize=12) 
plt.yticks(fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Students (thousands)', fontsize=12)

# legend
plt.legend(loc="upper left")
plt.title('Enrolment and Graduates in Higher Education in 2019-2021', fontsize=14)

# annotate
for x, y in zip(year, enrolment):
    plt.text(x-0.2, y/2, str(y), fontsize=12)
for x, y in zip(year, graduates):
    plt.text(x+0.2, y/2, str(y), fontsize=12)

plt.tight_layout()
plt.savefig(r'Bar Chart/png/125.png')
plt.clf()