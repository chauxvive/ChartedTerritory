import requests
from bs4 import BeautifulSoup
import json

# Wikipedia URL for best-selling albums by year
url = "https://en.wikipedia.org/wiki/List_of_best-selling_albums_by_year"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all tables
tables = soup.find_all("table", class_="wikitable")

# Store album data
band_data = {}

for table in tables:
    rows = table.find_all("tr")
    for row in rows[1:]:  # Skip headers
        cols = row.find_all("td")
        if len(cols) >= 3:
            year = cols[0].text.strip()
            artist = cols[2].text.strip()

            if year not in band_data:
                band_data[year] = []

            if artist not in band_data[year]:  # Avoid duplicates
                band_data[year].append({"artist": artist})

# Save as JSON
with open("top_bands_by_year.json", "w", encoding="utf-8") as f:
    json.dump(band_data, f, indent=4)

print("Data saved to top_bands_by_year.json")