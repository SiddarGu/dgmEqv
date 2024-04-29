

import matplotlib.pyplot as plt

age = ['18-25','26-35','36-45','46-55','56-65','66-75']
weight = [68,72,77,81,85,87]
height = [170,175,180,185,190,195]
bmi = [21,23,25,27,29,30]

fig = plt.figure(figsize=(10,6))

ax1 = fig.add_subplot(111)
ax1.plot(age,weight,label='Average Weight(kg)')
ax1.plot(age,height,label='Average Height(cm)')
ax1.plot(age,bmi,label='Average BMI')

ax1.set_xticks(age)
ax1.set_xlabel('Age')
ax1.set_ylabel('Average Weight/Height/BMI')
ax1.set_title('Average Health Statistics for Different Age Groups')
ax1.legend(loc=2)
plt.tight_layout()
plt.savefig('line chart/png/502.png')
plt.clf()