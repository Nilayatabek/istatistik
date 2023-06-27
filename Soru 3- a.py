import matplotlib.pyplot as plt
import pandas as pd

# Example time series data
uzunluk = ['6-8.', '8-10', '10-12', '12-14', '14-16','16-18','18-20','20-2','22-24','24-26','26-28','28-30','30-35','35-40','40-45']

frekans= [6,23,30,35,32,48,42,40,28,27,26,14,10.8,4.4,0.8]

# Create a pandas dataframe from the time series data
df = pd.DataFrame({'Uzunluk': uzunluk, 'Frekans': frekans})

# Plot the time series data as a bar plot
plt.bar(df['Uzunluk'], df['Frekans'], width=1)
plt.xticks(rotation=90)
plt.show()
