 #!/bin/bash
 
 echo
 echo "This program extracts all tracer data at a specified depth, and returns a csv file for each .nc"
 echo
 echo "Please enter the directory path, relative to your current directory: " 
 read directory_name
 echo "Please enter the depth you wish to extract from (Z=(1...22)): "
 read depth

 export depth=$depth
 export root="depth"$depth
 mkdir "depth"$depth

 cwd=$(pwd)
 file_path=$cwd/$directory_name

 month=1
 for f in $file_path/*
 do
      export nc_filename=$f
      python get_depth.py $month 
      ((month=month+1))
 done

 # Note: Try saving as pickle (python only) or MessagePack - faster, saves space
