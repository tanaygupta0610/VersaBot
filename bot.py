import discord,aiohttp
from bs4 import BeautifulSoup
from discord.ext import commands
from discord import app_commands
import ApiFun, ButtonClass,config
#m_server_id =Enter the server id here

guildid=discord.Object(id=config.serverid)
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
            guild = discord.Object(id=serverid)
            synced = await self.tree.sync(guild=guild)
        except Exception as e:
            print(f'Error is {e}')
    async def on_message(self, message):
        if message.author == self.user:
            return
        if(message.content.startswith("hello")):
            await message.channel.send(f'Hi sweetheart{message.author}')

intents=discord.Intents.default()
intents.messages = True
intents.message_content=True
client = Client(command_prefix="/", intents=intents)


serverid =0 #enter theserver id
helplist = "/hello -Says hello to Sh and T  \n /our_list - Sends the link of our playlist <3 \n /purpose - The purpose of my creation \n /help - To give this response "

@client.tree.command(name="hello", description="Says hello to Sh and T", guild=discord.Object(id=serverid))
async def sayshello(interaction: discord.Interaction, us: str):
    await interaction.response.send_message("Hi sweetheart "+us+" how are you doing?")


@client.tree.command(name="our_list", description="Send the link of our playlist <3", guild=discord.Object(id=serverid))
async def playlist(interaction: discord.Interaction,):
    await interaction.response.send_message("Hi sweetheart, here's our playlist link - "+" "+config.playlist_link)


@client.tree.command(name="purpose", description="The purpose of my creation", guild=discord.Object(id=serverid))
async def create(interaction: discord.Interaction,):
    await interaction.response.send_message("Hi, I was created by @sabmohmaayahai9462 on 31st March at around 2am."+". I was created to bring joy to the server :-( .")


@client.tree.command(name="motivation", description="Delivers a random motivational quote", guild=discord.Object(id=serverid))
async def motivation(interaction: discord.Interaction,):
    await interaction.response.send_message(ApiFun.motivation())


@client.tree.command(name="help", description="List commands", guild=discord.Object(id=serverid))
async def help(interaction: discord.Interaction,):
    await interaction.response.send_message(embed=ApiFun.help_msg())


@client.tree.command(name="compliment_shris", description="Gives a personalized compliment to Shristi.", guild=discord.Object(id=serverid))
async def complimentshris(interaction: discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.ComplimentSh())

@client.tree.command(name="compliment_tan", description="Gives a personalised compliment to Tanay", guild=discord.Object(id=serverid))
async def complimenttan(interaction: discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.ComplimentT())


@client.tree.command(name="say", description="Say anything", guild=discord.Object(id=serverid))
async def say(interaction: discord.Interaction, user: discord.Member, msg: str):
    await interaction.response.send_message(f"{interaction.user.mention} says to {user.mention} - '{msg}'")


@client.tree.command(name="youtube", description="goes to youtube", guild=discord.Object(id=serverid))
async def yt(interaction: discord.Interaction):
    embed = discord.Embed(title="Subscribe to my channel", url="https://www.youtube.com/channel/UCjB0O3-nx5YL_8l03JlYBeg/featured",
                          description="This is Tanay Gupta's Vlogging channel, pls subscribe", color=discord.Color.red())
    embed.set_thumbnail(url="")
    await interaction.response.send_message(embed=embed)

@client.tree.command(name="weather", description="Tells you about the weather in your city", guild=discord.Object(id=serverid) )
async def weather_fun(interaction:discord.Interaction, city:str):
    if "error" in ApiFun.get_weather(city):
        await interaction.response.send_message("Error occured - "+ApiFun.get_weather(city)["error"]["message"])
    else:
        await interaction.response.send_message(ApiFun.call_weather(city))

@client.tree.command(name="recipe_random",description="suggests a random recipe",guild=discord.Object(id=serverid))
async def recipe(interaction:discord.Interaction):
    await interaction.response.send_message(view=ButtonClass.Recipe())

@client.tree.command(name="recipes_by_category",description="gives list of all the recipes by a category",guild=discord.Object(id=serverid))
async def recipebycategories(interaction:discord.Interaction,):
    await interaction.response.send_message("Please choose a category to view all the recipes of it - \n ",view=ButtonClass.RecipesByCat())

@client.tree.command(name="recipe_by_search",description="gives list of categories",guild=discord.Object(id=serverid))
async def recipebysearch(interaction:discord.Interaction,meal:str):
    await interaction.response.send_message(ApiFun.meal_search(meal))

@client.tree.command(name="random_recipe_by_category",description="suggests a random recipe",guild=discord.Object(id=serverid))
async def recipecategoryrandom(interaction:discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.RecipeByCat())

@client.tree.command(name="random_number_fact",description="Gives a fact about a random number",guild=discord.Object(id=serverid))
async def random_number(interaction:discord.Interaction):
    await interaction.response.send_message(ApiFun.random_number_fact())

