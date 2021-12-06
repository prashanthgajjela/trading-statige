from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

go = pd.read_csv(r"C:\Users\gourishankar\OneDrive\Desktop\pands\chintu.csv")

go = go.set_index(pd.DatetimeIndex(go["datetime"].values))

# creating 25days simple moving 
go['25_sma'] = go['close'].rolling(window= 25, min_periods= 1).mean()

# creating 55days simple moving 
go['55_sma'] = go['close'].rolling(window= 55, min_periods= 1).mean()

go['Signal'] = 0.0
go['Signal'] = np.where(go['25_sma']>go['55_sma'],1.0,0.0)

go['Position'] = go['Signal'].diff()

plt.figure(figsize=(10,5))

#plot closing price , long term and short term price average
go['close'].plot(color = 'm', label= "closeprice")
go['25_sma'].plot(color='b',label='25-days')
go['55_sma'].plot(color='g',label='55-days')

#buy
plt.plot(go[go['Position']==1].index,go['25_sma'][go['Position']==1],'^', markersize=10 ,color='g',label='Buy')
#sell
plt.plot(go[go['Position']==-1].index,go['25_sma'][go['Position']==1], 'v', markersize=10 ,color='r',label='Sell')

plt.xlabel("date")
plt.ylabel("Price in rupess ")
plt.title('HINDALCO',fontsize=20,)

plt.legend()
plt.grid()
print(go.head())
#print(go)
print(plt.show())