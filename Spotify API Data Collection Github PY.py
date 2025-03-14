# Spotify API Data Collection

import requests
import pandas as pd
import json
import time

# Spotify API credentials
# To access the Spotify API, we need to authenticate using a client ID and client secret.
# These credentials allow us to obtain an access token, which is required to make requests
# to various Spotify API endpoints. The TOKEN_URL is used to obtain this access token.

CLIENT_ID = "your_id"
CLIENT_SECRET = "your_secret"
TOKEN_URL = "your token"

# Function to obtain an access token from Spotify API
# This function sends a POST request to the Spotify authentication endpoint with the necessary credentials.
# If the request is successful, it returns an access token that will be used in subsequent API requests.
# In case of an error, it prints the error message and returns None.

def get_access_token():
    try:
        response = requests.post(TOKEN_URL, {
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        })
        response.raise_for_status()  # If the request fails, raise an HTTPError
        token_info = response.json()
        return token_info.get('access_token')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching token: {e}")
        return None
    
# Function to fetch data from any Spotify API endpoint
# This function takes an API endpoint URL and an optional parameter dictionary.
# It first retrieves an access token and then uses it to send an authenticated GET request to Spotify.
# The function returns the JSON response from the API.

def get_spotify_data(endpoint, params=None):
    token = get_access_token()
    if token is None:
        print("Unable to fetch access token.")
        return {}
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(endpoint, headers=headers, params=params)
    return response.json()

# Function to fetch newly released albums from Spotify
# This function specifically calls the 'new-releases' API endpoint to retrieve the latest album releases.
# The response contains album details such as name, artist, and release date.

def fetch_new_tracks():
    url = "https://api.spotify.com/v1/browse/new-releases"
    data = get_spotify_data(url)
    return data

# Function to process the retrieved data and convert it into a structured Pandas DataFrame
# The function extracts album details such as album name, artist name, and release date.
# If no albums are found in the API response, it returns an empty DataFrame.

def process_data(data):
    if 'albums' not in data or 'items' not in data['albums']:
        print("No albums found.")
        return pd.DataFrame()
    
    albums = data['albums']['items']
    df = pd.DataFrame([{
        "album_name": album["name"],
        "artist_name": album["artists"][0]["name"],
        "release_date": album["release_date"]
    } for album in albums])
    return df

# Function to save the DataFrame to a CSV file
# If the DataFrame contains data, it is saved as a CSV file with the given filename.
# Otherwise, a message is displayed indicating that there is no data to save.

def save_to_csv(df, filename="spotify_data.csv"):
    if not df.empty:
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

# Main function to execute the data fetching, processing, and saving operations
# This function calls the appropriate functions in sequence to fetch new tracks, process them,
# and save the results to a CSV file.

def main():
    data = fetch_new_tracks()
    df = process_data(data)
    save_to_csv(df)

if __name__ == "__main__":
    main()

# Reading a CSV file into a Pandas DataFrame
# This section reads the saved CSV file containing newly released albums and displays its contents.

import pandas as pd
df = pd.read_csv('new_released_albums.csv', sep=',')
df

# Function to retrieve artists based on a specific genre
# This function sends a request to the Spotify API's search endpoint, filtering results by genre.
# It returns a list of artists that belong to the specified genre, sorted by popularity.

def get_artists_by_genre(genre, limit=50):
    try:
        token = get_access_token()
        if not token:
            raise ValueError("Token could not be retrieved.")

        headers = {"Authorization": f"Bearer {token}"}
        url = "https://api.spotify.com/v1/search"
        
        params = {
            "q": f"genre:{genre}",
            "type": "artist",
            "limit": limit
        }

        response = requests.get(url, headers=headers, params=params)
        
        # Check if the API response was successful
        response.raise_for_status()  # Raises HTTPError for failed requests
        data = response.json()

        # Extract and return the list of artists from the API response
        return data["artists"]["items"]

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
    except ValueError as e:
        print(f"Token error: {e}")
    except KeyError as e:
        print(f"Expected data missing: {e}")
    except Exception as e:
        print(f"An unknown error occurred: {e}")

# Function to create a DataFrame of artists based on genre
# This function fetches a list of artists for the specified genre and stores relevant details in a DataFrame.
# Each artist's name, popularity, and follower count are included.

def create_artist_dataframe(genre):
    try:
        artists = get_artists_by_genre(genre)
        if not artists:
            raise ValueError("No artists found for the given genre.")
        
        artist_list = []
        for i, artist in enumerate(artists, start=1):
            try:
                artist_list.append({
                    "index": i,
                    "name": artist.get("name", "Unknown"),
                    "popularity": artist.get("popularity", 0),
                    "followers": artist.get("followers", {}).get("total", 0)
                })
            except Exception as e:
                print(f"Error processing artist data: {e}")
                continue
        
        df = pd.DataFrame(artist_list)
        return df
    except Exception as e:
        print(f"Error fetching artists: {e}")
        return pd.DataFrame()

# Fetch rock artists and create a DataFrame
# The following code fetches data for artists in the "rock" genre and stores it in a Pandas DataFrame.

rock_df = create_artist_dataframe("rock")
rock_df
