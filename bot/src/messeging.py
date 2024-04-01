import discord
import requests

from bot.src.settings import settings

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'hello':
        response = "Hello, I'm a bot!"
        await message.channel.send(response)
    elif message.content.startswith('pokemon'):
        pokemon_name = message.content[len('pokemon'):].strip()
        if pokemon_name:
            req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
            if req.status_code == 200:
                pokemon_data = req.json()
                pokemon_id = pokemon_data.get('id')
                pokemon_type = pokemon_data.get('types')[0].get('type').get('name')
                await message.channel.send(
                    f"Pokemon found!\nName: {pokemon_name.capitalize()}\nID: {pokemon_id}\nType: {pokemon_type}")
            else:
                await message.channel.send(f"Sorry, I couldn't find information about the pokemon '{pokemon_name}'.")
        else:
            await message.channel.send("Please provide the name of the Pokemon after the 'pokemon' keyword.")


if __name__ == '__main__':
    client.run(settings.DISCORD_TOKEN)
