
pip install pandas numpy matplotlib

import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

start_date = data['Date'].iloc[0]
end_date = data['Date'].iloc[-1]

number_of_days = (end_date - start_date).days

date_list = [start_date + datetime.timedelta(days=day) for day in range(number_of_days)]

new_data = pd.DataFrame({'Date': date_list})

x = new_data['Date']
old_x = data['Date']
y = []

for i in range(len(x)):
    x_i = x.iloc[i]
    diff_list = [abs((x_i - old_x.iloc[j]).days) for j in range(len(data))]
    diff_list = np.array(diff_list)
    y.append(data['Close'].iloc[diff_list.argmin()])

plt.figure(figsize=(20,10))
plt.subplot(1,2,1)
plt.title('Original Data',color='red',fontsize=20)
plt.scatter(data['Date'], data['Close'], s=2)
plt.xlabel('Date')
plt.ylabel('Close')

plt.subplot(1,2,2)
plt.title('Smoothed Data',color='navy',fontsize=20)
plt.scatter(x, y, s=2, color='navy')
plt.xlabel('Date')
plt.ylabel('Close')

plt.show()
