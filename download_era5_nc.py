import argparse
import cdsapi

def download_era5_data(year, month):
    # Initialize the CDS API client
    client = cdsapi.Client()

    # Define dataset and variables
    dataset = "derived-era5-single-levels-daily-statistics"
    variables = [
        "2m_dewpoint_temperature",
        "2m_temperature",
        "mean_sea_level_pressure",
        "total_precipitation",
        "maximum_2m_temperature_since_previous_post_processing",
        "minimum_2m_temperature_since_previous_post_processing",
        "volumetric_soil_water_layer_1",
        "evaporation",
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "mean_top_net_long_wave_radiation_flux",
        "mean_surface_direct_short_wave_radiation_flux"
    ]

    # Define the request parameters
    request = {
        "product_type": "reanalysis",
        "year": str(year),
        "month": [str(month).zfill(2)],
        "day": [
            "01", "02", "03", "04", "05", "06",
            "07", "08", "09", "10", "11", "12",
            "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24",
            "25", "26", "27", "28", "29", "30", "31"
        ],
        "daily_statistic": "daily_mean",
        "time_zone": "utc+00:00",
        "frequency": "1_hourly",
        "variable": variables
    }

    # File path to save data
    output_file = f"/home/serfani/serfani_data0/era5_daily/ERA5_data_{year}_{month:02}.zip"

    # Retrieve and download the data
    print(f"Downloading data for year {year}-{month:02}...")
    client.retrieve(dataset, request, output_file)
    print(f"Data for {year}-{month:02} downloaded as {output_file}.")


def main():
    # Set up argument parser for year and month
    parser = argparse.ArgumentParser(description="Retrieve ERA5 data for a specific year and month.")
    parser.add_argument("--year", type=int, required=True, help="Year of the data to download (e.g., 2023)")
    parser.add_argument("--month", type=int, required=True, help="Month of the data to download (1-12)")

    # Parse arguments
    args = parser.parse_args()

    # Call the download function with provided year and month
    download_era5_data(args.year, args.month)


if __name__ == "__main__":
    main()
