# Telegram Template Bot

Template bot for Telegram in Python.

## How to Run
1. Set up your bot:
    1.1. Create a bot account on [Telegram](https://telegram.org/).
    1.2. Create a bot on [Telegram Bot Creator](https://t.me/botfather).
    1.3. Set up your bot:
        1.3.1. Set the bot token.
        1.3.2. Set the bot name.
        1.3.3. Set the bot description.
        1.3.4. Set the bot username.

2. Set your Telegram bot token as the environment variable `BotToken`.
```
export BotToken=<your bot token>
```

3. Add 'src' to your `PYTHONPATH`:
```
export PYTHONPATH=${PWD}
```

4. Run the bot with:
```
python src/run.py
```