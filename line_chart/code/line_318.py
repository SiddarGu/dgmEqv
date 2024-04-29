
import matplotlib.pyplot as plt
plt.figure(figsize=(8,6))
plt.plot(['January','February','March','April'],[100,90,120,150],label='Hotel A')
plt.plot(['January','February','March','April'],[120,100,110,160],label='Hotel B')
plt.plot(['January','February','March','April'],[80,110,130,120],label='Hotel C')
plt.plot(['January','February','March','April'],[150,120,140,80],label='Hotel D')
plt.xticks(['January','February','March','April'])
plt.title('Hotel visitors in four cities during the first four months of 2021')
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig('line chart/png/216.png')
plt.clf()