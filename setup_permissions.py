import twitch
import utils

def main():
    utils.init_logger()
    logger = utils.get_logger()

    twitch.user_access_token()

if __name__ == "__main__":
    main()
