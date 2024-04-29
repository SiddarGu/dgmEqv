
import matplotlib.pyplot as plt
data = {'January':[2.5,3.4,2.1],'February':[2.7,3.8,2.2],'March':[2.6,3.5,2.3],'April':[2.5,3.3,2.4],'May':[2.8,3.7,2.5],'June':[2.9,3.9,2.6],'July':[2.7,3.6,2.7],'August':[2.8,4.0,2.8]}
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
for i in data:
    ax.plot(data[i],label=i)
ax.set_title('Prevalence of Diabetes, Hypertension and Obesity in the US in 2021',fontsize=14)
ax.set_xlabel('patients diagnosed with diseases (millions)',fontsize=14)
ax.set_xticks([0,1,2])
ax.set_xticklabels(['Diabetes','Hypertension','Obesity'], fontsize=14,rotation=0)
ax.legend()
plt.tight_layout()
plt.savefig('line chart/png/287.png')
plt.clf()