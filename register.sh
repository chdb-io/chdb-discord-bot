#!/bin/bash

DISCORD_BOT_TOKEN="${DISCORD_BOT_TOKEN:-0000000000000000000000000000000000000}"
DISCORD_APPLICATION_ID="${DISCORD_APPLICATION_ID:-0000000000000000}"

# /ping command
curl -X POST \
-H 'Content-Type: application/json' \
-H "Authorization: Bot $DISCORD_BOT_TOKEN" \
-d '{"name":"ping","description":"ping a bot","options":[]}' \
"https://discord.com/api/v8/applications/$DISCORD_APPLICATION_ID/commands"

# /query command
curl -X POST \
-H 'Content-Type: application/json' \
-H "Authorization: Bot $DISCORD_BOT_TOKEN" \
-d '{"name":"query","description":"Run a chdb SQL query","options":[{"name":"query","description":"SQL query","type":3,"required":true},{"name":"format","description":"Query output format","type":3,"required":false}]}' \
"https://discord.com/api/v8/applications/$DISCORD_APPLICATION_ID/commands"
