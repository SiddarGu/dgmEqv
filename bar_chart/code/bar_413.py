
import matplotlib.pyplot as plt
import numpy as np

age = np.arange(4)
Patients_thousands = [200,500,800,400]
Treatment_Cost_billion = [1.2,3.5,5.2,2.8]

plt.figure(figsize=(10,6))
ax = plt.subplot(1,1,1)
ax.bar(age,Patients_thousands,bottom=0,width=0.2,label='Patients(thousands)')
ax.bar(age+0.2,Treatment_Cost_billion,bottom=0,width=0.2,label='Treatment Cost(billion)')
ax.set_xticks(age)
ax.set_xticklabels(('0-17','18-35','36-55','55+'))
ax.set_title('Number of patients and treatment cost in four age groups in 2021')
ax.legend()
plt.tight_layout()
plt.savefig('bar chart/png/168.png')
plt.clf()