import requests, json, random,discord,config
import pathlib
from openai import OpenAI
weather_key="#API key here"
def motivation():
    apiurl=apiurl = "https://zenquotes.io/api/random"
    response = requests.get(apiurl)
    if(response.status_code == 200):
        data = response.json()
        quote = f'Here is a quote for you "{data[0]["q"]}" - {data[0]["a"]}'
    else:
        quote = "Sorry could not retreive the quote at the moment."
    return quote
    
def get_weather(city):

def call_weather(city):
    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={weather_key}&q={city}&aqi=no"
        response = requests.get(url)
        weather = json.loads(response.text)
        name = weather['location']['name']
        region = weather['location']['region']
        country = weather['location']['country']
        local_time = weather['location']['localtime']
        temp = weather['current']['temp_c']
        cond = weather['current']['condition']['text']
        wind_kph = weather['current']['wind_kph']
        feelslike_c = weather['current']['feelslike_c']
        res="City: " + name + "\nRegion: " + region + "\nCountry: " + country + "\nLocal Time: " + str(
            local_time) + "\nTemperature: " + str(temp) + "℃" + "\nCondition: " + cond + "\nWind speed: " + str(
            wind_kph) + " kph" + "\nFeels like " + str(feelslike_c) + "℃"
    except Exception as e:
        res="Some error occured --> "+str(e)
    return res

def get_recipe():
    rec_link="https://www.themealdb.com/api/json/v1/1/random.php"
    try:
        response=requests.get(rec_link)
        json_data=response.json()
        meal_name=json_data["meals"][0]["strMeal"]
        meal_category=json_data["meals"][0]["strCategory"]
        meal_instructions=json_data["meals"][0]["strInstructions"]
        meal_youtube=json_data["meals"][0]["strYoutube"]
        meal_ingredients=""
        for i in range(1,21):
            index="strIngredient"+str(i)
            index2="strMeasure"+str(i)
            if(json_data["meals"][0][index]==""):
                break
            meal_ingredients+=json_data["meals"][0][index]+" "+json_data["meals"][0][index2]+"\n"
        meal_link=json_data["meals"][0]["strSource"]
        res=f"Meal Name: {meal_name}\n"
        f"Category: {meal_category}\n\n"
        f"Ingredients:\n{meal_ingredients}\n"
        f"Instructions:\n{meal_instructions}\n\n"
        f"Youtube Link: {meal_youtube}\n"
        f"Meal Link: {meal_link}"
    except Exception as e:
        res="Some error occurred --> "+str(e)
    return res

def filter_by_category(category):
    if(category=="Beef"):
        return("Sorry, this bot has banned beef. We're not hypocrites like the BJP.")
    url=f"http://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    response=requests.get(url)
    A=json.loads(response.text)
    if(A["meals"]=="null"):
        return("Error, please check the categories again using /recipe_category_list")
    #recipe_list="Here are some "+category+" dishes"+"\n"
    recipe_list=[]
    for i in range(len(A["meals"])):
        #recipe_list+=A["meals"][i]["strMeal"]+"\n"
        recipe_list.append(A["meals"][i]["strMeal"])
    return (recipe_list)
def meal_search(meal):
    url=f"https://www.themealdb.com/api/json/v1/1/search.php?s={meal}"
    try:
        json_data=json.loads(requests.get(url).text)
        meal_name=json_data["meals"][0]["strMeal"]
        meal_category=json_data["meals"][0]["strCategory"]
        meal_instructions=json_data["meals"][0]["strInstructions"]
        meal_youtube=json_data["meals"][0]["strYoutube"]
        meal_ingredients=""
        for i in range(1,21):
            index="strIngredient"+str(i)
            index2="strMeasure"+str(i)
            if(json_data["meals"][0][index]==""):
                break
            meal_ingredients+=json_data["meals"][0][index]+" "+json_data["meals"][0][index2]+"\n"
        meal_link=json_data["meals"][0]["strSource"]
        res =f"Meal Name: {meal_name}\n"
        f"Category: {meal_category}\n\n"
        f"Ingredients:\n{meal_ingredients}\n"
        f"Instructions:\n{meal_instructions}\n\n"
        f"Youtube Link: {meal_youtube}\n"
        f"Meal Link: {meal_link}"
    except Exception as e:
        res="Some error occurred --> "+str(e)
    return res

