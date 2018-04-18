import json
import requests

from discord import Colour, Embed
from config import config

DANBOORU_API = "http://danbooru.donmai.us/posts.json?limit=1&random=true&tags={}"
login = config["danbooru_login"]
api_key = config["danbooru_apikey"]


def generate_help_string():
    help = "UNDER CONSTRUCTION"
    return help


async def get_lewd(term, bot):
    try:
        res = requests.get(DANBOORU_API.format(term), auth=(login, api_key)).content
        parsed = json.loads(res)
        img_url = parsed[0]
        return img_url["file_url"]
        
    except:
        await bot.say("Something happened ;^)")


def create_command(bot):

    @bot.command(pass_context=True, brief="Random lewd image for you. Courtesy of danbooru.donmai.us", help=generate_help_string())
    async def lewd(ctx, *, term):
        lewd = await get_lewd(term, bot)

        embed = Embed()
        embed.type = "rich"
        embed.colour = Colour.magenta()

        embed.set_image(
            url=lewd
        )
        await bot.say(None, embed=embed)
