import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('text to send')
      print(f"[>] Messaged: {user.name}")
    except:
       print(f"[-] Couldnt Message: {user.name}")

client.run('token here', bot=False)
