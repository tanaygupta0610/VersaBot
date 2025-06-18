import random, discord,datetime
OpenAIToken=0#Enter your openai token for chat gpt operations
token = 'Enter your token here'
#Enter user id of sid, T and SH below
userid={"Sid":1,"Sh":2,"T":3}
serverid = 0 #Enter your server id here
def rotate_bottle(interaction:discord.Interaction):
    players=["Sh", "T"]
    member=interaction.guild.fetch_member(userid["Sid"])
    permissions=interaction.channel.permissions_for(member)
    if(permissions.read_messages):
        players.append("Sid")
    return(random.choice(players))

positive_words = {
    'a': ['Amazing', 'Awesome', 'Affectionate', 'Admirable'],
    'b': ['Brilliant', 'Beautiful', 'Blessed', 'Brave'],
    'c': ['Caring', 'Creative', 'Confident', 'Charming'],
    'd': ['Delightful', 'Dazzling', 'Dedicated', 'Dependable'],
    'e': ['Excellent', 'Energetic', 'Elegant', 'Empathetic'],
    'f': ['Fantastic', 'Fabulous', 'Faithful', 'Friendly'],
    'g': ['Gracious', 'Great', 'Generous', 'Genuine'],
    'h': ['Happy', 'Honest', 'Helpful', 'Humble'],
    'i': ['Incredible', 'Inspirational', 'Innovative', 'Impressive'],
    'j': ['Joyful', 'Jovial', 'Jubilant', 'Judicious'],
    'k': ['Kind', 'Keen', 'Knowledgeable', 'Kingly'],
    'l': ['Loving', 'Lively', 'Legendary', 'Luminous'],
    'm': ['Magnificent', 'Motivated', 'Mindful', 'Marvelous'],
    'n': ['Nice', 'Noble', 'Notable', 'Nurturing'],
    'o': ['Outstanding', 'Optimistic', 'Open-minded', 'Organized'],
    'p': ['Positive', 'Powerful', 'Passionate', 'Peaceful'],
    'q': ['Quick-witted', 'Quintessential', 'Quietly-strong', 'Quality-focused'],
    'r': ['Radiant', 'Respectful', 'Resilient', 'Reliable'],
    's': ['Spectacular', 'Strong', 'Smart', 'Supportive'],
    't': ['Terrific', 'Trustworthy', 'Talented', 'Thoughtful'],
    'u': ['Unique', 'Upbeat', 'Understanding', 'Uplifting'],
    'v': ['Valiant', 'Vibrant', 'Victorious', 'Virtuous'],
    'w': ['Wonderful', 'Wise', 'Witty', 'Warmhearted'],
    'x': ['Xenial', 'Xtraordinary', 'Xceptional'],  # X words are rare!
    'y': ['Youthful', 'Yummy', 'Yielding (in a positive way)', 'Yearning (positive aspirations)'],
    'z': ['Zealous', 'Zestful', 'Zen', 'Zappy']
}
def create_fullform(name):
    res="Here is the breakdown of each letter of your name - \n"
    name=name.lower()
    flag=True
    for i in name:
        if (ord(i) not in range(ord("a"),ord("z")+1) and ord(i) not in range(ord("A"),ord("Z")+1)):
            continue
        else:
            if flag==True:
                res+=i.upper()+": "+random.choice(positive_words[i])+"\n"
                flag=False
            else:
                res+=i+": "+random.choice(positive_words[i]).lower()+"\n"
    return res
def countdown(user,year,month,day):
    target_date = datetime.datetime(year, month,day, 0, 0, 0)
    now = datetime.datetime.now()
    time_left = target_date - now
    if time_left.total_seconds() <= 0:
        return("The time is in the past, no need for a countdown")
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = (time_left.seconds % 3600) // 60
    seconds = time_left.seconds % 60
    embed=discord.Embed(title=user+"'s birthday",color=discord.Color.red())
    embed.add_field(name="Countdown - ", value=f"Time remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")
    return embed