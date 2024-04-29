
import matplotlib.pyplot as plt 
fig = plt.figure(figsize=(8,6)) 
ax = fig.add_subplot() 
ax.plot(['2001', '2002', '2003', '2004', '2005'], [100, 120, 140, 160, 180], 'r', label='Number of Graduates') 
ax.plot(['2001', '2002', '2003', '2004', '2005'], [200, 220, 240, 260, 280], 'b', label='Number of Enrollments') 
ax.set_title('Increase in Enrollment and Graduates in Universities from 2001 to 2005') 
ax.set_xlabel('Year') 
ax.set_ylabel('Number of Enrollments/Graduates') 
ax.legend(loc='upper left', bbox_to_anchor=(1,1)) 
ax.grid(axis='y') 
ax.set_xticks(['2001', '2002', '2003', '2004', '2005']) 
for i,j in zip(['2001', '2002', '2003', '2004', '2005'], [100, 120, 140, 160, 180]):
    ax.annotate(str(j), xy=(i,j), xytext=(-20,10), textcoords='offset points')
for i,j in zip(['2001', '2002', '2003', '2004', '2005'], [200, 220, 240, 260, 280]):
    ax.annotate(str(j), xy=(i,j), xytext=(-20,10), textcoords='offset points')
plt.tight_layout() 
plt.savefig('line chart/png/230.png', bbox_inches='tight') 
plt.clf()