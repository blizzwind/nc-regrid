import netCDF4
import numpy as np

def nc_regrid(target,target_lat,target_lon,target_val,refer,refer_lat,refer_lon,interp):
  if np.array(netCDF4.Dataset(target)[target_lat]).ndim == 1 or np.array(netCDF4.Dataset(target)[target_lon]).ndim == 1:
    t_lat = np.empty([len(netCDF4.Dataset(target)[target_lat]),len(netCDF4.Dataset(target)[target_lon])])
    t_lon = np.empty([len(netCDF4.Dataset(target)[target_lat]),len(netCDF4.Dataset(target)[target_lon])])
    for i in range(len(netCDF4.Dataset(target)[target_lat])):
      for j in range(len(netCDF4.Dataset(target)[target_lon])):
        t_lat[i][j] = np.array(netCDF4.Dataset(target)[target_lat])[i]
        t_lon[i][j] = np.array(netCDF4.Dataset(target)[target_lon])[j]
  else:
    t_lat = np.array(netCDF4.Dataset(target)[target_lat])
    t_lon = np.array(netCDF4.Dataset(target)[target_lon])
  if np.array(netCDF4.Dataset(refer)[refer_lat]).ndim == 1 or np.array(netCDF4.Dataset(refer)[refer_lon]).ndim == 1:
    r_lat = np.empty([len(netCDF4.Dataset(refer)[refer_lat]),len(netCDF4.Dataset(refer)[refer_lon])])
    r_lon = np.empty([len(netCDF4.Dataset(refer)[refer_lat]),len(netCDF4.Dataset(refer)[refer_lon])])
    for i in range(len(netCDF4.Dataset(refer)[refer_lat])):
      for j in range(len(netCDF4.Dataset(refer)[refer_lon])):
        r_lat[i][j] = np.array(netCDF4.Dataset(refer)[refer_lat])[i]
        r_lon[i][j] = np.array(netCDF4.Dataset(refer)[refer_lon])[j]
  else:
    r_lat = np.array(netCDF4.Dataset(refer)[refer_lat])
    r_lon = np.array(netCDF4.Dataset(refer)[refer_lon])
  if np.array(netCDF4.Dataset(target)[target_val]).ndim == 3:
    t_val = np.array(netCDF4.Dataset(target)[target_val])
    new_t_val = np.empty([len(netCDF4.Dataset(target)[target_val]),r_lat.shape[0],r_lat.shape[1]])
    for t in range(len(netCDF4.Dataset(target)[target_val])):
      for i in range(r_lat.shape[0]):
        for j in range(r_lat.shape[1]):
          tmp = np.nan
          if interp == "2x2":
            d = ((t_lat-r_lat[i][j])**2+(t_lon-r_lon[i][j])**2)**0.5
            d_min = np.argpartition(d,4,axis=None)
            d_all = d[np.unravel_index(d_min[0],d.shape)]+d[np.unravel_index(d_min[1],d.shape)]+d[np.unravel_index(d_min[2],d.shape)]+d[np.unravel_index(d_min[3],d.shape)]
            new_t_val[t][i][j] = t_val[t][np.unravel_index(d_min[0],d.shape)]*d[np.unravel_index(d_min[0],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[1],d.shape)]*d[np.unravel_index(d_min[1],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[2],d.shape)]*d[np.unravel_index(d_min[2],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[3],d.shape)]*d[np.unravel_index(d_min[3],d.shape)]/d_all
          elif interp == "4x4":
            d = ((t_lat-r_lat[i][j])**2+(t_lon-r_lon[i][j])**2)**0.5
            d_min = np.argpartition(d,16,axis=None)
            d_all = d[np.unravel_index(d_min[0],d.shape)]+d[np.unravel_index(d_min[1],d.shape)]+d[np.unravel_index(d_min[2],d.shape)]+d[np.unravel_index(d_min[3],d.shape)]+d[np.unravel_index(d_min[4],d.shape)]+d[np.unravel_index(d_min[5],d.shape)]+d[np.unravel_index(d_min[6],d.shape)]+d[np.unravel_index(d_min[7],d.shape)]+d[np.unravel_index(d_min[8],d.shape)]+d[np.unravel_index(d_min[9],d.shape)]+d[np.unravel_index(d_min[10],d.shape)]+d[np.unravel_index(d_min[11],d.shape)]+d[np.unravel_index(d_min[12],d.shape)]+d[np.unravel_index(d_min[13],d.shape)]+d[np.unravel_index(d_min[14],d.shape)]+d[np.unravel_index(d_min[15],d.shape)]
            new_t_val[t][i][j] = t_val[t][np.unravel_index(d_min[0],d.shape)]*d[np.unravel_index(d_min[0],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[1],d.shape)]*d[np.unravel_index(d_min[1],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[2],d.shape)]*d[np.unravel_index(d_min[2],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[3],d.shape)]*d[np.unravel_index(d_min[3],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[4],d.shape)]*d[np.unravel_index(d_min[4],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[5],d.shape)]*d[np.unravel_index(d_min[5],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[6],d.shape)]*d[np.unravel_index(d_min[6],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[7],d.shape)]*d[np.unravel_index(d_min[7],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[8],d.shape)]*d[np.unravel_index(d_min[8],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[9],d.shape)]*d[np.unravel_index(d_min[9],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[10],d.shape)]*d[np.unravel_index(d_min[10],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[11],d.shape)]*d[np.unravel_index(d_min[11],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[12],d.shape)]*d[np.unravel_index(d_min[12],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[13],d.shape)]*d[np.unravel_index(d_min[13],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[14],d.shape)]*d[np.unravel_index(d_min[14],d.shape)]/d_all+t_val[t][np.unravel_index(d_min[15],d.shape)]*d[np.unravel_index(d_min[15],d.shape)]/d_all
          else:
            d = ((t_lat-r_lat[i][j])**2+(t_lon-r_lon[i][j])**2)**0.5
            new_t_val[t][i][j] = t_val[t][np.unravel_index(d.argmin(),d.shape)]
    new = netCDF4.Dataset(target[:-3]+"_regrid.nc","w",format="NETCDF4")
    new.createDimension(target_lat,r_lat.shape[0])
    new.createDimension(target_lon,r_lon.shape[1])
    new.createDimension(target_val,None)
    new_lat = new.createVariable(target_lat,"f8",(target_lat,target_lon,))
    new_lon = new.createVariable(target_lon,"f8",(target_lat,target_lon,))
    new_val = new.createVariable(target_val,"f8",(target_val,target_lat,target_lon))
    new_lat[:,:] = r_lat
    new_lon[:,:] = r_lon
    new_val[:,:,:] = new_t_val
    new.close()
  else:
    t_val = np.array(netCDF4.Dataset(target)[target_val])
    new_t_val = np.empty([r_lat.shape[0],r_lat.shape[1]])
    for i in range(r_lat.shape[0]):
      for j in range(r_lat.shape[1]):
        tmp = np.nan
        if interp == "2x2":
          d = ((t_lat-r_lat[i][j])**2+(t_lon-r_lon[i][j])**2)**0.5
          d_min = np.argpartition(d,4,axis=None)
          d_all = d[np.unravel_index(d_min[0],d.shape)]+d[np.unravel_index(d_min[1],d.shape)]+d[np.unravel_index(d_min[2],d.shape)]+d[np.unravel_index(d_min[3],d.shape)]
          new_t_val[i][j] = t_val[np.unravel_index(d_min[0],d.shape)]*d[np.unravel_index(d_min[0],d.shape)]/d_all+t_val[np.unravel_index(d_min[1],d.shape)]*d[np.unravel_index(d_min[1],d.shape)]/d_all+t_val[np.unravel_index(d_min[2],d.shape)]*d[np.unravel_index(d_min[2],d.shape)]/d_all+t_val[np.unravel_index(d_min[3],d.shape)]*d[np.unravel_index(d_min[3],d.shape)]/d_all
        elif interp == "4x4":
          d = ((t_lat-r_lat[i][j])**2+(t_lon-r_lon[i][j])**2)**0.5
          d_min = np.argpartition(d,16,axis=None)
          d_all = d[np.unravel_index(d_min[0],d.shape)]+d[np.unravel_index(d_min[1],d.shape)]+d[np.unravel_index(d_min[2],d.shape)]+d[np.unravel_index(d_min[3],d.shape)]+d[np.unravel_index(d_min[4],d.shape)]+d[np.unravel_index(d_min[5],d.shape)]+d[np.unravel_index(d_min[6],d.shape)]+d[np.unravel_index(d_min[7],d.shape)]+d[np.unravel_index(d_min[8],d.shape)]+d[np.unravel_index(d_min[9],d.shape)]+d[np.unravel_index(d_min[10],d.shape)]+d[np.unravel_index(d_min[11],d.shape)]+d[np.unravel_index(d_min[12],d.shape)]+d[np.unravel_index(d_min[13],d.shape)]+d[np.unravel_index(d_min[14],d.shape)]+d[np.unravel_index(d_min[15],d.shape)]
          new_t_val[i][j] = t_val[np.unravel_index(d_min[0],d.shape)]*d[np.unravel_index(d_min[0],d.shape)]/d_all+t_val[np.unravel_index(d_min[1],d.shape)]*d[np.unravel_index(d_min[1],d.shape)]/d_all+t_val[np.unravel_index(d_min[2],d.shape)]*d[np.unravel_index(d_min[2],d.shape)]/d_all+t_val[np.unravel_index(d_min[3],d.shape)]*d[np.unravel_index(d_min[3],d.shape)]/d_all+t_val[np.unravel_index(d_min[4],d.shape)]*d[np.unravel_index(d_min[4],d.shape)]/d_all+t_val[np.unravel_index(d_min[5],d.shape)]*d[np.unravel_index(d_min[5],d.shape)]/d_all+t_val[np.unravel_index(d_min[6],d.shape)]*d[np.unravel_index(d_min[6],d.shape)]/d_all+t_val[np.unravel_index(d_min[7],d.shape)]*d[np.unravel_index(d_min[7],d.shape)]/d_all+t_val[np.unravel_index(d_min[8],d.shape)]*d[np.unravel_index(d_min[8],d.shape)]/d_all+t_val[np.unravel_index(d_min[9],d.shape)]*d[np.unravel_index(d_min[9],d.shape)]/d_all+t_val[np.unravel_index(d_min[10],d.shape)]*d[np.unravel_index(d_min[10],d.shape)]/d_all+t_val[np.unravel_index(d_min[11],d.shape)]*d[np.unravel_index(d_min[11],d.shape)]/d_all+t_val[np.unravel_index(d_min[12],d.shape)]*d[np.unravel_index(d_min[12],d.shape)]/d_all+t_val[np.unravel_index(d_min[13],d.shape)]*d[np.unravel_index(d_min[13],d.shape)]/d_all+t_val[np.unravel_index(d_min[14],d.shape)]*d[np.unravel_index(d_min[14],d.shape)]/d_all+t_val[np.unravel_index(d_min[15],d.shape)]*d[np.unravel_index(d_min[15],d.shape)]/d_all
        else:
          d = ((t_lat-r_lat[i][j])**2+(t_lon-r_lon[i][j])**2)**0.5
          new_t_val[i][j] = t_val[np.unravel_index(d.argmin(),d.shape)]
    new = netCDF4.Dataset(target[:-3]+"_regrid.nc","w",format="NETCDF4")
    new.createDimension(target_lat,r_lat.shape[0])
    new.createDimension(target_lon,r_lon.shape[1])
    new_lat = new.createVariable(target_lat,"f8",(target_lat,target_lon,))
    new_lon = new.createVariable(target_lon,"f8",(target_lat,target_lon,))
    new_val = new.createVariable(target_val,"f8",(target_lat,target_lon,))
    new_lat[:,:] = r_lat
    new_lon[:,:] = r_lon
    new_val[:,:] = new_t_val
    new.close()
