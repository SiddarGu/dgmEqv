
import matplotlib.pyplot as plt
import pandas as pd

data = {'Year': [2015, 2016, 2017, 2018, 2019],
        'Number of students enrolled in music classes': [1000, 1200, 1400, 1300, 1500],
        'Number of students enrolled in art classes': [800, 900, 1100, 1200, 1000]}

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)
ax.plot(data['Year'],data['Number of students enrolled in music classes'],label='Music Classes')
ax.plot(data['Year'],data['Number of students enrolled in art classes'],label='Art Classes')
ax.set_xticks([2015,2016,2017,2018,2019])
ax.legend(loc='best')
ax.set_title('Growth of student enrollment in art and music classes from 2015 to 2019')
plt.tight_layout()
plt.savefig('line chart/png/429.png')
plt.clf()