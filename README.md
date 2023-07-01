
<img src="https://github.com/lmangani/chdb-discord-bot/assets/1423657/c759f2bc-ecd7-464c-aaab-b9bfbc9b3569" height=150 ><img src="https://github.com/lmangani/chdb-discord-bot/assets/1423657/020db902-a577-4bf4-a9ce-45403b166e19" height=130 >

# chdb-discord-bot
Serverless bot running SQL queries using [chDB](https://chdb.io) [public servers](https://chdb.fly.dev) or any ClickHouse HTTP/S APIs

## Features
- `/ping` - a simple command that tells you the bot's latency.
- `/query <query> [format]` - a command that queries [chDB API](https://chdb.io) (ClickHouse).
- A status message `Listening to /query! | chDB` via [scheduled actions](https://deta.space/docs/en/basics/micros#scheduled-actions).
- And you can easily create and add more commands yourself!


## Requirements
- **Discord Application:** Create an app for **FREE** at [Discord Developer Portal](https://discord.com/developers/applications).
- **Deta Space account:** Create an account for **FREE** at [Deta Space](https://deta.space/), username + password.
- **chDB API URL:** Use the public service, or point at your HTTP/S chDB/ClickHouse compatible API..

## Running Online
1. Create a new deta.space application:
   1. Install the [Space CLI](https://deta.space/docs/en/basics/cli).
   2. Clone this repository.
   3. Make sure you're in the project folder: `$cd <folder>`
   4. Create a space app: `$space new`
   5. Push the space app: `$space push`
2. Enter the environment variables (Space App Settings ➔ Configuration).<br>
    <img src="https://github.com/lmangani/chdb-discord-bot/assets/1423657/3c43aba8-1e8a-4b1c-91e4-241a1ff5ba17" width=500 >
    - `DISCORD_APPLICATION_ID` - Your discord app's ID.
    - `DISCORD_PUBLIC_KEY` - Your discord app's public key.
    - `DISCORD_BOT_TOKEN` - Your bot's token.
    - `CHDB_API` - Your ClickHouse HTTP/S API _(optional)_
    - _Other environment variables are optional._
4. Set `Interactions Endpoint URL` to `<micro_url>/bot/interactions`.
    - This is located in: `https://discord.com/developers/applications/{application_id}/information`
    - A Micro URL looks like this: `https://chdbdiscordbot-xxxxxxx.deta.app`
5. Visit `<micro_url>/bot/api/dash/<discord_bot_token>` to register the slash commands for the first time.
   - If this fails, use the `register.sh` script with your `DISCORD_APPLICATION_ID` and `DISCORD_BOT_TOKEN`
6. Run `/ping` to make sure it's working! Enjoy!

## Test Commands

![chdb-discord-bot](https://github.com/lmangani/chdb-discord-bot/assets/1423657/c0db85ef-0cf6-46ef-91da-d2d42fffabee)

## Powered by Deta.space
This Discord bot is **SERVERLESS** which means it can run for **FREE** and be **ALWAYS online** on [Deta Space](https://deta.space)!  

Code forked and adapted from [chatgpt-discord-bot](https://github.com/imptype/serverless-chatgpt-discord-bot)

## Links and Resources
- **Deta Space Documentation:** https://deta.space/docs
- **Deta Discord:** https://discord.gg/deta
- **Discohook Discord:** https://discord.gg/xEEpJvE9py
- **Discord API Documentation:** https://discord.com/developers/docs
- **Space App Discovery Page:** https://deta.space/discovery/@imp1/chatgpt
