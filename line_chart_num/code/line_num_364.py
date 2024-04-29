
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(12, 7))

age = ['18-22','23-27','28-32','33-37','38-42','43-47']
average_salary = [35000,45000,55000,60000,65000,70000]
male = [0.4,0.45,0.5,0.4,0.3,0.25]
female = [0.6,0.55,0.5,0.6,0.7,0.75]

plt.plot(age,average_salary,color='blue', label='Average Salary')
plt.plot(age,male,color='green', label='Male')
plt.plot(age,female,color='red', label='Female')

plt.xlabel('Age')
plt.ylabel('Salary')
plt.xticks(np.arange(len(age)), age, rotation=45)
plt.title('Gender pay gap among different age groups in 2020')
plt.legend()

for a,b,c,d in zip(age,average_salary,male,female): 
    plt.annotate('Avg: {}\nMale:{}\nFemale:{}'.format(b,c,d),  xy=(a, b), xytext=(0, 5), textcoords='offset points',rotation=45, va='bottom')

plt.tight_layout()
plt.savefig('line chart/png/141.png')
plt.clf()