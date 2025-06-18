import random,datetime
OpenAIToken=0#Enter your openai token for chat gpt operations
token = 'Enter your token here'
#Enter user id of sid, T and SH below
userid={"Sid":1,"Sh":2,"T":3}
serverid = 0 #Enter your server id here
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