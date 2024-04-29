import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import io

# Given data
data = """
Subject,Number of Students,Research Funding (Million $),Global Ranking,Job Prospects (Score)
Psychology,20000,1.2,15,85
Philosophy,15000,0.9,20,80
Sociology,18000,1.3,10,90
History,16000,1.4,18,87
Anthropology,14000,0.8,22,82
Linguistics,17000,1,17,83
Literature,13000,0.6,25,79
"""

# Transforming the data into a DataFrame
df = pd.read_csv(io.StringIO(data))
data = df.to_numpy()

# Data labels and line labels
data_labels = df.columns[1:]
line_labels = list(df.iloc[:, 0] + ' ' + df.iloc[:, 2].astype(str))

# Create figure and add subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Scatter plot
norm = plt.Normalize(data[:, 3].min(), data[:, 3].max())
sm = plt.cm.ScalarMappable(cmap="Blues", norm=norm)
sm.set_array([])

for i, line_label in enumerate(line_labels):
    ax.scatter(data[i, 1], data[i, 2], c=plt.cm.Blues(norm(data[i, 3])),
               s=(600+(data[i, 2]-data[:, 2].min())/(data[:, 2].max()-data[:, 2].min())*4400), label=None)
    ax.scatter([], [], c=plt.cm.Blues(norm(data[i, 3])), s=20, label=line_label)

ax.grid(True)
plt.colorbar(sm, label=data_labels[3])
ax.legend(title=data_labels[2], loc='best')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.title('Analysis of Different Disciplines in Social Sciences and Humanities')
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/188_202312310045.png')
plt.clf()
