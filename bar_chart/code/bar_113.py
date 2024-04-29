
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9,5))
ax = fig.add_subplot()

data = [['USA', 500, 7500, 50000],
        ['UK', 400, 6500, 40000],
        ['Germany', 450, 7000, 45000],
        ['France', 550, 8000, 50000]]

x = np.arange(4)
hospital = [i[1] for i in data]
medical = [i[2] for i in data]
patients = [i[3] for i in data]

bar_width = 0.25
plt.bar(x, hospital, width=bar_width, label="Hospitals")
plt.bar(x + bar_width, medical, width=bar_width, label="Medical Staff")
plt.bar(x + bar_width * 2, patients, width=bar_width, label="Patients")

plt.xticks(x + bar_width, [i[0] for i in data], rotation=45, wrap=True)
plt.title("Healthcare resources and patient numbers in four countries in 2021")
plt.legend(bbox_to_anchor=(1,1))

plt.tight_layout()
plt.savefig('bar_113.png')
plt.clf()