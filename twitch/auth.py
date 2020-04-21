import utils
import config

logger = utils.get_logger()

# TODO: Permissions for bits and chat
# TODO: Automate this process
def user_access_token():
    oauth_link = "https://id.twitch.tv/oauth2/authorize?client_id={}&redirect_uri={}&response_type=token&scope=channel:read:redemptions".format(
        config.client_id,
        config.redirect_uri
    )

    # Steps
    logger.debug("Twitch documentation (for the curious): https://dev.twitch.tv/docs/authentication/getting-tokens-oauth#oauth-implicit-code-flow")
    logger.info("Follow these steps:")
    logger.info("1. Copy and paste this link into your browser")
    print()
    print(oauth_link)
    print()
    logger.info("2. Sign in (if you aren't already)")
    logger.info("3. You will be redirected to http://localhost/#access_token=YOUR ACCESS TOKEN&token_type=bearer")
    logger.info("4. You only care about access_token=YOUR ACCESS TOKEN")
    logger.info("4. Copy the access_token from the url and paste in twitch_config.py's auth_token variable")
