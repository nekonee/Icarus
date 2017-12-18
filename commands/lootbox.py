import random
import time

from discord import Colour, Embed

lootbox_contents = open("data/lootbox.txt").readlines()

def create_command(bot):

    @bot.command(pass_context=True, brief="Opens a random lootbox for you")
    async def lootbox(ctx):
        await bot.say("{} is opening a loot box... :gift:".format(ctx.message.author.mention))
        time.sleep(3)

        embed = Embed()
        embed.type = "rich"
        embed.color = Colour.gold()
        embed.add_field(
            name="The contents are yours...",
            value=random.choice(lootbox_contents)
        )
        embed.set_footer(
            text= "A boon, at last! "
        )
        await bot.say(None, embed=embed)
