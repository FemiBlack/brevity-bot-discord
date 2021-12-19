import os
import asyncio
import random

import discord

TOKEN = os.environ.get("TOKEN")


class MyClient(discord.Client):
	async def on_ready(self):
		print(f"Logged in as {self.user} (ID: {self.user.id})")
		print("------")

	async def on_member_join(self, member):
		guild = member.guild
		await member.create_dm()
		await member.dm_channel.send(
		    f'Hi {member.name}, welcome to my Discord server!')
		if guild.system_channel is not None:
			to_send = f"Welcome {member.mention} to {guild.name}!"
			await guild.system_channel.send(to_send)

	async def on_message(self, message):
		# we do not want the bot to reply to itself
		if message.author.id == self.user.id:
			return

		if message.content.startswith("$guess"):
			await message.channel.send(
			    "Guess a number between 1 and 10 in 5 seconds.")

			def is_correct(m):
				return m.author == message.author and m.content.isdigit()

			answer = random.randint(1, 10)

			tries = 0
			hit = False
			while not hit:
				if tries == 3:
					await message.channel.send("You have exceeded 3 trials")
					break
				try:
					guess = await self.wait_for("message",
					                            check=is_correct,
					                            timeout=5.0)
				except asyncio.TimeoutError:
					return await message.channel.send(
					    f"Sorry, you took too long it was {answer}.")

				if int(guess.content) == answer:
					hit = True
					await message.channel.send("You are right!")
					break
				elif int(guess.content) < answer:
					await message.channel.send(
					    f"Close!, the number is larger than {guess.content}.")
					tries += 1
				elif int(guess.content) > answer:
					await message.channel.send(
					    f"Close, the number is less than {guess.content}")
					tries += 1
				else:
					await message.channel.send(
					    f"Oops. It is actually {answer}.")


intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
client.run(TOKEN)
