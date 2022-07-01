import discord
from discord.ext import commands
class BoostPlugin(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        print(message.type)
        if message.type == discord.MessageType.premium_guild_subscription:
            embed = discord.Embed(title=f"**Ding ding! We got a new booster!**", description=f"Thank you so much for boosting ﹫: s. effects. ˀ ⸝⸝ ％! Our server perks are pinned in the pinned messages! <3.
", color=0xff0000)
                embed.set_thumbnail(url="https://i.pinimg.com/564x/1e/41/7c/1e417c8e8fbe94dd90ba8e3244a2acf2.jpg")
                embed.set_footer(text="perks are in the pinned msg in this channel :) dm owner to claim.")
            m = await message.channel.send(embed=embed)
            await m.add_reaction("<a:Heartanimated:707510241276985425>")
            
def setup(bot):
    bot.add_cog(BoostPlugin(bot))
