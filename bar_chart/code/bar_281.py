
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot()
country = ['USA', 'UK', 'Germany', 'France']
criminal_cases = [25000, 30000, 28000, 27000]
civil_cases = [100000, 105000, 110000, 107000]
plt.bar(country, criminal_cases, bottom=civil_cases, color='#FF8C00', label='Criminal Cases')
plt.bar(country, civil_cases, color='#1E90FF', label='Civil Cases')
plt.title('Number of criminal and civil cases in four countries in 2021')
plt.xlabel('Country')
plt.ylabel('Number of Cases')
plt.xticks(country, rotation=45, wrap=True)
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/26.png')
plt.clf()