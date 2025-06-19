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
## New feature added:
🤖 AI-Powered Responses (OpenAI Integration)
The Discord bot can now generate smart, context-aware replies using OpenAI’s API! Just use the askai command followed by your prompt, and let the AI handle the rest.

✨ Key Features
askai [prompt] – Get instant AI-generated responses in Discord.

Natural Language Understanding – Supports questions, creative prompts, and general knowledge.

Error Handling – Gracefully manages API failures, rate limits, and invalid requests.

Configurable Settings – Adjust response length, creativity (temperature), and more via bot settings.

⚙️ Setup Instructions
Obtain an OpenAI API Key – Sign up at OpenAI and add your key to the bot’s config.

Enable the Feature – Add the generated key to the OpenAIKey variable in the 2nd line of config.py file.

Customize Responses (Optional) – Tweak parameters like max_tokens for different results.

## 🛠Installation

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
    - OpenWeatherMap API
    - Free Dictionary API
    - MusicBrainz API
    - Dog CEO API
    - Numbers API
    - Zen Quotes API (Motivational quotes)
    - TheMealDB API (Recipes)
    - lyrics.ovh API
  
