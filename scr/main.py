# it is bot`s login 
# @IwillsolvetheGIA_bot

from BotScript import Bot

link_for_materials={
    "education_materials":{

        "9":{
            "english":"",
            "mathematics":"",
            "russian":"",
            "informatika":"",
            "physics":"",
            "geography":""
        },

        "11":{
            "english":"",
            "mathematics":"",
            "russian":"",
            "informatika":"",
            "physics":"",
            "geography":""
        }
    }
}

print(link_for_materials["education_materials"]["9"])
TOKEN = ""
bot = Bot(TOKEN)
bot.run()
