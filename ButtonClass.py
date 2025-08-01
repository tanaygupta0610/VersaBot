import discord,random
import config,ApiFun
from personal import compliments,roasts,apology
from gmat import gmat_quant,gmat_verbal,gmat_data_insights
discordbuttonstyle=[discord.ButtonStyle.blurple,discord.ButtonStyle.gray,discord.ButtonStyle.danger,discord.ButtonStyle.green]
class Apology(discord.ui.View):
    @discord.ui.button(label="Apologise to Sh",style=discord.ButtonStyle.red,emoji="👑")
    async def button_callback(self,button,interaction):
        await button.response.send_message("T says to <UserID of the person you are apologizing to> - "+apology.apologise_to_Sh())
    @discord.ui.button(label="Apologise to T",style=discord.ButtonStyle.blurple,emoji="👨🏻")
    async def button_call(self,button,interaction):
        await button.response.send_message("T says - no need cutu, apology accepted.")
class ComplimentSh(discord.ui.View):
    @discord.ui.button(label="Romantic Compliment",style=discord.ButtonStyle.red,emoji="❤️")
    async def button_compliment(self,button,interaction):
        await button.response.send_message("<User ID>, "+random.choice(compliments.Sh_romantic_compliments))
    @discord.ui.button(label="Trait Compliment", style=discord.ButtonStyle.blurple,emoji="💪")
    async def button_compliment2(self,button,interaction):
        await button.response.send_message("<User ID>, "+random.choice(compliments.Sh_trait_compliments))
class ComplimentT(discord.ui.View):
    @discord.ui.button(label="Romantic Compliment",style=discord.ButtonStyle.red,emoji="❤️")
    async def button_romantic_compliment(self,button,interaction):
        await(button.response.send_message("T, "+random.choice(compliments.T_romantic_compliments)))
    @discord.ui.button(label="Trait Compliment", style=discord.ButtonStyle.blurple,emoji="💪")
    async def button_trait_compliment(self,button,interaction):
        await button.response.send_message("T, "+random.choice(compliments.T_trait_compliments))
class Roast(discord.ui.View):
    @discord.ui.button(label="Roast T",style=discord.ButtonStyle.grey)
    async def roastT(self,button,interaction):
        await button.response.send_message(f"A roast for <@{config.userid['T']}> - {random.choice(roasts.T_roasts)}")
    @discord.ui.button(label="Roast Sh",style=discord.ButtonStyle.red)
    async def roastshris(self,button,interaction):
        await button.response.send_message(f"A roast for <@{config.userid['Sh']}> - {random.choice(roasts.Sh_roasts)}")
    @discord.ui.button(label="Roast Sid",style=discord.ButtonStyle.blurple)
    async def roastsid(self,button,interaction):
        await button.response.send_message(f"A roast for <@{config.userid['Sid']}> - {random.choice(roasts.Sid_roasts)}")
class Bore(discord.ui.View):
    @discord.ui.button(label="Bore lagra",style=discord.ButtonStyle.grey,emoji="🎲")
    async def borelagra(self,button,interaction):
        await button.response.send_message(config.bore_fun())
    @discord.ui.button(label="ShrisTan",style=discord.ButtonStyle.success,emoji="👩🏻‍❤️‍👨🏻")
    async def boreshristan(self,button,interaction):
        await button.response.send_message(config.bore_shristan())
class TruthDare(discord.ui.View):
    def __init__(self,players):
        super().__init__()
        self.players=players
    @discord.ui.button(label="Truth",style=discord.ButtonStyle.blurple)
    async def truth(self,button,interaction):
        await button.response.send_message("Here's a question for you - "+config.get_truth())
    @discord.ui.button(label="Dare",style=discord.ButtonStyle.danger)
    async def dare(self,button,interaction):
        await button.response.send_message("Here's a dare for you - "+config.get_dare())
    @discord.ui.button(label="Rotate",style=discord.ButtonStyle.green)
    async def rotate(self,button,interaction):
        target = random.choice(self.players)
        await button.response.edit_message(content=f"🍾 The bottle points at... **{target}!**\n\n**New round!** Choose below:",view=TruthDare(self.players))
class Recipe(discord.ui.View):
    @discord.ui.button(label="Random recipe",style=discord.ButtonStyle.blurple,emoji="🥗")
    async def random(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe())
    @discord.ui.button(label="List of categories",style=discord.ButtonStyle.success,emoji="🍽️")
    async def category(self,button,interaction):
        await button.response.send_message(view=RecipeByCat())
