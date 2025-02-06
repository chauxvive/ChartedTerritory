import musicbrainzngs
import json

# Set up MusicBrainz API
musicbrainzngs.set_useragent("YourApp", "1.0")

# Load the scraped JSON file
with open("top_bands_by_year.json", "r", encoding="utf-8") as f:
    band_data = json.load(f)

# Function to get artist hometown
def get_artist_hometown(artist_name):
    try:
        # Search for the artist
        result = musicbrainzngs.search_artists(artist=artist_name, limit=1)
        if result["artist-list"]:
            artist = result["artist-list"][0]  # Pick the first result

            # Try to get the primary area (hometown)
            if 'area' in artist:
                return artist["area"]["name"]  # Primary location for the artist
            else:
                return "Unknown"
    except Exception as e:
        print(f"Error fetching {artist_name}: {e}")
    return "Unknown"

# Loop through the JSON and add hometowns
for year, artists in band_data.items():
    for artist in artists:
        artist["hometown"] = get_artist_hometown(artist["artist"])

# Save updated JSON
with open("top_bands_with_hometowns.json", "w", encoding="utf-8") as f:
    json.dump(band_data, f, indent=4)

print("Updated data saved to top_bands_with_hometowns.json")
