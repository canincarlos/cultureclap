# SUPER great tutorial by FreeCodeCamp
# https://www.youtube.com/watch?v=SPTfmiYiuok

from pprint import pprint as ppr

import discord
import tweepy

import token


BOT_TOKEN = token.bot_tech
SERVER_ID = token.server

tweetle = tweepy.Client(
    consumer_key=tw_consumer_key,
    consumer_secret=tw_consumer_secret,
    access_token=tw_access_token,
    access_token_secret=tw_access_secret
)

intents = discord.Intents(reactions=True)
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print("We've logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
# 	if message.author == client.user:
# 		return

# 	msg = message.content

# 	if msg.startswith("$tweet") and message.channel.name == "auto-tweet":
# 		d = {}
# 		d['message_id'] = message.id
# 		d['message_content'] = message.content[7:]
# 		d['message_reactions'] = message.reactions
# 		d['author_name'] = message.author.name
# 		d['author_id'] = message.author.id
# 		d['author_disc'] = message.author.discriminator
# 		ppr(d)
# 		await message.channel.send(message.author.name)

@client.event
async def on_raw_reaction_add(payload):
	if payload.user_id == client.user.id:
		return
	if payload.guild_id != SERVER_ID:
		print("wrong server")
		return
		
	channel = await client.fetch_channel(int(payload.channel_id))
	print('zoom zoom', payload)
	if channel.name == "auto-tweet":
		channel = await client.fetch_channel(payload.channel_id)
		message = await channel.fetch_message(payload.message_id)
		reacts = message.reactions
		userList = []
		for react in reacts:
			users = await react.users().flatten()
			for u in users: userList.append(u)
			# print(react.emoji.encode('utf-8'))
		nul = []
		for user in userList: nul.append(user.id)
		if len(set(nul)) > 80:
			tweetle.create_tweet(text=message.content[7:])

client.run(BOT_TOKEN)