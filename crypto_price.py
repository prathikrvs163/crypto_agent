import requests
from cachetools import TTLCache

# Cache the prices for 5 minutes (300 seconds)
cache = TTLCache(maxsize=50, ttl=300)

def fetch_crypto_price(crypto_name):
    """Fetch the price of a specific cryptocurrency in USD."""
    crypto_name = crypto_name.lower()  # Normalize the input

    if crypto_name in cache:
        return cache[crypto_name]

    try:
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name}&vs_currencies=usd"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()

        if crypto_name in data:
            price = f"{crypto_name.capitalize()} price is ${data[crypto_name]['usd']} USD."
            cache[crypto_name] = price
            return price
        else:
            return f"Could not find price for '{crypto_name}'. Make sure the name is correct."
    except requests.exceptions.RequestException as e:
        return f"Error fetching {crypto_name} price: {str(e)}"
