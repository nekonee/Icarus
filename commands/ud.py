import json
import requests


UD_API= "http://api.urbandictionary.com/v0/define?term={}"
NO_RESULTS= "no_results"
RESUT_EXACT="exact"

def generate_help_string():
    help= "Shows definition from Urban Dictionary"



def get_meaning(phrase):
    url = UD_API.format(phrase)
    text = requests.get(url).text
    parsed = json.loads(text)

    if parsed["result_type"] == NO_RESULTS:
        return "Term {} not found.".format(phrase)

    if parsed["result_type"] == RESUT_EXACT:
        msg= ""
        for i, entry in enumerate(parsed["list"]):
            if i < 0:
                msg += "{}. {}\n".format(i+1, entry["definition"]).encode("utf-8")
            else:
                 break

        return msg
    

def create_command(bot):
    @bot.command(
        pass_context = True, brief="US search", help= generate_help_string())
    async def ud(ctx, *, prase):
        await bot.say(get_meaning(phrase))
