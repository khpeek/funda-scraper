import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_json('amsterdam_sold_geo_4pp.json')
df.reset_index(drop = True)

df['price per unit area'] = df['price'] / df['area']

df['postdate']=pd.to_datetime(df['posting_date'], dayfirst = True)
df['saledate']=pd.to_datetime(df['sale_date'], dayfirst = True)

df['time_to_sell'] = df['saledate'] - df['postdate']

dfp=df[df['price'] > 50000]
dfp['days_to_sell'] = dfp['time_to_sell'].apply(lambda x: x.days)
dfp=dfp[dfp['days_to_sell']>0]

dfp_week = dfp.groupby(pd.TimeGrouper(key='saledate', freq='W')).mean()

fig, (ax1,ax2) = plt.subplots(2, sharex = True)
ax1.scatter(dfp['saledate'].values, dfp['price']/1000.0, s=10)
ax1.plot_date(dfp_week.index, dfp_week['price']/1000.0, 'r-', linewidth = 2)
ax1.set_xlim([datetime.datetime(2015,4,1), datetime.datetime(2016,8,1)])
ax1.set_xlabel('Date of sale')
ax1.set_ylabel(u'Asking price (1,000 EUR)')
ax1.set_title('Property sales in Amsterdam')
ax1.set_ylim([0,800])
ax1.grid('on')

ax2.scatter(dfp['saledate'].values,dfp['days_to_sell'].values, s=10)
ax2.plot_date(dfp_week.index, dfp_week['days_to_sell'].values,'r-', linewidth = 2)
ax2.set_xlabel('Date of sale')
ax2.set_ylabel('Days on the market')
ax2.set_ylim([0,300])
ax2.grid('on')

fig.autofmt_xdate()

plt.show(block = False)





# plt.show()

# df.to_json('amsterdam_sold_geo_4pp_dates.json')

# plt.scatter(df['longitude_4pp'], df['latitude_4pp'], c=df['price per unit area'])
# plt.axis('equal')
# plt.show()

# df_by_4pp = df.groupby('postal_code_4pp').mean()
#
# new_df = pd.DataFrame()
# new_df['lat'] = df_by_4pp['latitude_4pp'].values
# new_df['lon'] = df_by_4pp['longitude_4pp'].values
# new_df['price_per_unit_area'] = df_by_4pp['price per unit area'].values
#
# new_df=new_df[new_df['lat'].notnull()]

# plt.figure()
# plt.scatter(new_df['lon'],new_df['lat'],c=new_df['price_per_unit_area'])
# plt.axis('equal')

# plt.figure()
# plt.scatter(df['price'],df['time_to_sell'])

# dfp = df[df['price']>50000]

# fig, ax = plt.subplots()
# ax.scatter(dfp['area'],dfp['price']/1000.0,c=dfp['latitude_4pp'])
# ax.set_title('Price per unit area colored by latitude')

# fig.colorbar()


# new_df.to_csv('coords_4pp_and_price_per_unit_area4.csv', index=False)

# plt.show()
