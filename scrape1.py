import requests
from datetime import datetime

# CoinMarketCap API Key
API_KEY = '802d432f-1408-4f1a-8c44-a554aa78f2db'

# List of memecoins slugs
coin_slugs = [
'4-chan','pond-coin','octocat','cs1888','pepe-ordinals',
'sharp-al','corgial','fwog','giggle-academy''a-gently-used-2001-honda-civic','godcat', 'exploding-kittens', 'godcat','act-i-the-al-prophecy','baby-doge-coin-1m','cats-catshouse-live',
'al-companions', 'moo-deng-moodeng-vip','cheems-cheems-pet','real-nigger-late','smiley','kabosucoin-erc','kamala-harris-kamalaharrist-oken-xyz','neiro-solana-neirobropump-com', 'memetic-pepecoin',
    'unicorn', 'snap', 'mawcat','pepeal', 'skulls-of-pepetoken', 'act-i-the-al-prophecy',
'dogeswap','michi''tooker-kurlson','dogeswap', 'meme-cup', 'tate-stop', 'sharpei', 'flavia-is-online', 'fartcoin',
    'slop','bellscoin', 'terminus'  
]

# CoinMarketCap API endpoint for coin listings
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

# Function to fetch listing date for each coin
def fetch_listing_dates(api_key, slugs):
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    
    listing_dates = {}
    
    for slug in slugs:
        # Fetching data for each coin
        params = {'slug': slug}
        response = requests.get(BASE_URL, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            coin_data = data.get('data')
            if coin_data:
                coin_id = list(coin_data.keys())[0]
                first_data_date = coin_data[coin_id].get('date_added')
                listing_dates[slug] = first_data_date
            else:
                listing_dates[slug] = "Data not found"
        else:
            listing_dates[slug] = f"Error {response.status_code}"
    
    return listing_dates

# Get listing dates
listing_dates = fetch_listing_dates(API_KEY, coin_slugs)

# Print results
for coin, date in listing_dates.items():
    if date != "Data not found" and "Error" not in date:
        date = datetime.fromisoformat(date).strftime('%Y-%m-%d')
    print(f"{coin}: {date}")
