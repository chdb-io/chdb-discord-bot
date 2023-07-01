---
app_name: "chDBot"
title: "Serverless chDB/ClickHouse Query Discord Bot"
tagline: "Your personal SQL query bot."
theme_color: "#74aa9c"
git: "https://github.com/lmangani/chdb-discord-bot"
homepage: "https://deta.space"
---

With this, you can run your own instance of a chDB/ClickHouse Discord bot.

### Installation steps:
1. First install the app.
2. Enter the required environment variables:
    - `DISCORD_APPLICATION_ID` - Your discord app's ID.
    - `DISCORD_PUBLIC_KEY` - Your discord app's public key.
    - `DISCORD_BOT_TOKEN` - Your bot's token.
    - `CHDB_API` - Custom chDB/ClickHouse HTTP/S API URL.
3. Set the `Interactions Endpoint URL` in your discord app's general information to `<micro_url>/bot/interactions`.
4. Visit `<micro_url>/bot/api/dash/<token>` to register the slash commands for the first time.

Run `/ping` to make sure it's working! Enjoy!
