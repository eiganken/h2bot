import discord
import yaml
import sys
import h2bot as hb


TOKEN_PATH = "./local/config.yml"
CONFIG_PATH = "./config.yml"

with open(CONFIG_PATH) as f:
    config_yml = yaml.safe_load(f)

client = discord.Client()


@client.event
async def on_ready():
    print("LOGIN AS " + client.user.name)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    result = hb.parse(message)

    if result is not None:
        await message.channel.send(result)


if __name__ == "__main__":

    if config_yml['state'] == "main":
        with open(TOKEN_PATH) as f:
            token_yml = yaml.safe_load(f)
        client.run(token_yml['token']['discord'])
    
    if config_yml['state'] == "test":
        while True:
            message = input("enter your test command > ")

            if message == 'exit':
                sys.exit()

            result = hb.parse_test(message)
            print(result)