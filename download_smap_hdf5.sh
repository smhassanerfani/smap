#!/bin/bash

# Define start and end dates
start_date="2015-03-31"
end_date="2024-10-28"

# Define base directory for saving files
base_dir="/home/serfani/serfani_data1/SPL3SMP_E"

# Loop over each date in the range
current_date="$start_date"
while [[ "$current_date" < "$end_date" ]] || [[ "$current_date" == "$end_date" ]]; do
  # Format the date for the file name and URL
  formatted_date=$(echo "$current_date" | sed 's/-/./g')
  
  # Download the file for the current date with the modified path
  wget --load-cookies ~/.urs_cookies \
       --save-cookies ~/.urs_cookies \
       --keep-session-cookies \
       --no-check-certificate \
       --auth-no-challenge=on \
       -r --reject "index.html*" -np -e robots=off \
       -nH --cut-dirs=4 -P "$base_dir" \
       "https://n5eil01u.ecs.nsidc.org/SMAP/SPL3SMP_E.006/$formatted_date/SMAP_L3_SM_P_E_${formatted_date//./}_R19240_001.h5"
  
  # Increment date by one day
  current_date=$(date -I -d "$current_date + 1 day")
done