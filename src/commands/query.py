import os
import discohook
import requests

api_url = os.getenv('CHDB_API', 'https://chdb.fly.dev')

format_csv = discohook.Choice(name="csv", value="CSV")
format_csv_name = discohook.Choice(name="csv_name", value="CSVWithNames")
format_tsv = discohook.Choice(name="tsv", value="TSV")
format_tsv_name = discohook.Choice(name="tsv_name", value="TSVWithNames")
format_json = discohook.Choice(name="json", value="JSONCompact")
formats = [format_csv, format_csv_name, format_tsv, format_tsv_name, format_json]

options = [
    discohook.StringOption('query', 'Type your chdb SQL query here.', required=True),
    discohook.StringOption('format', 'Choose the response format.', choices=formats)
]


@discohook.command('query', 'Query chDB!', options=options)
async def query_command(interaction, query, format):
    await interaction.defer()  # because it takes more than 3 seconds!

    if not format:
        format = formats[-1]

    params = {"default_format": format.value}
    headers = {"Content-Type": "text/plain;charset=UTF-8"}
    response = requests.post(api_url, params=params, data=query, headers=headers)
    if response.status_code != 200:
        await interaction.followup("Server error with unsupported format, status_code: {0}".format(response.status_code))
        return
    if len(response.content) == 0:
        await interaction.followup("Query error")
        return

    await interaction.followup(response.content.decode("utf-8"))
