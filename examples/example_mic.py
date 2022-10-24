from brillibot_client.brillibot_client import BrillibotClient
from brillibot_client.config import Config

if __name__ == "__main__":
    client = BrillibotClient(Config(actions_file="../actions/actions_flight.json"))
    try:
        message, status = client.get_status()
    except:
        print("System is offline")
        quit()

    #you can now make requests to the server with a mic
    response = client.listen()
    print(response)
