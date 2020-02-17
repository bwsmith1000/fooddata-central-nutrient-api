import requests
import json

apiKey = '###' #need USDA API key
foodID = '342594' #example of Asparagus,raw

def nutrient_API(apiKey, foodID):
    #calls get api and json load
    api_resp = json.loads(requests.get('https://api.nal.usda.gov/fdc/v1/' + foodID + '?api_key=' + apiKey).text)
    #only return nutrition information
    api_nutrients = api_resp['foodNutrients']
    #first entry is its description, foodID, and database entry type
    nutrientDict = {"FoodID": [api_resp['description'],foodID, api_resp['dataType']]}

    for items in api_nutrients:
        if 'amount' in items:
            #each entry includes nutrient name, nutrient id, amount, and its respective unit
            nutrientDict.update({(items['nutrient']['name']): [(items['nutrient']['id']),
                (items['amount']),(items['nutrient']['unitName'])]})
    return(nutrientDict)
