from brillibot_client.brillibot_client import BrillibotClient
from brillibot_client.config import Config

if __name__ == "__main__":
    client = BrillibotClient(Config(actions_file="../actions/actions_flight.json",awake_word="computer"))
    try:
        message, status = client.get_status()
    except:
        print("System is offline")
        quit()

    #you can now make requests to the server with file
    response = client.from_file("audio0.mp3",format="mp3")
    print(response)
