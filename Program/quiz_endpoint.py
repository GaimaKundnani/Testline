import requests
import json

# URL of the JSON file
url = "https://www.jsonkeeper.com/b/LLQT"

# Send a GET request to fetch the JSON data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    # Save the data to a file
    with open("quiz_endpoint.json", "w") as file:
        json.dump(data, file, indent=4)  # Save with formatting for readability
    
    print("JSON file has been saved as 'quiz_endpoint.json'")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
