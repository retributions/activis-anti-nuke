import datetime
start_time = datetime.datetime.utcnow()
import discord
import keep_alive
keep_alive.keep_alive()
import os
import asyncio
import os.path

import json
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

from cogs.AntiChannel import AntiChannel
from cogs.AntiRemoval import AntiRemoval
from cogs.AntiRole import AntiRole



def is_allowed(ctx):
    return ctx.message.author.id == 759109429458894928


def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 759109429458894928



client = commands.Bot(command_prefix = '>')
client.remove_command("help")


client.add_cog(AntiChannel(client))
client.add_cog(AntiRemoval(client))
client.add_cog(AntiRole(client))

@client.listen("on_guild_join")
async def update_json(guild):
    with open ('whitelisted.txt', 'r') as f:
        whitelisted = json.load(f)


    if str(guild.id) not in whitelisted:
      whitelisted[str(guild.id)] = []


    with open ('whitelisted.txt', 'w') as f: 
        json.dump(whitelisted, f, indent=4)

@client.command(aliases = ['wld'], hidden=True)
async def whitelisted(ctx):

  embed = discord.Embed(title=f"Whitelisted users for {ctx.guild.name}", description="")

  with open ('whitelisted.txt', 'r') as i:
        whitelisted = json.load(i)
  try:
    for u in whitelisted[str(ctx.guild.id)]:
      embed.description += f"<@{(u)}> - {u}\n"
    await ctx.send(embed = embed)
  except KeyError:
    await ctx.send("Nothing found for this guild!")

@client.command(aliases = ['wl'], hidden=True)
@commands.check(is_server_owner)
async def whitelist(ctx, user: discord.Member = None):
    if user is None:
        await ctx.send("You must specify a user to whitelist.")
        return
    with open ('whitelisted.txt', 'r') as f:
        whitelisted = txt.load(f)


    if str(ctx.guild.id) not in whitelisted:
      whitelisted[str(guild.id)] = []
    else:
      if str(user.id) not in whitelisted[str(ctx.guild.id)]:
        whitelisted[(ctx.guild.id)].append(str(user.id))
      else:
        await ctx.send("That user is already in the whitelist.")
        return



    with open ('whitelisted.txt', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
    
    await ctx.send(f"{user} has been added to the whitelist.")

@client.command(aliases = ['uwl'], hidden=True)
@commands.check(is_server_owner)
async def unwhitelist(ctx, user: discord.User = None):
  if user is None:
      await ctx.send("You must specify a user to unwhitelist.")
      return
  with open ('whitelisted.txt', 'r') as f:
      whitelisted = txt.load(f)
  try:
    if str(user.id) in whitelisted[str(ctx.guild.id)]:
      whitelisted[str(ctx.guild.id)].remove(str(user.id))
      
      with open ('whitelisted.txt', 'w') as f: 
        json.dump(whitelisted, f, indent=4)
    
      await ctx.send(f"{user} has been removed from the whitelist.")
  except KeyError:
    await ctx.send("This user was never whitelisted.")

@client.command()   
async def help(ctx):
  embed = discord.Embed(description=f"**Categories (7)**")
  embed.add_field(name="``ANTI``", value="Shows Anti Commands", inline=False)
  embed.add_field(name="``ADMIN``", value="Shows Admin Commands", inline=False)
  embed.add_field(name="``TRAVIS``", value="Shows Travis Commands", inline=False)
  embed.add_field(name="``SERVER``", value="Shows Server Commands", inline=False)
  embed.add_field(name="``MISC``", value="Shows Misc Commands", inline=False)
  embed.add_field(name="``FUN``", value="Show Fun Commands", inline=False)
  embed.add_field(name="``>[category]``", value=f"Made By <@759109429458894928> & <@774729890251538432>", inline=False)
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/743233650975309894/759418643104268319/giphy_19.gif?format=png')
  embed.set_footer(text='7 Categories | 6 Commands')
  await ctx.send(embed=embed)

@client.command()   
async def anti(ctx):
  embed = discord.Embed(description=f"")
  embed.add_field(name="``whitelist``", value="Keeps User Safe From Being Affected By Antiwizz Modules", inline=False)
  embed.add_field(name="``unwhitelist``", value="Removes User From Being Whitelisted", inline=False)
  embed.add_field(name="``whitelisted``", value="Lists The Whitelisted Users In Your Guild", inline=False)
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/743233650975309894/759418643104268319/giphy_19.gif?format=png')
  await ctx.send(embed=embed)

@client.command()   
async def server(ctx):
  embed = discord.Embed(description=f"")
  embed.add_field(name="``serverinfo``", value="", inline=False)
  embed.add_field(name="``channelinfo``", value="", inline=False)
  embed.add_field(name="``roleinfo``", value="", inline=False)
  embed.add_field(name="``banner``", value="", inline=False)
  embed.add_field(name="``membercount``", value="", inline=False)
  embed.add_field(name="``servericon``", value="", inline=False)
  embed.add_field(name="``invitebackround``", value="", inline=False)
  embed.add_field(name="``invite``", value="", inline=False)
  embed.add_field(name="``emote``", value="", inline=False)
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/743233650975309894/759418643104268319/giphy_19.gif?format=png')
  embed.set_footer(text='7 Categories | 6 Commands')
  await ctx.send(embed=embed)

@client.command()   
async def invite(ctx):
  embed = discord.Embed(description=f"")
  embed.add_field(name="**My Bot Invite**", value="https://discord.com/api/oauth2/authorize?client_id=779969792378798101&permissions=8&scope=bot", inline=False)
  embed.set_thumbnail(url='https://media.discordapp.net/attachments/743233650975309894/759418643104268319/giphy_19.gif?format=png')
  await ctx.send(embed=embed)

@client.command()
async def membercount(ctx):
    await ctx.send(embed=discord.Embed(title="Travis Membercount", description=f"{len(client.guilds)} servers, {len(client.users)} users | Database is connected"))


@client.command()
async def uptime(ctx): 
    await ctx.message.delete()
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')

@client.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send('Pong!')

client.run('Nzk1NTEyNjYzODgyOTg5NTk4.X_Kc5g.jP6GvnZ-JYWIFgWm1TZOPAYyBoU')
