import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est connecté !")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commandes synchronisées.")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="bienvenue")
    if channel:
        await channel.send(
            f"🐉 Bienvenue {member.mention} sur **Éclipse Des Dragons** ! 💜"
        )

@bot.tree.command(name="ping", description="Vérifie si le bot est en ligne.")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong ! Je suis bien en ligne.")

bot.run(TOKEN)
@bot.tree.command(name="bonjour", description="Le bot te dit bonjour.")
async def bonjour(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"👋 Bonjour {interaction.user.mention} ! Bienvenue sur **Éclipse Des Dragons** 🐉💜"
    )