def get_recipe_by_category(cat):
    L=filter_by_category(cat)[1:]
    if("" in L):
        L.remove("")
    random_recipe=random.choice(L)
    return meal_search(random_recipe)
def love_quote():
    url = "https://love-quote.p.rapidapi.com/lovequote"
    headers = {"x-rapidapi-key": "05ed2b2960msh67feedeb38db313p1158c7jsn2e8756e74a0e",
	"x-rapidapi-host": "love-quote.p.rapidapi.com"}
    response = requests.get(url, headers=headers)
    return(response.json())
'''
#Movie recommendation API(was hosted in my local machine)
def movie_recommend(genre,count):
    url=f"http://localhost:5162/Movie/genre/{genre}?count={count}"
    response=requests.get(url)
    return response
    
#horoscope feature to be added afterwards 
def horoscope(sunsign):
    headers={ 'Content-Type': 'application/json', 'x-api-key': 'xxo7AwhDS81gjQOfngRKS2b02jOznVTk4jP4SG8L' }
    response=requests.get()
'''
def random_number_fact():
    url="http://numbersapi.com/random/"
    response=requests.get(url)
    return response.text
def number_fact(num):
    url=f'http://numbersapi.com/{num}'
    try:
        response=requests.get(url)
        res=response.text()
    except Exception as e:
        res="Some error occurred --> "+str(e)
    return res
def lyrics(artist,title):
    url=f"https://api.lyrics.ovh/v1/{artist}/{title}"
    response=requests.get(url)
    data=response.json()
    if(response.status_code!=200 or "error" in response.json()):
        return ("Sorry, there was some error in fetching lyrics.")
    else:
        return("Here are the lyrics for song - {title} by {artist} - \n "+data["lyrics"])
def help_msg():
    embed = discord.Embed(title="List of commands -",color=discord.Color.green())
    embed.add_field(name="/help", value="This is what is does", inline=False)
    embed.add_field(
        name="/hello", value="says hello to Sh or T", inline=False)
    embed.add_field(name="/our_list",
                    value="sends the link of our shared playlist", inline=False)
    embed.add_field(
        name="/purpose", value="Describes who created this bot and what was the purpose of its creation", inline=False)
    embed.add_field(name="/compliment_shris <num>",
                    value="Gives a specified number of personalized compliments to Sh.", inline=False)
    embed.add_field(name="/compliment_tan <num>",
                    value="Gives a specified number of personalized compliments to T.", inline=False)
    embed.add_field(
        name="/say <to> <msg>", value="Make the bot send a message to a specified user.", inline=False)
    embed.add_field(
        name="/youtube", value="Sends an embedded message about the creator's YT channel.", inline=False)
    embed.add_field(
        name="/weather <city>", value="Sends  info about weather of a city(input).", inline=False)
    embed.add_field(
        name="/recipe_random", value="Sends a link of random recipe.", inline=False)
    embed.add_field(
        name="/recipe_category_list", value="Shows the listed categories of recipes.", inline=True)
    embed.add_field(
        name="/recipes_by_category<category>", value="Shows the listed recipes by a specified category.", inline=False)
    embed.add_field(
        name="/recipe_by_search<recipe>", value="Shows the specified recipe.", inline=True)
    embed.add_field(
        name="/random_recipe_by_category<category>", value="Shows a recipe by a specified category.", inline=False)
    embed.add_field(
        name="/pickup_line<user>", value="Mentions a user followed by a random pickup line.", inline=False)
    embed.add_field(
        name="/random_number_fact", value="Gives a fact about a random number.", inline=False)
    embed.add_field(
        name="/number_fact <num>", value="Gives a fact about the specified number(input).", inline=False)
    embed.add_field(
        name="/horoscope <sun_sign>", value="Gives you today's horoscope on the basis of sun sign entered.", inline=False)
    embed.add_field(name="/roast", value="Gives you a personalised roast.",inline=False)
    embed.set_footer(text="Have fun using this bot, love you sweethearts.")
    return embed
def dogapi():
    url="https://dog.ceo/api/breeds/image/random"
    try:
        response=requests.get(url)
        data=response.json()
        image_url=data["message"]
        embed=discord.Embed(title="Here is a random dog picture")
        embed.set_image(url=image_url)
    except Exception as e:
        embed=discord.Embed(title="Sorry, there was some error in fetching lyrics. \n"+str(e))
    return embed
