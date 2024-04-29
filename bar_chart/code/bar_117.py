
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(13,7))
ax = fig.add_subplot(111)

age_group = ['0-14','15-29','30-44','45-59','60-74','75+']
medical_services = [500,800,1000,1200,1400,1600]
hospital_visits = [1000,1200,1400,1600,1800,2000]

ax.bar(age_group, medical_services, width=0.4, label='Medical Services')
ax.bar(age_group, hospital_visits, width=0.4, bottom=medical_services, label='Hospital Visits')
ax.set_title('Utilization of medical services and hospital visits by different age groups in 2021')
ax.set_xlabel('Age Group')
ax.set_ylabel('Usage (million)')
ax.legend(loc='upper right')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('bar chart/png/169.png')
plt.clf()