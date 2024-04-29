
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))

ax = plt.subplot()

ax.plot([2001, 2002, 2003, 2004, 2005, 2006], [500, 450, 475, 525, 480, 450], label='Number of Laws Passed')
ax.plot([2001, 2002, 2003, 2004, 2005, 2006], [50, 75, 65, 55, 60, 75], label='Number of Laws Rejected')

ax.annotate('500', xy=(2001, 500))
ax.annotate('50', xy=(2001, 50))
ax.annotate('450', xy=(2002, 450))
ax.annotate('75', xy=(2002, 75))
ax.annotate('475', xy=(2003, 475))
ax.annotate('65', xy=(2003, 65))
ax.annotate('525', xy=(2004, 525))
ax.annotate('55', xy=(2004, 55))
ax.annotate('480', xy=(2005, 480))
ax.annotate('60', xy=(2005, 60))
ax.annotate('450', xy=(2006, 450))
ax.annotate('75', xy=(2006, 75))

ax.legend(loc='upper left')

ax.set_title('Lawmaking activity in the United States from 2001 to 2006')
ax.set_xlabel('Year')
ax.set_ylabel('Laws')

ax.set_xticks([2001, 2002, 2003, 2004, 2005, 2006])

ax.grid(True, ls = '--', color='0.75')

plt.tight_layout()

plt.savefig('line chart/png/404.png')
plt.clf()