
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))

x = [2015, 2016, 2017, 2018, 2019, 2020]
y1 = [100, 120, 140, 160, 170, 150]
y2 = [200, 180, 220, 240, 220, 210]
y3 = [300, 220, 280, 320, 290, 280]
y4 = [400, 380, 370, 360, 350, 340]

plt.plot(x, y1, label='Wheat Yield(tons)')
plt.plot(x, y2, label='Rice Yield(tons)')
plt.plot(x, y3, label='Corn Yield(tons)')
plt.plot(x, y4, label='Soybean Yield(tons)')

plt.title('Crop Yields in the US from 2015 to 2020')
plt.xlabel('Year')
plt.ylabel('Yields (tons)')
plt.xticks(x, rotation=45)
plt.grid(True)
plt.legend(bbox_to_anchor=(1.0,1.0))

for a,b in zip(x, y1):
    plt.annotate(str(b),xy=(a,b),xytext=(a,b+10))
for a,b in zip(x, y2):
    plt.annotate(str(b),xy=(a,b),xytext=(a,b+10))
for a,b in zip(x, y3):
    plt.annotate(str(b),xy=(a,b),xytext=(a,b+10))
for a,b in zip(x, y4):
    plt.annotate(str(b),xy=(a,b),xytext=(a,b+10))

plt.tight_layout()
plt.savefig('line chart/png/266.png')
plt.clf()