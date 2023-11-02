import requests

# Define a function to obtain the Metabase session ID
def get_metabase_session_id(base_url, username, password):
    url = f"{base_url}/api/session"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("id")
    else:
        print("Failed to obtain the session ID. Status code:", response.status_code)
        return None

# Define a function to delete a Metabase card
def delete_metabase_card(card_id, base_url, session_id):
    url = f"{base_url}/api/card/{card_id}"
    headers = {"Content-Type": "application/json", "X-Metabase-Session": session_id}
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print("Card deleted successfully.")
    else:
        print("Failed to delete the card. Status code:", response.status_code)

# Set the appropriate values for the Metabase base URL, username, and password
metabase_base_url = "YOUR_METABASE_URL"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

# Get the session ID
session_id = get_metabase_session_id(metabase_base_url, username, password)

if session_id:
    print("Session ID:", session_id)
    # Set the appropriate values for the card ID
    card_ids = []
    # Delete the Metabase card
    delete_metabase_card(card_ids, metabase_base_url, session_id)
else:
    print("Failed to obtain the session ID.")
