from constants import ABORT_ALL_POSITIONS, FIND_COINTEGRATED, PLACE_TRADES, MANAGE_EXITS
from func_connections import connect_dydx
from func_private import abort_all_positions
from func_public import construct_market_prices
from func_cointegration import store_cointegration_results
from func_entry_pairs import open_positions
from func_exit_pairs import manage_trade_exits
from func_messaging import send_message

if __name__ == "__main__":

    # Message on launch
    send_message("Bot Launch Successful")
    

    # Connect to client
    try: 
        print("connecting to client ...")
        client = connect_dydx()
    except Exception as e:
      print("Error connecting to client", e)
      send_message("Failed to connect to client"{e})
      exit(1)

# Abort all open positions
if ABORT_ALL_POSITIONS:
    try:
      print("closing all positions ...")
      close_orders = abort_all_positions(client)
    except Exception as e: 
        print("Error closing all positions", e)
        send_message("Error closing all position" {e})
        exit(1)

# Find cointegrated pairs
if FIND_COINTEGRATED:

  # Construct Markets prices
    try: 
        print("Fetching markets prices, please allow 3 mins ...")
        df_market_prices = construct_market_prices(client)
    except Exception as e:
      print("Error constructing market prices", e)
      send_message("Error constructing market prices"{e})
      exit(1)

 # Store Cointegrated pairs
    try: 
        print("Storing cointagrated pairs ...")
        stores_result = store_cointegration_results(df_market_prices)
        if stores_result != "saved":
          print("Error saving cointegrated pairs")
          exit(1)
    except Exception as e:
      print("Error saving cointegrated pairs", e)
      send_message("Error saving cointegrated pairs"{e})
      exit(1)

#Run as always running on
while True:


  if MANAGE_EXITS:
    try: 
        print("manage exit ...")
        manage_trade_exits(client)
    except Exception as e:
      print("Error managing exit positions", e)
      send_message("Error managing exit positions"{e})
      exit(1)

  if PLACE_TRADES:
    try: 
        print("finding trading opportunities ...")
        open_positions(client)
    except Exception as e:
      print("Error trading pairs", e)
      send_message("Error opening trades"{e})
      exit(1)

 