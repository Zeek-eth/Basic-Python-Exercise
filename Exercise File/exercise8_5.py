import requests
import time
from telegram.ext import Updater

# CoinGecko API URL
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
TELEGRAM_TOKEN = "5698712224:AAGnNrK0THRu5L8vBTWcZQZU1nBBFLWIuvU";
TELEGRAM_CHAT_ID = "5591584952";


# function to get latest price data for all tokens
def get_all_token_prices(page=1):
    # make API call to CoinGecko
    response = requests.get(API_URL, params={"vs_currency": "usd", "per_page": 250, "page": page})

    # parse response as JSON
    data = response.json()
    # print(data)

    # create a map to store token prices
    token_prices = {}
    # store the prices in the map
    for token in data:
        token_prices[token["id"]] = token["current_price"]

    # log token price
    print(token_prices)

    # log token_prices length
    print(len(token_prices))

    # check if there are more pages of data
    if len(data) == 250:
        # get prices for next page
        token_prices.update(get_all_token_prices(page=page + 1))

    # #log token price
    # print(token_prices)

    # return the map
    return token_prices

    # return a map of token IDs to current prices
    return {token["id"]: token["current_price"] for token in data}


# function to scan for sudden changes in token prices
def scan_for_sudden_changes():
    # create a new Telegram bot
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    bot = updater.bot

    # get the initial prices for all tokens
    previous_prices = get_all_token_prices()

    # scan for sudden changes in token prices every 5 minutes
    while True:
        # sleep for 5 minutes
        time.sleep(5 * 60)

        # get the current prices for all tokens
        current_prices = get_all_token_prices()

        # check for sudden changes in token prices
        for token_id, current_price in current_prices.items():
            # compare current price to previous price
            previous_price = previous_prices[token_id]
            change = (current_price - previous_price) / previous_price
            if abs(change) > 0.05:  # 5% change
                # send notification to user
                bot.send_message(TELEGRAM_CHAT_ID,
                                 f"{token_id} has experienced a sudden {'increase' if change > 0 else 'decrease'} in price")

                # update previous price for token
                previous_prices[token_id] = current_price


# start scanning for sudden changes in token prices
scan_for_sudden_changes()