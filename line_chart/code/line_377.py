

import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(15, 10)) 
ax = fig.add_subplot(111) 
ax.plot(['2018','2019','2020','2021','2022'],[20,25,30,35,40],label='Attendance at Music Concerts (million people)',linewidth=3)
ax.plot(['2018','2019','2020','2021','2022'],[10,12,14,16,18],label='Attendance at Art Exhibitions (million people)',linewidth=3)
ax.plot(['2018','2019','2020','2021','2022'],[15,17,16,18,20],label='Attendance at Theatre Performances (million people)',linewidth=3)
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
ax.set_title("Change in Attendance at Arts and Cultural Events from 2018 to 2022")
ax.set_xticks(['2018','2019','2020','2021','2022'])
ax.set_xlabel('Year')
ax.set_ylabel('Attendance (million people)')
plt.tight_layout()
plt.savefig('line chart/png/461.png')
plt.clf()