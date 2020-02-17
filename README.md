# fooddata-central-nutrient-api
Uses USDA's FoodData Central API to get complete nutrition information of a food using a FoodID

## Getting Started
This is a pretty simple python script/function to help you extract nutrition information from the USDA's food database

### Prerequisites
Python IDE
USDA FoodData Central API Key(https://fdc.nal.usda.gov/api-guide.html)
FDC ID (https://fdc.nal.usda.gov/index.html)
  *Type name of food you are interested in and FDC ID is listed in results table

### Libraries
requests (https://pypi.org/project/requests/2.7.0/)
json *included standard python library

## Usage
The 'nutrient_API' function requires two arguments (your API key and FDC ID) and returns a dictionary with all the avaliable nutrients. The first entry includes the FDC ID, description, and entry type. The subsequent entries are each nutrient name (key) with list of the nutrient ID (i.e Protien is 1003), the amount, and the unit of that amount.
