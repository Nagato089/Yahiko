import discord
from discord import app_commands
from discord.ext import commands

# 1. Setup the Bot
TOKEN = 'MTUwMDAyMzY4NzgxNzA3Mjc3MQ.GQbmZC.0GncuZLccxbt7OSp98f86LPFkVmOCGBmSQX-7s'
intents = discord.Intents.default()
intents.members = True  # Required to see members

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Syncs the slash commands with Discord
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

bot = MyBot()

# 2. The Nickname Command
@bot.tree.command(name="nick", description="Change a member's nickname")
@app_commands.describe(member="The member to change", new_nickname="The new name")
async def nick(interaction: discord.Interaction, member: discord.Member, new_nickname: str):
    try:
        await member.edit(nick=new_nickname)
        await interaction.response.send_message(f"Successfully changed {member.mention}'s nickname to **{new_nickname}**!")
    except discord.Forbidden:
        await interaction.response.send_message("I don't have permission to change that user's nickname. (Check role hierarchy!)", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)

bot.run(TOKEN)
