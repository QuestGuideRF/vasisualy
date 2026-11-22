import json
defaults ={
"voice":"Artemiy",
"speed":30 ,
"pitch":0 ,
"wiki_sentences":4 ,
"music":"music/",
"theme":"Темно-красный",
"from_lang":"ru",
"to_lang":"en",
"weather_api":"",
"weather_city":"Лондон"
}
def get_value (param ):
    with open ("vasisualy.json","r")as f :
        settings =json .load (f )
        value =settings [param ]
    return value