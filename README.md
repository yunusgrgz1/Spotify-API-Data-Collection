# Spotify API Data Collection

## Overview

This project leverages the Spotify API to fetch and collect data about new album releases and artists based on a specific genre (e.g., "rock"). The data is processed and saved into a CSV file for further analysis. It provides a simple yet efficient way to interact with the Spotify API, retrieve music data, and organize it into a structured format using Python and Pandas.

## Features

- **Fetch New Releases**: Retrieves newly released albums from Spotify, including album name, artist name, and release date.
- **Genre-based Artist Search**: Allows you to search for artists by genre (e.g., "rock") and retrieves information such as artist name, popularity, and follower count.
- **Data Processing**: Transforms the raw data from Spotify API into structured data stored in a Pandas DataFrame.
- **CSV Export**: Saves the processed data into a CSV file for easy export and analysis.
- **Error Handling**: Handles potential errors gracefully, such as issues with the API token or missing data.

## Prerequisites

Before running the project, you will need:

- **Spotify Developer Account**: Obtain a **Client ID** and **Client Secret** from the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
- **Python**: Ensure Python is installed (preferably version 3.6 or higher).
- **Python Packages**: You will need to install the following Python packages:
  - `requests` for making API calls.
  - `pandas` for handling data and saving it to CSV.

You can install the required packages by running:

```bash
pip install requests pandas
```

## Setup

1. **Spotify Credentials**: Replace the `CLIENT_ID` and `CLIENT_SECRET` variables in the script with your own Spotify API credentials.

```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
```

2. **Run the Script**: Execute the Python script to start collecting and processing the data.

```bash
python spotify_data_collection.py
```

3. **Result**: The data will be saved to a CSV file called `spotify_data.csv` in the same directory as the script.

## Functions

### `get_access_token()`
Obtains an access token from the Spotify API using the provided **Client ID** and **Client Secret**.

### `get_spotify_data(endpoint, params=None)`
Fetches data from a specified Spotify API endpoint using the access token.

### `fetch_new_tracks()`
Retrieves newly released albums from the Spotify API.

### `process_data(data)`
Converts the retrieved data into a structured Pandas DataFrame with columns like album name, artist name, and release date.

### `save_to_csv(df, filename="spotify_data.csv")`
Saves the processed data into a CSV file.

### `get_artists_by_genre(genre, limit=50)`
Searches for artists based on a specific genre (e.g., "rock") and returns the list of artists with their popularity and follower count.

### `create_artist_dataframe(genre)`
Fetches a list of artists for the specified genre and converts it into a Pandas DataFrame containing artist details.

## Example Usage

### Fetching Newly Released Albums
To fetch and save newly released albums, simply run the script:

```bash
python spotify_data_collection.py
```

### Fetching Artists by Genre
To fetch artists from a specific genre (e.g., "rock"):

```python
rock_df = create_artist_dataframe("rock")
print(rock_df)
```

This will display a DataFrame containing the artist's name, popularity, and follower count.

## Error Handling

- If the token fetch fails, the script will print an error message and terminate the process.
- Missing or incomplete data will be gracefully handled with error messages.
- If no data is found (e.g., no new releases or no artists for the selected genre), an empty DataFrame will be returned.

## License

This project is open-source and available under the MIT License. Feel free to fork and modify it as per your needs.

---

By using this project, you can efficiently collect and organize Spotify data, whether it's for analysis, recommendations, or any other use case!
