from logging.handlers import RotatingFileHandler

import discord,redis
from discord.ext import commands
import ApiFun, ButtonClass,config

guild_id=discord.Object(id=config.serverid)
#Logger setup
'''
def setup_logging():
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)  # Log INFO and higher

    # Format: [ISO Time] [Level] [Command] User123: Message (Guild: 123)
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s (User: %(user_id)s | Guild: %(guild_id)s)",
        datefmt="%Y-%m-%dT%H:%M:%SZ"
    )

    # Rotating logs (5MB each, keep 3 backups)
    file_handler = RotatingFileHandler(
        filename="discord.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=3,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger

logger = setup_logging()
#m_server_id =Enter the server id here
'''
'''
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='sh/1.0'
)
''' 
    
class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        try:
            synced = await self.tree.sync(guild=guild_id)
        except Exception as e:
            print(f'Error is {e}')



intents=discord.Intents.default()
intents.messages = True
intents.message_content=True
client = Client(command_prefix="/", intents=intents)

helplist = "/hello -Says hello to Sh and T  \n /our_list - Sends the link of our playlist <3 \n /purpose - The purpose of my creation \n /help - To give this response "
'''
@client.event
async def on_interaction(interaction: discord.Interaction):
    #logs all the commands used by users in the server.
    if interaction.type == discord.InteractionType.application_command:
        logger.debug(
            f"Interaction: {interaction.data.get('name')}",
            extra={
                "user_id": interaction.user.id,
                "guild_id": interaction.guild.id if interaction.guild else "DM"
            }
        )
'''
@client.tree.command(name="hello", description="Says hello to Server", guild=guild_id)
async def sayshello(interaction: discord.Interaction, us: str):
    await interaction.response.send_message("Hi sweetheart "+us+" how are you doing?")

@client.tree.command(name="purpose", description="The purpose of my creation", guild=guild_id)
async def create(interaction: discord.Interaction,):
    await interaction.response.send_message("Hi, I was created by @sabmohmaayahai9462 on 31st March at around 2am."+". I was created to bring joy to the server :-( .")

@client.tree.command(name="motivation", description="Delivers a random motivational quote", guild=guild_id)
async def motivation(interaction: discord.Interaction,):
    await interaction.response.send_message(ApiFun.motivation())


@client.tree.command(name="help", description="List commands", guild=guild_id)
async def help(interaction: discord.Interaction,):
    await interaction.response.send_message(embed=ApiFun.help_msg())


@client.tree.command(name="compliment_shris", description="Gives a personalized compliment to Shristi.", guild=guild_id)
async def complimentshris(interaction: discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.ComplimentSh())

@client.tree.command(name="compliment_tan", description="Gives a personalised compliment to Tanay", guild=guild_id)
async def complimenttan(interaction: discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.ComplimentT())


@client.tree.command(name="say", description="Say anything", guild=guild_id)
async def say(interaction: discord.Interaction, user: discord.Member, msg: str):
    await interaction.response.send_message(f"{interaction.user.mention} says to {user.mention} - '{msg}'")


@client.tree.command(name="youtube", description="goes to youtube", guild=guild_id)
async def yt(interaction: discord.Interaction):
    embed = discord.Embed(title="Subscribe to my channel", url="https://www.youtube.com/channel/UCjB0O3-nx5YL_8l03JlYBeg/featured",
                          description="This is Tanay Gupta's Vlogging channel, pls subscribe", color=discord.Color.red())
    embed.set_thumbnail(url="")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="weather", description="Tells you about the weather in your city", guild=guild_id)
async def weather_fun(interaction:discord.Interaction, city:str):
    if "error" in ApiFun.get_weather(city):
        await interaction.response.send_message("Error occured - "+ApiFun.get_weather(city)["error"]["message"])
    else:
        await interaction.response.send_message(ApiFun.call_weather(city))

@client.tree.command(name="recipe_random",description="suggests a random recipe",guild=guild_id)
async def recipe(interaction:discord.Interaction):
    await interaction.response.send_message(view=ButtonClass.Recipe())

@client.tree.command(name="recipes_by_category",description="gives list of all the recipes by a category",guild=guild_id)
async def recipebycategories(interaction:discord.Interaction,):
    await interaction.response.send_message("Please choose a category to view all the recipes of it - \n ",view=ButtonClass.RecipesByCat())

@client.tree.command(name="recipe_by_search",description="gives list of categories",guild=guild_id)
async def recipebysearch(interaction:discord.Interaction,meal:str):
    await interaction.response.send_message(ApiFun.meal_search(meal))

@client.tree.command(name="random_recipe_by_category",description="suggests a random recipe",guild=guild_id)
async def recipecategoryrandom(interaction:discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.RecipeByCat())

@client.tree.command(name="random_number_fact",description="Gives a fact about a random number",guild=guild_id)
async def random_number(interaction:discord.Interaction):
    await interaction.response.send_message(ApiFun.random_number_fact())

@client.tree.command(name="number_fact",description="Gives a fact about a number",guild=guild_id)
async def number(interaction:discord.Interaction,num:int):
    await interaction.response.send_message(ApiFun.number_fact(num))

