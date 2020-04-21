import twitch
import utils

def main():
    utils.init_logger()
    logger = utils.get_logger()
    
    twitch.pubsub()

if __name__ == "__main__":
    main()
