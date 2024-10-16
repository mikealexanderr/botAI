import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')

            nama, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')

            if nama == "kupu-kupu\n" and skor >= 0.65:
                await ctx.send("Ini adalah kupu-kupu!")
                await ctx.send("Kupu-kupu mempunyai warna yang sangat indah dan cerah!")
                await ctx.send("Kupu-kupu pada umumnya beraktivitas pada siang hari.")
            elif nama == "ngengat\n" and skor >= 0.65:
                await ctx.send("Ini adalah ngengat!")
                await ctx.send("Ngengat mempunyai warna yang cenderung kusam.")
                await ctx.send("Ngengat pada umumnya beraktivitas pada malam hari.")
            else:
                await ctx.send("GAMBAR YANG DIKIRIM TIDAK DIKENALI  ")
    
    else:
        await ctx.send("TIDAK ADA FILE YANG DIKIRIMKAN")


