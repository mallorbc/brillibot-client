from client import BrillibotClient
from config import Config
if __name__ == "__main__":
    client = BrillibotClient(Config())
    try:
        message, status = client.get_status()
    except:
        print("System is offline")
        quit()

    response = client.listen()
    print(response)