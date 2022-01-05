from redbot.core import Config
from redbot.core import commands
import discord

class FactionsMC(commands.Cog):
    """A cog to make embeds for factions"""

    def __init__(self):
        self.config = Config.get_conf(self, identifier = 26282562630)
        default_guild = {
            "factions": [],
            "fmembers": [[]],
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
        """Displays the factions on the selected channel"""
        fchannel = await self.config.guild(ctx.guild).fchannel()
        if fchannel is None:
            await ctx.send("Please setup a channel before using this command")

        #reads the data from the github page
        url = await self.config.guild(ctx.guild).url()
        response = urlopen(url)
        data = response.read()
        arr = [i.split(',') for i in text.split(';')]

        print(arr[0])
        print(arr[1,2])

        """factions = await self.config.guild(ctx.guild).factions()
        members = await self.config.guild(ctx.guild).fmembers()

        count = 0
        async for _ in fchannel.history(limit=None):
            count += 1

        await fchannel.purge(count)

        for i in range(factions.length):
            factionName = members[i][0]
            members = members.pop[0]

            color = members[i][1]
            members = members.pop[1]

            membersField = members.join('\n')
            embed = discord.Embed(title=factionName,color=color)
            embed.add_field(title="Faction members:",value=membersField)

            await fchannel.send(embed=embed)"""

        return