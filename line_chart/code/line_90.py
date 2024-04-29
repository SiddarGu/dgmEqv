
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(['5th','6th','7th','8th','9th','10th','11th','12th'],[90,93,95,97,99,95,93,90],'-o',color='#07499b',label='Average Grade')
plt.plot(['5th','6th','7th','8th','9th','10th','11th','12th'],[100,125,150,175,200,175,150,125],'-o',color='#ffa000',label='Student Enrollment')
plt.title('Average Grade and Student Enrollment in Public School over 7 years')
plt.xlabel('Grade')
plt.ylabel('Average Grade/Student Enrollment')
plt.xticks(['5th','6th','7th','8th','9th','10th','11th','12th'])
plt.legend(loc='upper left',bbox_to_anchor=(1,1))
plt.tight_layout()
plt.savefig('line chart/png/55.png')
plt.clf()