class RecipeByCat(discord.ui.View):
    @discord.ui.button(label="Category -Chicken",style=discord.ButtonStyle.grey,emoji="🍗")
    async def chicken(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Chicken"))
    @discord.ui.button(label="Category - Dessert",style=discord.ButtonStyle.success,emoji="🍨")
    async def dessert(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Dessert"))
    @discord.ui.button(label="Category - Lamb",style=discord.ButtonStyle.blurple,emoji="🍖")
    async def lamb(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Lamb"))
    @discord.ui.button(label="Category - Miscellaneous",style=discord.ButtonStyle.danger,emoji="🍽️")
    async def misc(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Miscellaneous"))
    @discord.ui.button(label="Category - Pasta",style=discord.ButtonStyle.grey,emoji="🍝")
    async def pasta(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Pasta"))
    @discord.ui.button(label="Category - Pork",style=discord.ButtonStyle.red,emoji="🐷")
    async def prok(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Pork"))
    @discord.ui.button(label="Category - Seafood",style=discord.ButtonStyle.green,emoji="🍤")
    async def seafood(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Seafood"))
    @discord.ui.button(label="Category - Side",style=discord.ButtonStyle.blurple,emoji="🍽️")
    async def sidet(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Side"))
    @discord.ui.button(label="Category - Starter",style=discord.ButtonStyle.success,emoji="🍟")
    async def starter(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Starter"))
    @discord.ui.button(label="Category - Vegan",style=discord.ButtonStyle.red,emoji="🥗")
    async def vegan(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Vegan"))
    @discord.ui.button(label="Category - Vegetarian",style=discord.ButtonStyle.blurple,emoji="🥦")
    async def vegetarian(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Vegetarian"))
    @discord.ui.button(label="Category - Breakfast",style=discord.ButtonStyle.success,emoji="🍳")
    async def breakfast(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Breakfast"))
    @discord.ui.button(label="Category - Goat",style=discord.ButtonStyle.grey,emoji="🐐")
    async def goat(self,button,interaction):
        await button.response.send_message(ApiFun.get_recipe_by_category("Goat"))
class RecipesByCat(discord.ui.View):
    @discord.ui.button(label="Category -Chicken",style=discord.ButtonStyle.grey,emoji="🍗")
    async def chicken(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Chicken"))
    @discord.ui.button(label="Category - Dessert",style=discord.ButtonStyle.success,emoji="🍨")
    async def dessert(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Dessert"))
    @discord.ui.button(label="Category - Lamb",style=discord.ButtonStyle.blurple,emoji="🍖")
    async def lamb(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Lamb"))
    @discord.ui.button(label="Category - Miscellaneous",style=discord.ButtonStyle.danger,emoji="🍽️")
    async def misc(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Miscellaneous"))
    @discord.ui.button(label="Category - Pasta",style=discord.ButtonStyle.grey,emoji="🍝")
    async def pasta(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Pasta"))
    @discord.ui.button(label="Category - Pork",style=discord.ButtonStyle.red,emoji="🐷")
    async def prok(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Pork"))
    @discord.ui.button(label="Category - Seafood",style=discord.ButtonStyle.green,emoji="🍤")
    async def seafood(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Seafood"))
    @discord.ui.button(label="Category - Side",style=discord.ButtonStyle.blurple,emoji="🍽️")
    async def sidet(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Side"))
    @discord.ui.button(label="Category - Starter",style=discord.ButtonStyle.success,emoji="🍟")
    async def starter(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Starter"))
    @discord.ui.button(label="Category - Vegan",style=discord.ButtonStyle.red,emoji="🥗")
    async def vegan(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Vegan"))
    @discord.ui.button(label="Category - Vegetarian",style=discord.ButtonStyle.blurple,emoji="🥦")
    async def vegetarian(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Vegetarian"))
    @discord.ui.button(label="Category - Breakfast",style=discord.ButtonStyle.success,emoji="🍳")
    async def breakfast(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Breakfast"))
    @discord.ui.button(label="Category - Goat",style=discord.ButtonStyle.grey,emoji="🐐")
    async def goat(self,button,interaction):
        await button.response.send_message(ApiFun.filter_by_category("Goat"))
class RecipeList(discord.ui.View):
    def __init__(self,recipes):
        super().__init__()
        for recipe in recipes:
            self.add_item(RecipeButton(recipe))
class RecipeButton(discord.ui.Button):
    def __init__(self, *, recipe):
        super().__init__(label=recipe,style=random.choice(discordbuttonstyle),)
        self.recipe=recipe
    async def callback(self, interaction):
        await interaction.response.send_message(ApiFun.meal_search(self.recipe))

'''class AddChannel(discord.ui.View):
    def __init__(self)->None:
        super().__init__(timeout=None)
    @discord.ui.button(label="Create a new ticket",style=discord.ButtonStyle.success)
    
'''   
def rotate_bottle(interaction:discord.Interaction):
    players=["Sh", "T"]
    member=interaction.guild.fetch_member(config.userid["Sid"])
    permissions=interaction.channel.permissions_for(member)
    if permissions.read_messages:
        players.append("Sid")
    return random.choice(players)
def create_fullform(name):
    res="Here is the breakdown of each letter of your name - \n"
    name=name.lower()
    flag=True
    for i in name:
        if ord(i) not in range(ord("a"),ord("z")+1) and ord(i) not in range(ord("A"),ord("Z")+1):
            continue
        else:
            if flag:
                res+=i.upper()+": "+random.choice(compliments.positive_words[i])+"\n"
                flag=False
            else:
                res+=i+": "+random.choice(compliments.positive_words[i]).lower()+"\n"
    return res


class AnswerButtons(discord.ui.View):
    def __init__(self, correct,explanation):
        super().__init__(timeout=120)
        self.correct_answer = correct
        self.explanation = explanation
        self.responded = False

    async def disable_all_buttons(self):
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True

    async def on_timeout(self):
        await self.disable_all_buttons()

    @discord.ui.button(label='A', style=discord.ButtonStyle.blurple)
    async def a_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, 'A')

    @discord.ui.button(label='B', style=discord.ButtonStyle.grey)
    async def b_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, 'B')

    @discord.ui.button(label='C', style=discord.ButtonStyle.primary)
    async def c_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, 'C')

    @discord.ui.button(label='D', style=discord.ButtonStyle.grey)
    async def d_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, 'D')

    @discord.ui.button(label='E', style=discord.ButtonStyle.primary)
    async def e_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.handle_answer(interaction, 'E')

    async def handle_answer(self, interaction: discord.Interaction, selected_answer):
        if self.responded:
            return

        self.responded = True
        await self.disable_all_buttons()

        is_correct = selected_answer == self.correct_answer
        color = discord.Color.green() if is_correct else discord.Color.red()
        result = "Correct!" if is_correct else "Incorrect!"

        embed = discord.Embed(
            title=f"Answer: {self.correct_answer} ({result})",
            description=f"**Explanation:** {self.explanation}",
            color=color
        )

        await interaction.response.edit_message(view=self)
        await interaction.followup.send(embed=embed)

class Gmat(discord.ui.View):
    def get_gmat(self,type):
        random_element = {}
        if type == "Quant":
            random_element = random.choice(gmat_quant.quant_questions)
        elif type == "Verbal":
            random_element = random.choice(gmat_verbal.verbal_questions)
        elif type == "DataInsights":
            random_element = random.choice(gmat_data_insights.data_insights_questions)
        return random_element
    def embed_question(self,element: dict):
        options_embed = ""
        for op in element["options"]:
            options_embed = options_embed + f" {op}\n"
        return element["question"] + "\n" + options_embed
    @discord.ui.button(label="Quantitative Aptitude", style=discord.ButtonStyle.green)
    async def quant(self, button, interaction):
        ele_var=self.get_gmat("Quant")
        embed = discord.Embed(title="Quantitative Aptitude", description=self.embed_question(ele_var))
        await button.response.send_message(embed=embed,view=AnswerButtons(ele_var["answer"],ele_var["explanation"]))

    @discord.ui.button(label="Data Insights", style=discord.ButtonStyle.blurple)
    async def di(self, button, interaction):
        ele_var = self.get_gmat("DataInsights")
        embed = discord.Embed(title="Data Insights", description=self.embed_question(ele_var))
        await button.response.send_message(embed=embed,view=AnswerButtons(ele_var["answer"],ele_var["explanation"]))


    @discord.ui.button(label="Verbal Reasoning", style=discord.ButtonStyle.red)
    async def verbal(self, button, interaction):
        ele_var=self.get_gmat("Verbal")
        embed=discord.Embed(title="Verbal Reasoning", description=self.embed_question(ele_var))
        await button.response.send_message(embed=embed,view=AnswerButtons(ele_var["answer"],ele_var["explanation"]))

