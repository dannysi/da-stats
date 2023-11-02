import requests

# Replace with your actual client ID and client secret
client_id = ''
client_secret = ''

# Define the token URL provided by the OAuth 2.0 authorization server
token_url = 'https://www.deviantart.com/oauth2/token'  # Replace with the actual token URL

# Define the parameters for the token request
token_params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Make the token request
response = requests.post(token_url, data=token_params)

if response.status_code == 200:
    # Parse the JSON response to get the access token
    token_data = response.json()
    access_token = token_data.get('access_token')

    print(f"Access Token: {access_token}")
else:
    print(f"Failed to retrieve access token. Status code: {response.status_code}")