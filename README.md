This is a short script developed for the purpose of extracting tracer data from an oceanic circulation model (S.Dutkiewicz & M.Follows at MIT). It allows the user to specify the specific depth at which they'd like to extract data, and outputs a folder containing all the extracted data, ordered by month. 

Currently, the files are saved in csv format, but this may be  updated, to improve performance and reduce memory usage.

NOTE: Please ensure that the netCDF files you'd like to extract from are all contained in the same folder, and that there are no missing monthly datasets, as the resulting files will be named in consequtive order. 
