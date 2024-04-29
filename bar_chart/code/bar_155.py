
import matplotlib.pyplot as plt
import numpy as np
 
# set up data 
country = ['USA', 'UK', 'Germany', 'France']
social_policies = [15, 14, 12, 13]
economic_policies = [20, 18, 17, 19]
educational_policies = [10, 9, 7, 8]
 
x = np.arange(len(country))  # the label locations
width = 0.2  # the width of the bars
 
# set up figure
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, social_policies, width, label='Social Policies')
rects2 = ax.bar(x, economic_policies, width, label='Economic Policies')
rects3 = ax.bar(x + width, educational_policies, width, label='Educational Policies')
 
# format
ax.set_xticks(x)
ax.set_xticklabels(country, fontsize='large', rotation=0)
ax.set_title('Public policy initiatives in four countries in 2021', fontsize = 'x-large')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fontsize='large', ncol=3)
fig.tight_layout()
 
# save image
plt.savefig('bar chart/png/256.png', bbox_inches='tight')
plt.close()