@client.tree.command(name="number_fact",description="Gives a fact about a number",guild=discord.Object(id=serverid))
async def number(interaction:discord.Interaction,num:int):
    await interaction.response.send_message(ApiFun.number_fact(num))

@client.tree.command(name="love_quote",description="Gives a random love quote",guild=discord.Object(id=serverid))
async def lovequote(interaction:discord.Interaction):
    await interaction.response.send_message(ApiFun.love_quote())

@client.tree.command(name="pickup_lines",description="generates a random pickup line", guild=discord.Object(id=serverid))
async def pickup(interaction:discord.Interaction,user:discord.Member):
    await interaction.response.send_message(user.mention+" "+config.pickup_line())

@client.tree.command(name="horoscope",description="suggests a random recipe",guild=discord.Object(id=serverid))
async def horoscope_fun(interaction:discord.Interaction,sunsign:str):
    await interaction.response.send_message("This is currently under development")

@client.tree.command(name="apologise",description="Gives you two options to apologise to",guild=guildid)
async def mybutton(interaction:discord.Interaction,):
    await interaction.response.send_message(view=ButtonClass.Apology())
@client.tree.command(name="bore",description="Get a random suggestion",guild=guildid)
async def bore(interaction:discord.Interaction):
    await interaction.response.send_message(view=ButtonClass.Bore())
@client.tree.command(name="truth_dare",description="Play truth and dare",guild=guildid)
async def truthdare(interaction:discord.Interaction):
    await interaction.response.send_message("Truth or Dare, choose below",view=ButtonClass.TruthDare(config.rotate_bottle(interaction)))
@client.tree.command(name="lyrics",description="Search for lyrics of a song by artist",guild=guildid)
async def lyrics_fetch(interaction:discord.Interaction,artist:str,song:str):
    await interaction.response.send_message(ApiFun.lyrics(artist,song))
@client.tree.command(name="dog_random",description="Sends a picture of a random dog",guild=guildid)
async def dog(interaction:discord.Interaction):
    await interaction.response.send_message(embed=ApiFun.dogapi())
@client.tree.command(name="roast",description="Roasts you personally",guild=guildid)
async def roast(interaction:discord.Interaction):
    await interaction.response.send_message(view=ButtonClass.Roast())
@client.tree.command(name="check_user",description="Gives online offline status of a user",guild=guildid)
async def find(interaction:discord.Interaction,user:discord.Member):
    await interaction.response.send_message(ApiFun.checkusr(user))
@client.tree.command(name="flip",description="Flip a coin",guild=guildid)
async def flip(interaction:discord.Interaction):
    await interaction.response.send_message(embed=ApiFun.flip())
@client.tree.command(name="role",description="Check roles",guild=guildid)
async def roles(interaction:discord.Interaction,user:discord.Member):
    await interaction.response.send_message(str(user.roles))
@client.tree.command(name="fullform_name",description="Gives you compliments/positive words corresponding to each letter in your name",guild=guildid)
async def fullform(interaction:discord.Interaction,name:str):
    await interaction.response.send_message(config.create_fullform(name))
@client.tree.command(name="random_music_by_genre",description="Gives you music recommendations",guild=guildid)
async def random_music_by_genre(interaction:discord.Interaction,genre:str,limit:int):
    recommendations=ApiFun.musicrecbygen(genre,limit)
    await interaction.response.send_message(ApiFun.format_rec(recommendations=recommendations))
@client.tree.command(name="random_music_by_artist",description="Gives you music recommendations",guild=guildid)
async def random_music_by_artist(interaction:discord.Interaction,artist:str,limit:int):
    recommendations=ApiFun.get_random_recommendation_by_artist(artist,limit)
    await interaction.response.send_message(ApiFun.format_rec(recommendations=recommendations))
@client.tree.command(name="dictionary",description="Gives you definitions of a word",guild=guildid)
async def dictionary(interaction:discord.Interaction,word:str):
    await interaction.response.send_message(ApiFun.dic(word))
async def bolo(interaction:discord.Interaction,msg:str):
    await interaction.response.send_message(interaction.user.mention+" says '"+msg+"'")
@client.tree.command(name="synonyms",description="Gives you synonyms of a word",guild=guildid)
async def synonym(interaction:discord.Interaction,word:str):
    await interaction.response.send_message(ApiFun.syn(word))
@client.tree.command(name="birthday",description="Gives you time remaining for the birthday",guild=guildid)
async def birthday_function(interaction: discord.Interaction,user:discord.Member,year:int,month:int,day:int):
    await interaction.response.send_message(embed=config.countdown(user,year,month,day))
@client.tree.command(name="askai",description="Gives you an AI generated response of the input prompt",guild=guildid)
async  def askai(interaction:discord.Interaction,msg:str):
    await interaction.response.send_message(ApiFun.askai(msg))
client.run(config.token)
#<@> or <@userid> to mention a usercls
