# Delete_metabase_cards

This Python script demonstrates how to interact with the Metabase API using the `requests` library. It includes functions to obtain a Metabase session ID and delete a Metabase card.

---

## Configuration

You need to provide the following information to configure the script:

- `metabase_base_url`: The base URL of your Metabase instance.
- `username`: Your Metabase username.
- `password`: Your Metabase password.

Make sure to set appropriate values for these variables:

metabase_base_url = "YOUR_METABASE_URL"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

## Functions

### `get_metabase_session_id(base_url, username, password)`

This function obtains the Metabase session ID by making a POST request to the Metabase API.

- `base_url`: The Metabase base URL.
- `username`: Your Metabase username.
- `password`: Your Metabase password.

### `delete_metabase_card(card_id, base_url, session_id)`

This function deletes a Metabase card by making a DELETE request to the Metabase API.

- `card_id`: The ID of the Metabase card you want to delete.
- `base_url`: The Metabase base URL.
- `session_id`: The session ID obtained using the `get_metabase_session_id` function.

## Usage

To use the script, set the configuration variables as described above. Then, you can call the functions to interact with the Metabase API.

Example:

## Set the appropriate values for the Metabase base URL, username, and password
metabase_base_url = "YOUR_METABASE_URL"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

# Get the session ID
session_id = get_metabase_session_id(metabase_base_url, username, password)

if session_id:
    print("Session ID:", session_id)
    # Set the appropriate values for the card ID
    card_ids = [1, 2, 3]  # Replace with actual card IDs
    # Delete the Metabase cards
    for card_id in card_ids:
        delete_metabase_card(card_id, metabase_base_url, session_id)
else:
    print("Failed to obtain the session ID.")

Replace `"YOUR_METABASE_URL"`, `"YOUR_USERNAME"`, and `"YOUR_PASSWORD"` with your Metabase configuration. The `card_ids` list should contain the IDs of the cards you want to delete.

## License

This script is provided under the [MIT License](LICENSE).

Feel free to contribute to or modify the script as needed.

If you encounter any issues or have questions, please contact us.