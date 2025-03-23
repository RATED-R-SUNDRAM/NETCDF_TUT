#%%

import pandas as pd
import xarray as xr 
import numpy as np
# %%
# creating a netcdf dataframe using xr.Dataset

depth =[10+i for i in range(0,100,10)]
latitude= [30,60,90,100]
longitude= [20,40,60,80,100]

xrds = xr.Dataset(
    coords ={
        'depth':depth,
        'latitude':latitude,
        'longitude':longitude
    }
)
print(xrds)
# %%

pressure =[100+i for i in range(0,100,10)]
xrds['pressure']= ('depth',pressure)
xrds['temperature']=(['latitude','longitude'],np.random.randint(len(latitude),size=(len(latitude),len(longitude))))
check1=xrds[['temperature']].to_dataframe()
check1
# %%
xrds.to_netcdf("test.nc")
#