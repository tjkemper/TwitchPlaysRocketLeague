# TwitchPlaysRocketLeague
Control Rocket League with Twitch channel points


## Usage

### Start
Open powershell, cd to this project directory and run:
```
python run.py
```

### Stop
Either:
* Press `ctrl + C` in the powershell window
* Close the powershell window

### Customizing
The easiest way to turn on/off controls is through your channel points. If you want to remove jump, disable or delete your `Twitch Plays: Jump` channel points.


## Getting set up

### 1. Download repository
```
git clone https://github.com/tjkemper/RocketLeagueTwitchController.git
```

### 2. Create Twitch Application
https://dev.twitch.tv/console/apps/create

Set `OAuth Redirect URLs` to `http://localhost`

In `config/twitch_config.py`, set the two following values

```
client_id = ""
redirect_uri = "http://localhost"
```

### 3. Find your channel_id
You must set the `client_id` variable in order to do this step.

Open powershell, cd to this project directory and run:
```
python get_channel_id.py
```

Put your Twitch channel id in `config/twitch_config.py`

### 4. Get an access_token / auth_token
Open powershell, cd to this project directory and run:
```
python setup_permissions.py
```

Follow the instructions.

This token is only good for 60 days.

### 5. Set up Rocket League key bindings
Go to `config/rocketleague_config.py` and set up key bindings.

```
DRIVE_FORWARD   = ["w",           3]
```
The above means that "w" is my drive key and I want it held for 3 seconds.

> Known issue: Mouse inputs and some special characters are not yet supported.

### 6. Channel Points
Create channel point rewards in Twitch.

Here's the link, just replace `YOUR USERNAME`.
https://dashboard.twitch.tv/u/YOUR USERNAME/community/channel-points/rewards

Then go to `config/twitch_config.py` and edit the `channel_points_title_to_rocketleague_control` dictionary.

If this is my configuration, I need a channel points title that matches `Twitch Plays: Jump`.
```
channel_points_title_to_rocketleague_control = {
    "Twitch Plays: Jump": Controls.JUMP,
}
```

### 7. Run it
Open powershell, cd to this project directory and run:
```
python run.py
```

Everything should work! Give it a try :)


## Links

### Twitch Links 
* https://dev.twitch.tv
* https://dev.twitch.tv/docs/glossary#glossary
* https://dev.twitch.tv/docs/pubsub/
* https://dev.twitch.tv/docs/authentication/getting-tokens-oauth#oauth-implicit-code-flow
* https://dev.twitch.tv/docs/authentication/getting-tokens-oauth#oauth-client-credentials-flow
* https://github.com/twitchdev/pubsub-javascript-sample/blob/master/main.js
* https://discuss.dev.twitch.tv/t/only-getting-err-badauth-from-listen-pubsub-request/23598/4

### Websocket Links
* https://github.com/websocket-client/websocket-client
