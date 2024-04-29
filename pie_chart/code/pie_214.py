
import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))
gender_list = ["Women", "Men", "Non-binary", "Other"]
percentage_list = [50, 45, 2, 3]
plt.pie(percentage_list, labels=gender_list, autopct='%1.1f%%', textprops={'fontsize': 14},
        shadow=True, startangle=90, rotatelabels=True, pctdistance=0.7)
plt.title("Gender Distribution in the USA in 2021", fontsize=20)
plt.tight_layout()
plt.savefig('pie chart/png/15.png')
plt.clf()