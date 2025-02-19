#%%
import xarray as xr 

netcdf_file = 'https://opendap1.nodc.no/opendap/physics/point/cruise/nansen_legacy-single_profile/NMDC_Nansen-Legacy_PR_CT_58US_2021708/CTD_station_P1_NLEG01-1_-_Nansen_Legacy_Cruise_-_2021_Joint_Cruise_2-1.nc'
xrds = xr.open_dataset(netcdf_file)
print(xrds)
#%%
# coords are the dimensions of the dataset 
print(xrds.coords)
# %%

# LOADING A VAR into n-d array based on coordinates 
temp_arr = xrds['TEMP'].values
print(temp_arr)
# %%
