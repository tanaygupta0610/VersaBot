import os
from dotenv import load_dotenv
load_dotenv('.env')
#This file contains the necessary configurations, keys/tokens for running this application.
OpenAIKey=os.getenv("OPENAI_KEY")#Enter your openai token for chat gpt operations
token = os.getenv("DISCORD_VERSABOT_TOKEN")
#Enter user id of sid, T and SH below
userid={"Sid":1,"Sh":2,"T":3}
serverid = int(os.getenv("DISCORD_SERVER_TANAY")) #Enter your server id here
weatherkey=0
#weatherkey = os.getenv("WEATHER_KEY")
