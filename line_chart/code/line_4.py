
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))

Year = [2000, 2001, 2002, 2003, 2004]
Criminal_Cases_Filed = [1000, 1200, 1400, 1300, 1100] 
Criminal_Cases_Closed = [850, 1000, 1300, 1200, 1000]
Civil_Cases_Filed = [900, 1100, 1200, 1100, 1000] 
Civil_Cases_Closed = [800, 900, 1000, 900, 800]

plt.plot(Year, Criminal_Cases_Filed, label='Criminal Cases Filed', marker='o', linestyle='-.')
plt.plot(Year, Criminal_Cases_Closed, label='Criminal Cases Closed', marker='o', linestyle='-')
plt.plot(Year, Civil_Cases_Filed, label='Civil Cases Filed', marker='o', linestyle='-.')
plt.plot(Year, Civil_Cases_Closed, label='Civil Cases Closed', marker='o', linestyle='-')
plt.xticks(Year, rotation=45)
plt.title('Change in the number of cases filed and closed in the US between 2000 and 2004')
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/397.png')
plt.clf()