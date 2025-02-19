#%%
import xarray as xr 
import matplotlib.pyplot as plt
# %%
import xarray as xr
netcdf_file = 'https://opendap1.nodc.no/opendap/chemistry/point/cruise/nansen_legacy/2021708/Chlorophyll_A_and_phaeopigments_Nansen_Legacy_cruise_2021708_station_P4_NLEG11_20210718T085042.nc'
xrds = xr.open_dataset(netcdf_file)
xrds
# %%
# xarry has some basic matplotlib built into it
xrds['CHLOROPHYLL_A_TOTAL'].plot()
plt.show()

# %%
# drops all values where chlorophyll is missing is dropped
# yincrease decides if the y axis increases from top to bottom or bottom to top
xr.plot.line(xrds['CHLOROPHYLL_A_TOTAL'].dropna('DEPTH'),y='DEPTH',yincrease=False)
plt.show()
# %%

# Set up the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

xrds['CHLOROPHYLL_A_TOTAL'].plot.line(y='DEPTH', yincrease=False, label='TOTAL', ax=axes[0])
xrds['CHLOROPHYLL_A_10um'].plot.line(y='DEPTH', yincrease=False, label='10um', ax=axes[0])
axes[0].set_title('Chlorophyll a')
axes[0].legend()

xrds['PHAEOPIGMENTS_TOTAL'].plot.line(y='DEPTH', yincrease=False, label='TOTAL', ax=axes[1])
xrds['PHAEOPIGMENTS_10um'].plot.line(y='DEPTH', yincrease=False, label='10um', ax=axes[1])
axes[1].set_title('Phaeopigments')
axes[1].legend()

# Adjust layout and display the plot
plt.suptitle('Chlorophyll and Phaeopigments')
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust the layout to avoid overlap
plt.show()
# %%
