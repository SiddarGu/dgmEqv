
import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots(figsize=(12,7)) 

year = np.array([2020, 2021, 2022, 2023]) 
research_papers = np.array([100, 120, 130, 140]) 
patents = np.array([8, 10, 12, 14]) 
grants = np.array([50, 60, 70, 80]) 

ax.bar(year, research_papers, label="Research Papers", bottom=patents+grants) 
ax.bar(year, patents, label="Patents", bottom=grants) 
ax.bar(year, grants, label="Grants") 

plt.xticks(year) 
plt.title("Science and Engineering Output in four years") 
plt.legend(loc="center left") 

for i in range(len(year)): 
    ax.annotate(f"{research_papers[i] + patents[i] + grants[i]}", 
                xy=(year[i], research_papers[i] + patents[i] + grants[i]), 
                xytext=(-30, 10), 
                textcoords="offset points") 

plt.tight_layout() 
plt.savefig("Bar Chart/png/392.png") 
plt.clf()