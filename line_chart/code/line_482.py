
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
ax = plt.subplot()
plt.plot(['2001', '2002', '2003', '2004', '2005'], [5, 6, 7, 4, 8], color='blue', label='Music Album Sales(million copies)')
plt.plot(['2001', '2002', '2003', '2004', '2005'], [15, 16, 18, 20, 17], color='red', label='Movie Ticket Sales(million tickets)')
plt.plot(['2001', '2002', '2003', '2004', '2005'], [10, 12, 14, 9, 11], color='green', label='Book Sales(million copies)')
plt.title('Changes in Popular Arts & Culture Consumption from 2001 to 2005')
ax.set_xticks(['2001', '2002', '2003', '2004', '2005'])
ax.set_xlabel('Year')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()
plt.savefig('line chart/png/132.png')
plt.clf()