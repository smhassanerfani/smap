import cdsapi

# Initialize the CDS API client
client = cdsapi.Client()

# Define dataset and variables
dataset = "reanalysis-era5-single-levels"
variables = [
    "2m_dewpoint_temperature",
    "2m_temperature",
    "mean_sea_level_pressure",
    "total_precipitation",
    "maximum_2m_temperature_since_previous_post_processing",
    "minimum_2m_temperature_since_previous_post_processing",
    "mean_surface_latent_heat_flux",
    "mean_surface_sensible_heat_flux",
    "volumetric_soil_water_layer_1"
    "evaporation",
    "10m_u_component_of_wind",
    "10m_v_component_of_wind",
    "mean_top_net_long_wave_radiation_flux",
    "mean_surface_direct_short_wave_radiation_flux"
]

# Loop through each year from 1990 to 2023
for year in range(1990, 2024):
    for month in range(1, 13):
        # Define the request parameters
        request = {
            "product_type": "reanalysis",
            "year": str(year),
            "month": str(month).zfill(2),
            "day": [
                "01", "02", "03", "04", "05", "06",
                "07", "08", "09", "10", "11", "12",
                "13", "14", "15", "16", "17", "18",
                "19", "20", "21", "22", "23", "24",
                "25", "26", "27", "28", "29", "30", "31"
            ],
            "time": [
                "00:00", "01:00", "02:00", "03:00", "04:00", "05:00",
                "06:00", "07:00", "08:00", "09:00", "10:00", "11:00",
                "12:00", "13:00", "14:00", "15:00", "16:00", "17:00",
                "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"
            ],
            "data_format": "netcdf",
            "variable": variables
        }

        # File path to save each year's data
        output_file = f"/home/serfani/serfani_data0/era5/ERA5_data_{year}_{month:02}.nc"
        
        # Retrieve and download the data
        print(f"Downloading data for year {year}-{month:02}...")
        client.retrieve(dataset, request, output_file)
        print(f"Data for {year} downloaded as {output_file}.")