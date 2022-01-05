from redbot.core import Config
from redbot.core import commands
import urllib.request
import discord

class FactionsMC(commands.Cog):
    """A cog to make embeds for factions"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier = 26282562630)
        default_guild = {
            "fchannel": None,
            "url": "https://raw.githubusercontent.com/Yuuki2628/TL-Cogs/main/MinecraftFactions/factions.txt"
        }

        self.config.register_guild(**default_guild)

    @commands.group(pass_context=True)
    @commands.guild_only()
    async def factions(self, ctx):
        """All the commands of the cog are under this group"""
        pass

    @factions.command(name="update")
    @commands.guild_only()
    async def update_channel(self, ctx):
        """Updates or displays the factions on the selected channel"""
        achannel = await self.config.guild(ctx.guild).fchannel()
        if achannel is None:
            return await ctx.send("Please setup a channel before using this command")

        for channel in ctx.guild.channels:
            if channel.id == achannel:
                fchannel = channel
                break

        #reads the data from the github page
        url = await self.config.guild(ctx.guild).url()
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode('utf-8')
        factions = [i.split(',') for i in text.split(';')]

        await ctx.send(arr[0])
        await ctx.send(arr[1][2])

        count = 0
        async for _ in fchannel.history(limit=None):
            count += 1

        await fchannel.purge(limit=count)

        factionName = [i[0] for i in factions]

        for i in range(factionName.length):
            color = members[i][1]
            members = factions.pop[i][0]
            members = members.pop[1]

            membersField = members.join('\n')
            embed = discord.Embed(title=factionName,color=color)
            embed.add_field(title="Faction members:",value=membersField)

            await fchannel.send(embed=embed)

        return

    @factions.command(name="setchannel")
    @commands.guild_only()
    async def setc_hannel(self, ctx, ch: discord.TextChannel = None):
        """Set the channel where you want the factions to be shown"""
        if ch == None:
            return await ctx.send("Set the channel where you want the factions to be shown")
        await self.config.guild(ctx.guild).fchannel.set(ch.id)
        return await ctx.send(f"The faction channel has been set to {ch.mention}!")
