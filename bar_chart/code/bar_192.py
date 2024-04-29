
import matplotlib.pyplot as plt

#create figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

#set title
ax.set_title("Number of high school and college graduates from 2020 to 2023")

#set data
year = [2020, 2021, 2022, 2023]
high_school_graduates = [150, 200, 220, 250]
college_graduates = [250, 300, 320, 350]

#plot chart
ax.bar(year, high_school_graduates, width=0.3, label='High School Graduates', color='#6ea8bc', bottom=0)
ax.bar(year, college_graduates, width=0.3, label='College Graduates', color='#fdc966', bottom=high_school_graduates)

#set grid
ax.grid(linestyle=':')

#set axis ticks
plt.xticks(year)

#add legend
ax.legend(loc='upper center')

#tight layout
plt.tight_layout()

#save the figure
plt.savefig(r'bar_192.png')

#clear figure
plt.clf()