@client.tree.command(name="love_quote",description="Gives a random love quote",guild=guild_id)
async def lovequote(interaction:discord.Interaction):
    await interaction.response.send_message(ApiFun.love_quote())

@client.tree.command(name="pickup_lines",description="generates a random pickup line", guild=guild_id)
async def pickup(interaction:discord.Interaction,user:discord.Member):
    await interaction.response.send_message(user.mention+" "+config.pickup_line())

@client.tree.command(name="horoscope",description="suggests a random recipe",guild=guild_id)
async def horoscope_fun(interaction:discord.Interaction,sunsign:str):
    await interaction.response.send_message("This is currently under development")

@client.tree.command(name="apologise",description="Gives you two options to apologise to",guild=guild_id)
async def mybutton(interaction:discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.Apology())
@client.tree.command(name="bore",description="Get a random suggestion",guild=guild_id)
async def bore(interaction:discord.Interaction):
    await interaction.response.send_message(view=ButtonClass.Bore())
@client.tree.command(name="truth_dare",description="Play truth and dare",guild=guild_id)
async def truthdare(interaction:discord.Interaction):
    await interaction.response.send_message("Truth or Dare, choose below",view=ButtonClass.TruthDare(config.rotate_bottle(interaction)))
@client.tree.command(name="lyrics",description="Search for lyrics of a song by artist",guild=guild_id)
async def lyrics_fetch(interaction:discord.Interaction,artist:str,song:str):
    await interaction.response.send_message(ApiFun.lyrics(artist,song))
@client.tree.command(name="dog_random",description="Sends a picture of a random dog",guild=guild_id)
async def dog(interaction:discord.Interaction):
    await interaction.response.send_message(embed=ApiFun.dogapi())
@client.tree.command(name="roast",description="Roasts you personally",guild=guild_id)
async def roast(interaction:discord.Interaction):
    await interaction.response.send_message(view=ButtonClass.Roast())
@client.tree.command(name="check_user",description="Gives online offline status of a user",guild=guild_id)
async def find(interaction:discord.Interaction,user:discord.Member):
    await interaction.response.send_message(ApiFun.checkusr(user))
@client.tree.command(name="flip",description="Flip a coin",guild=guild_id)
async def flip(interaction:discord.Interaction):
    await interaction.response.send_message(embed=ApiFun.flip())
@client.tree.command(name="role",description="Check roles",guild=guild_id)
async def roles(interaction:discord.Interaction,user:discord.Member):
    await interaction.response.send_message(str(user.roles))
@client.tree.command(name="fullform_name",description="Gives you compliments/positive words corresponding to each letter in your name",guild=guild_id)
async def fullform(interaction:discord.Interaction,name:str):
    await interaction.response.send_message(config.create_fullform(name))
@client.tree.command(name="random_music_by_genre",description="Gives you music recommendations",guild=guild_id)
async def random_music_by_genre(interaction:discord.Interaction,genre:str,limit:int):
    recommendations=ApiFun.musicrecbygen(genre,limit)
    await interaction.response.send_message(ApiFun.format_rec(recommendations=recommendations))
@client.tree.command(name="random_music_by_artist",description="Gives you music recommendations",guild=guild_id)
async def random_music_by_artist(interaction:discord.Interaction,artist:str,limit:int):
    recommendations=ApiFun.get_random_recommendation_by_artist(artist,limit)
    await interaction.response.send_message(ApiFun.format_rec(recommendations=recommendations))
@client.tree.command(name="dictionary",description="Gives you definitions of a word",guild=guild_id)
async def dictionary(interaction:discord.Interaction,word:str):
    await interaction.response.send_message(ApiFun.dictionary(word))
async def bolo(interaction:discord.Interaction,msg:str):
    await interaction.response.send_message(interaction.user.mention+" says '"+msg+"'")
@client.tree.command(name="synonyms",description="Gives you synonyms of a word",guild=guild_id)
async def synonym(interaction:discord.Interaction,word:str):
    await interaction.response.send_message(ApiFun.syn(word))
@client.tree.command(name="birthday",description="Gives you time remaining for the birthday",guild=guild_id)
async def birthday_function(interaction: discord.Interaction,user:discord.Member,year:int,month:int,day:int):
    await interaction.response.send_message(embed=config.countdown(user,year,month,day))
@client.tree.command(name="askai",description="Gives you an AI generated response of the input prompt",guild=guild_id)
async def askai(interaction:discord.Interaction,msg:str):
    await interaction.response.defer()
    response=ApiFun.askai(str(interaction.user.id),msg)
    if len(response)>2000:
        chunks=[response[i:i+2000] for i in range(0,len(response),2000)]
        await interaction.followup.send(chunks[0])
        for chunk in chunks[1:]:
            await interaction.followup.send(chunk)
    else:
        await interaction.followup.send(response)
@client.tree.command(name="gmat",description="Gives you a random GMAT question to solve",guild=guild_id)
async def gmat(interaction:discord.Interaction):
    embed = discord.Embed(
        title="GMAT Practice Questions",
        description="Select a category to get started:",
        color=discord.Color.blue()
    )
    await interaction.response.send_message(embed=embed,view=ButtonClass.Gmat())
if __name__ =="__main__":
    client.run(config.token)
#<@> or <@userid> to mention a usercls
