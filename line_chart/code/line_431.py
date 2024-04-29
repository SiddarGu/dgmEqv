
import matplotlib.pyplot as plt
import numpy as np

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September']
attendance = [7500, 8000, 7000, 6500, 8500, 9000, 8400, 7200, 7600]
reviews = [3.2, 3.8, 3.4, 3.9, 3.5, 3.6, 3.7, 3.3, 3.4]

plt.figure(figsize=(15,7))
plt.plot(month, attendance, marker='o', color='blue', label='Attendance')
plt.plot(month, reviews, marker='*', color='red', label='Ratings')

plt.xticks(np.arange(len(month)), month, rotation=45, wrap=True)
plt.title('Attendance and Ratings of Art Exhibition in 2020')
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/157.png')
plt.clf()