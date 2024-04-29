
import matplotlib.pyplot as plt
import numpy as np

# Set font and size
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['font.size'] = 10

# Set figure size
plt.figure(figsize=(12, 6))

# Set data
dates = ['9/1/2019','9/2/2019','9/3/2019','9/4/2019','9/5/2019']
attendance = [12000,13000,14000,15000,16000]
revenue = [20,25,30,35,40]

# Add subplot
a1 = plt.subplot(1, 2, 1)
a2 = plt.subplot(1, 2, 2)

# Plot line chart
a1.plot(dates, attendance, label='Attendance', color='b')
a2.plot(dates, revenue, label='Revenue', color='g')

# Set label
a1.set_xlabel('Date')
a1.set_ylabel('Attendance (people)')
a2.set_xlabel('Date')
a2.set_ylabel('Revenue (million dollars)')

# Set ticks
a1.set_xticks(dates)
a2.set_xticks(dates)

# Add legend
a1.legend()
a2.legend()

# Set title
plt.suptitle('Attendance and revenue changes of a sports event on September 1-5, 2019')

# Annotate
for i in range(len(dates)):
    a1.annotate('{}'.format(attendance[i]), xy=(dates[i], attendance[i]), xytext=(dates[i], attendance[i]+1000))
    a2.annotate('{}'.format(revenue[i]), xy=(dates[i], revenue[i]), xytext=(dates[i], revenue[i]+5))

# Tight layout
plt.tight_layout()

# Save image
plt.savefig('line chart/png/487.png')

# Clear image
plt.clf()