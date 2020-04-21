import json
import requests
import config

def main():
    username = input("Enter Twitch username: ")
    link = "https://api.twitch.tv/helix/users?login={}".format(username)
    headers = {
        "Client-ID": config.client_id
    }
    response = requests.get(link, headers=headers)
    channel_id = json.loads(response.text)["data"][0]["id"]
    print("Twitch channel_id: {}".format(channel_id))
    
if __name__ == "__main__":
    main()
