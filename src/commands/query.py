import os
import discohook
import requests


api_url = os.getenv('CHDB_API', 'https://chdb.fly.dev')

formats = ['CSV', 'CSVWithNames', 'TSV', 'TSVWithNames', 'JSONCompact']

options = [
  discohook.StringOption('query', 'Type your chdb SQL query here.', required = True),
  discohook.StringOption('format', 'Choose the response format.', choices = formats)
]

@discohook.command('query', 'Query chDB!', options = options)
async def query_command(interaction, query, format):

  await interaction.defer() # because it takes more than 3 seconds!

  if not format:
    format = formats[-1]

  params = { "default_format": format }
  headers =  {"Content-Type":"text/plain;charset=UTF-8"}
  response = requests.post(api_url, params=params, data=query, headers=headers)

  await interaction.followup(response.content.decode("utf-8"))
