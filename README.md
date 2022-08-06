# nc-regrid
A function that regrids netCDF files.

### build
- linux x86_64
- python 3.9

### usage
```
# regrid target files to same grid as reference files
git clone https://github.com/blizzwind/nc-regrid
cd nc-regrid
python
>>> import nc_regrid
>>> nc_regrid.nc_regrid("./path-to/target.nc","variable that contain target latitude","variable that contain target longitude","variable that contain target value","./path-to/reference.nc","variable that contain reference latitude","variable that contain reference longitude",["nn" or "2x2" or "4x4"])
```

### notice
created by cython<br>
..._regrid.nc is the regrided file
