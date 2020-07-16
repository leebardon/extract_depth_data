<h3> Extracting Depth Data from NetCDF Files </h3>

This is a short script that I developed for extracting tracer data from an ocean biogeochemistry/ecosystem model produced by S.Dutkiewicz at MIT. The biogeochemical tracers are mixed and transported using the MIT general circulation model, which produces separate .nc files for each month of simulation time, at a range of depths. For my current research, I need to extract data for a specific depth, which I then transfer to my local machine for further processing. 

This program prompts the user to specify the depth at which they'd like to extract data, creates a suitably named directory, and populated it with the extracted data, ordered by month. At present, the files are saved in csv format, but this may be  updated, to improve performance and reduce memory usage.

<b>NOTE:</b> Please ensure that the netCDF files you'd like to extract from are all contained in the same folder, and that there are no missing monthly datasets, as the resulting files will be named in consequtive order. 
