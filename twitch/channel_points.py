import threading
import config
import rocketleague
import utils

logger = utils.get_logger()

def handle_message(cp_message):
    channel_points_title = cp_message["data"]["redemption"]["reward"]["title"]
    redeemer = cp_message["data"]["redemption"]["user"]["display_name"]
    redeemed_at = cp_message["data"]["redemption"]["redeemed_at"]

    logger.info("Channel points title: {}".format(channel_points_title))
    logger.info("Redeemer: {}".format(redeemer))
    logger.info("Redeemed at: {}".format(redeemed_at))
    
    if channel_points_title in config.channel_points_title_to_rocketleague_control:
        control = config.channel_points_title_to_rocketleague_control[channel_points_title]
        threading.Thread(target=rocketleague.inputs.do_control, args=[control]).start()
    else:
        logger.error("Channel points title not found: {}".format(channel_points_title))
