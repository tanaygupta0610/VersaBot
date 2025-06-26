# VersaBot 
VersaBot is a discord bot created by me in the month of March, 2025.
This bot is your all-in-one multifunctional Discord bot, designed to entertain, inform, and assist! Whether you're looking for music recommendations, curious about the weather, seeking a motivational quote, or just want to play a quick game of Truth or Dare — VersaBot has you covered.

---

## Features:
- AI Responses(New)
  - Get AI generated responses, brainstorm, ask questions or just chat with the AI powered bot using the "/askai" command.
  
- Music Recommendations
  - Get personalized music suggestions based on your favorite artist or genre.

- Dictionary Lookup
  - Instantly find definitions of any word.

- Motivational Quotes
  - Uplift your server members with inspiring quotes.

- Truth or Dare Game
  - A fun and interactive game to play with your friends.

- Speak on Your Behalf
  - Let the bot say something to another user with your chosen tone (we have a list of more than 100 compliments, apologies, and roasts).

- Weather Updates
  - Get current weather details by entering a location.

- Recipe Finder
  - Find delicious recipes based on any dish name you enter.

- Coin Flip
  - Heads or Tails? Let fate decide.

- Random Dog Picture
  - Who doesn't love a surprise doggo?

- Number Facts
  - Learn something new with a random or specific number fact.

--- 
# 🤖 AI-Powered Responses (OpenAI Integration)
The Discord bot can now generate smart, context-aware replies using OpenAI’s API! Just use the askai command followed by your prompt, and let the AI handle the rest.

## ✨ Key Features
- askai [prompt] – Get instant AI-generated responses in Discord.

- Natural Language Understanding – Supports questions, creative prompts, and general knowledge.

- Error Handling – Gracefully manages API failures, rate limits, and invalid requests.

- Configurable Settings – Adjust response length, creativity (temperature), and more via bot settings.

## ⚙️ Setup Instructions
- Obtain an OpenAI API Key – Sign up at OpenAI and add your key to the bot’s config.

- Enable the Feature – Add the generated key to the OpenAIKey variable in the 2nd line of config.py file.

- Customize Responses (Optional) – Tweak parameters like max_tokens for different results.

# 🔍 Advanced Features
## 📝 Smart Logging System
- Structured Logging: Implemented a centralized logging system using Python’s logging module, capturing:
  
  - Command invocations (user ID, guild ID, timestamp). 
  - API errors (with full stack traces via exc_info=True).
  - Bot lifecycle events (startup, shutdown).

- File Rotation: Automated log rotation with RotatingFileHandler (5MB/file, 3 backups) to prevent disk bloat.

  - Contextual Tracking: Enriched logs with user/guild metadata for debugging:

  - Severity Levels: Classified logs as INFO (commands), WARN (rate limits), and CRITICAL (crashes).

## ⚡ Redis Caching
- Performance Boost: Cached frequent API responses (OpenAI, weather, music) with 25x faster response times (500ms → 20ms).

## 🛠️ Setup Instructions
Logging: No config needed—logs save to ./discord.log automatically.

Redis:

```bash
docker run -p 6379:6379 redis  # Local setup
```
Key Use Cases:

- The askai command: Cache OpenAI responses to reduce costs and latency.

- The weather command: Store city forecasts for 1 hour (TTL=3600).

- Rate limiting: Track user command usage with INCR + EXPIRE.

- Efficient Storage: Used Redis’s SETEX for auto-expiring data and memory optimization.

# 🛠Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/VersaBot.git
   cd VersaBot
2. Install dependencies:
   (Python modules used - discord, json, requests, random, bs4, aiohttp)
    ```bash
    pip install -r requirements.txt 
3. Generate your discord bot token from the discord develper portal and add that to the token variable in config.py file (3rd line).
   
4. Run the bot:
    ```bash
    python3 bot.py

## Configuration :
 - Make sure to enable all necessary intents in the Discord Developer Portal for your bot, including:
      Message Content Intent
      Server Members Intent (if needed)

## Contributing
  - Pull requests are welcome! If you have suggestions for improvements or new features, feel free to fork the repo and submit a PR.

## License
  - This project is open-source and available under the MIT License.

## Acknowledgements
  - Thanks to the developers of various APIs used:
    - OpenAI API
    - OpenWeatherMap API
    - Free Dictionary API
    - MusicBrainz API
    - Dog CEO API
    - Numbers API
    - Zen Quotes API (Motivational quotes)
    - TheMealDB API (Recipes)
    - lyrics.ovh API
  
