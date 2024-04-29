
import matplotlib.pyplot as plt
import pandas as pd

data = {'Month':['January','February','March','April','May','June','July','August','September','October','November','December'],
        'Wind Power(kW-h)':[500,600,450,550,400,500,550,600,650,550,500,450],
        'Solar Power(kW-h)':[200,150,250,300,350,400,450,500,550,600,550,500],
        'Hydro Power(kW-h)':[800,700,600,900,800,700,600,500,400,500,600,700]}

df = pd.DataFrame(data)

plt.figure(figsize=(12, 8))
plt.subplot()
plt.plot(df['Month'], df['Wind Power(kW-h)'], label='Wind Power(kW-h)',marker='o')
plt.plot(df['Month'], df['Solar Power(kW-h)'], label='Solar Power(kW-h)',marker='o')
plt.plot(df['Month'], df['Hydro Power(kW-h)'], label='Hydro Power(kW-h)',marker='o')
plt.title('Renewable energy consumption in the United States in 2022')
plt.xticks(df['Month'], rotation=45, wrap=True)
plt.xlabel('Month')
plt.ylabel('Energy consumption(kW-h)')
plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/413.png')
plt.clf()