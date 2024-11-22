
#!/bin/bash

# Change to the directory where your Python script is located
cd /home/serfani/projects/smap/

# Activate the virtual environment
source /home/serfani/projects/smap/.venv/bin/activate

# Loop through each year
for year in {2004..2009}; do
    echo "Starting downloads for year $year"

    # Loop through each month
    for month in {1..12}; do
        
        echo "Requesting data for $year-$month..."
        file="/home/serfani/serfani_data0/era5_daily/ERA5_data_${year}_$(printf "%02d" $month).zip"
        
        if [ -f "$file" ]; then
            echo "$file exists."
        else
            # Run the Python script for the current year and month in the background
            python download_era5_nc.py --year "$year" --month "$month" &
        fi
     
    done

    # Wait for all background processes (i.e., all 12 monthly downloads) to complete for the current year
    wait
    echo "All downloads completed for year $year"

done

echo "All downloads completed for all years."
