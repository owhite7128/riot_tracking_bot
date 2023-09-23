import requests
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

client = commands.Bot(command_prefix="!", intents=Intents.default())
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

guild_ids = [{guild_id}]

@slash.slash(name="judeLP",description="Find out what LP Jude is At", guild_ids=guild_ids)
async def judeLP(ctx: SlashContext):
    r = requests.get("http://localhost:5000/api/v1/api_key")
    json_r = r.json()
    key = json_r["api_key"]
    id = json_r["summoner_id"]
    riot_one = requests.get(f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{id}", headers={"X-Riot-Token":key})
    json_riotone = riot_one.json()
    summ_id = json_riotone["id"]
    riot_two = requests.get(f"https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summ_id}", headers={"X-Riot-Token":key})
    json_riottwo = riot_two.json()
    jude = json_riottwo[0]
    tier = jude["tier"]
    rank = jude["rank"]
    lp = jude["leaguePoints"]
    descript = f"Jude is {tier} {rank} with {lp} LP!!"

    embed = Embed(title="What LP is Jude At?", description=f"{descript}")
    await ctx.send(embed=embed)

client.run("{discord_bot_token")