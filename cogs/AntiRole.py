import discord
import json
from discord.ext import commands
import datetime

class AntiRole(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
      with open('whitelisted.json') as f:
        whitelisted = json.load(f)
      async for i in role.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.role_create):
        if i.user.bot:
            return
      
        if str(i.user.id) in whitelisted[str(role.guild.id)]:
            return
    
        await role.guild.kick(i.user, reason="Antinuke: Creating Roles")
        return
        
    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
      with open('whitelisted.json') as f:
        whitelisted = json.load(f)
      async for i in role.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.role_delete):
          if i.user.bot:
              return
      
          if str(i.user.id) in whitelisted[str(role.guild.id)]:
              return
    
          await role.guild.kick(i.user, reason="Antinuke: Deleting Roles")
          return

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
      with open('whitelisted.json') as f:
        whitelisted = json.load(f)
      async for i in after.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.role_update):
      
