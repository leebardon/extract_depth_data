<h3> Extracting Depth Data from NetCDF Files </h3>

This is a short script developed for the purpose of extracting tracer data from a biogeochemical/ecosystem model produced by S.Dutkiewicz at MIT, and mixed and transported using the MIT general circulation model. The model produces separate .nc files for each month of simulation time, containing values of tracers at a range of depths. For my current research purposes, I needed to obtain data at a specific depth, and then transfer it to my local machine for further processing. 

This program allows the user to specify the depth at which they'd like to extract data, and outputs a folder containing all the extracted data, ordered by month. At present, the files are saved in csv format, but this may be  updated, to improve performance and reduce memory usage.

<b>NOTE:</b> Please ensure that the netCDF files you'd like to extract from are all contained in the same folder, and that there are no missing monthly datasets, as the resulting files will be named in consequtive order. 
