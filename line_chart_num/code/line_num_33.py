
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(8,5))

# Set data
Year = [2010, 2011, 2012, 2013, 2014]
Number_of_Cases = [10000, 12000, 8000, 15000, 18000]
Number_of_Verdicts = [8000, 9000, 10000, 12000, 14000]
Number_of_Sentences = [6000, 7000, 8000, 9000, 10000]

# Plot line chart
plt.plot(Year, Number_of_Cases, label= 'Number of Cases')
plt.plot(Year, Number_of_Verdicts, label= 'Number of Verdicts')
plt.plot(Year, Number_of_Sentences, label= 'Number of Sentences')

# Set label and title
plt.xlabel('Year')
plt.ylabel('Number')
plt.title('Changes in the Number of Cases, Verdicts and Sentences in US Courts from 2010 to 2014')

# Add grids
plt.grid(True)

# Add legend
plt.legend(loc='best')

# Add xticks
plt.xticks(Year)

# Annotate labels
plt.annotate(str(Number_of_Cases[0]), xy=(Year[0],Number_of_Cases[0]), xytext=(Year[0],Number_of_Cases[0]+1000))
plt.annotate(str(Number_of_Cases[1]), xy=(Year[1],Number_of_Cases[1]), xytext=(Year[1],Number_of_Cases[1]+1000))
plt.annotate(str(Number_of_Cases[2]), xy=(Year[2],Number_of_Cases[2]), xytext=(Year[2],Number_of_Cases[2]+1000))
plt.annotate(str(Number_of_Cases[3]), xy=(Year[3],Number_of_Cases[3]), xytext=(Year[3],Number_of_Cases[3]+1000))
plt.annotate(str(Number_of_Cases[4]), xy=(Year[4],Number_of_Cases[4]), xytext=(Year[4],Number_of_Cases[4]+1000))

plt.annotate(str(Number_of_Verdicts[0]), xy=(Year[0],Number_of_Verdicts[0]), xytext=(Year[0],Number_of_Verdicts[0]+1000))
plt.annotate(str(Number_of_Verdicts[1]), xy=(Year[1],Number_of_Verdicts[1]), xytext=(Year[1],Number_of_Verdicts[1]+1000))
plt.annotate(str(Number_of_Verdicts[2]), xy=(Year[2],Number_of_Verdicts[2]), xytext=(Year[2],Number_of_Verdicts[2]+1000))
plt.annotate(str(Number_of_Verdicts[3]), xy=(Year[3],Number_of_Verdicts[3]), xytext=(Year[3],Number_of_Verdicts[3]+1000))
plt.annotate(str(Number_of_Verdicts[4]), xy=(Year[4],Number_of_Verdicts[4]), xytext=(Year[4],Number_of_Verdicts[4]+1000))

plt.annotate(str(Number_of_Sentences[0]), xy=(Year[0],Number_of_Sentences[0]), xytext=(Year[0],Number_of_Sentences[0]+1000))
plt.annotate(str(Number_of_Sentences[1]), xy=(Year[1],Number_of_Sentences[1]), xytext=(Year[1],Number_of_Sentences[1]+1000))
plt.annotate(str(Number_of_Sentences[2]), xy=(Year[2],Number_of_Sentences[2]), xytext=(Year[2],Number_of_Sentences[2]+1000))
plt.annotate(str(Number_of_Sentences[3]), xy=(Year[3],Number_of_Sentences[3]), xytext=(Year[3],Number_of_Sentences[3]+1000))
plt.annotate(str(Number_of_Sentences[4]), xy=(Year[4],Number_of_Sentences[4]), xytext=(Year[4],Number_of_Sentences[4]+1000))

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/44.png')

# Clear the current image state
plt.clf()