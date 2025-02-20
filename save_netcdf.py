#%%
import pandas as pd 
import xarray as xr
import datetime as dt
# %%
netcdf_file = 'https://opendap1.nodc.no/opendap/physics/point/cruise/nansen_legacy-single_profile/NMDC_Nansen-Legacy_PR_CT_58US_2021708/CTD_station_P1_NLEG01-1_-_Nansen_Legacy_Cruise_-_2021_Joint_Cruise_2-1.nc'
xrds = xr.open_dataset(netcdf_file)
xrds
# %%

# .values writes to numpy arrray
# .to_dataframe() writes to pandas dataframe
df=xrds[['TEMP', 'PSAL', 'PRES']].to_dataframe()
print(df.columns) #Index(['PRES', 'TEMP', 'PSAL'], dtype='object')
df=df.reset_index() # all the coords are in index
print(df.columns) #Index(['PRES', 'TEMP', 'PSAL'], dtype='object')
#df.to_csv(r"")
# %%
# 3d array
xrds = xr.open_dataset('https://opendap1.nodc.no/opendap/physics/point/cruise/nansen_legacy/NMDC_Nansen-Legacy_PR_CT_58US_2022702.nc')
xrds
# %%
# method ='nearest' in sel uses the nearest value provided
time = dt.datetime(2020,12,1)
df=xrds[['TEMP', 'PSAL', 'PRES']].sel(TIME=time, method='nearest').to_dataframe().reset_index()
df.head()
# %%
xrds.coords
# %%
