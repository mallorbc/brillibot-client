from client import BrillibotClient
from config import Config
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--actions_file", help="Option to override actions", type=str,default=None)
    parser.add_argument("-k", "--key", help="Option to override key", type=str,default=None)
    parser.add_argument("-u", "--url", help="Option to override url", type=str,default=None)
    parser.add_argument("-s", "--save_file", help="Option to override save_file", action="store_true",default=None)
    parser.add_argument("-e", "--energy_threshold", help="Option to override energy_threshold", type=int,default=None)
    parser.add_argument("-p", "--pause_threshold", help="Option to override pause_threshold", type=float,default=None)
    parser.add_argument("-w", "--awake_word", help="Option to override awake_word", type=str,default=None)
    parser.add_argument("-l", "--listen_loop", help="Will keep listening", action="store_true",default=None)
    args = parser.parse_args()
    config = Config()
    if args.actions_file:
        config.actions_file = args.actions_file
    if args.key:
        config.key = args.key
    if args.url:
        config.url = args.url
    if args.save_file:
        config.save_file = args.save_file
    if args.energy_threshold:
        config.energy_threshold = args.energy_threshold
    if args.pause_threshold:
        config.pause_threshold = args.pause_threshold

    client = BrillibotClient(config)
    try:
        message, status = client.get_status()
    except:
        print("System is offline")
        quit()
    
    if args.listen_loop:
        client.listen_loop()
    else:
        response = client.listen()
        print(response)    

if __name__ == "__main__":
    main()