def checkusr(user:discord.Member):
    if(user.status==discord.Status.online):
        return "The user ",user.mention," is online."
    elif (user.status == discord.Status.offline):
        return "The user "+user.mention+" is offline"
    else:
        return "The user"+user.mention+"is idle/dnd"
def flip():
    a=["heads","tails"]
    res=random.choice(a)
    embed=discord.Embed(title="It is "+res)
    if(res=="tails"):
        imageurl="https://upload.wikimedia.org/wikipedia/commons/1/16/Indian_1_Rupee_Coin_Reverse_or_Tails.jpg"
    else:
        imageurl="https://qph.cf2.quoracdn.net/main-qimg-9c81a54813716fccd8e3608ab2f51dcf-lq"
    embed.set_image(url=imageurl)
    return(embed)
def musicrecbygen(genre,limit):
    HEADERS = {"User-Agent": "YourDiscordBot/1.0 (your@email.com)"}
    #all:      /genre/all?limit=<LIMIT>&offset=<OFFSET>
    url = "https://musicbrainz.org/ws/2/"
    params = {"query": f'tag:"{genre}" AND status:official',"fmt": "json","limit": limit}
    try:
        response = requests.get(
            f"{url}recording/",
            params=params,
            headers=HEADERS
        )
        response.raise_for_status()
        recordings = response.json().get('recordings', [])
        return random.choice(recordings) if recordings else None
    except requests.RequestException as e:
        print(f"MusicBrainz API error: {e}")
        return None

def get_random_recommendation_by_artist(artist: str, limit: int = 5) -> dict:
    """Get random music recommendations similar to artist"""
    MUSICBRAINZ_API_URL = "https://musicbrainz.org/ws/2/"
    HEADERS = {"User-Agent": "YourDiscordBot/1.0 (your@email.com)"}
    params = {
        "query": f'artist:"{artist}" AND status:official',
        "fmt": "json",
        "limit": limit
    }
    
    try:
        response = requests.get(
            f"{MUSICBRAINZ_API_URL}recording/",
            params=params,
            headers=HEADERS
        )
        response.raise_for_status()
        recordings = response.json().get('recordings', [])
        return random.choice(recordings) if recordings else None
    except requests.RequestException as e:
        print(f"MusicBrainz API error: {e}")
        return None
def format_rec(recommendations:dict)->str:
    if not recommendations:
        return("No recommendations found")
    artist = recommendations.get('artist-credit', [{}])[0].get('artist', {}).get('name', 'Unknown Artist')
    title=recommendations.get('title','Unknown Track')
    year=recommendations.get('first-release-date','Unknown Year')[:4]
    return f"🎵 Recommended Track: {artist} - {title} ({year})"
def dic(word:str):
    link=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    try:
        response=requests.get(link).json()
        if(type(response)==type({}) and response['title']=='No Definitions Found'):
            return("Sorry, the word "+ word +" was not found!")
        word=word.lower()
        res="Word - "+word+"\n"
        meanings=response[0]['meanings']
        for a in range(len(meanings)):
            res+=str(a+1)+") Part of speech- "+meanings[a]['partOfSpeech']+"\n"
            for b in range(len(meanings[a]["definitions"])):
                res+="Definition"+"#"+str(b+1)+" - "+meanings[a]['definitions'][b]['definition']+" \n"
    except Exception as e:
        res=str(e)
    return res
def syn(word):
    link=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    try:
        response=requests.get(link).json()
        if(type(response)==type({}) and response['title']=='No Definitions Found'):
            return("Sorry, the word "+ word +" was not found!")
        word=word.lower()
        res="Word - "+word+"\n"
        meanings=response[0]['meanings']
        for a in range(len(meanings)):
            res+=str(a+1)+") "+"Part of Speech - "+meanings[a]["partOfSpeech"]+"\n"
            if(len(meanings[a]['synonyms'])!=0):
                res+="Synonyms - "
                for i in range(len(meanings[a]['synonyms'])):
                    res+=meanings[a]['synonyms'][i]
                    if(i!=len(meanings[a]['synonyms'])-1):
                        res+=", "
                    res+="\n"
                    res+="\n"
    except Exception as e:
        res=str(e)
    return res
def askai(message:str):
    try:
        client = OpenAI(api_key=config.OpenAIKey)
        response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": message}]
        )
        gpt = response.choices[0].message.content
    except Exception as e:
        gpt="Some error occured -->"+str(e)
    return gpt

    
