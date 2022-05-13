import pickle
import requests
from bs4 import BeautifulSoup

url = "https://davemcw.com/factorio/tech-tree/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

class Item:

    timeToProduce = 0 #Time to produce the item in seconds
    numberOfProducts = 0 #Number of items produced
    name = "invalid" #name of the item
    recipe = {} #dictionary where the key is the name of the item and the value is the # of items needed

    
    def __init__(self, name, recipe, numberOfProducts, timeToProduce):
        
        self.name = name
        self.recipe = recipe
        self.numberOfProducts = numberOfProducts
        self.timeToProduce = timeToProduce
    
    def printThisObject(self):

        text = "Name: {0}\nnumberOfProducts: {1}\nTime to produce it: {2}s".format(self.name, self.numberOfProducts, self.timeToProduce) + "\nRecipe:\n"

        for nameOfRecipe, numberOfItemsOfRecipe in self.recipe.items():
            text += "{0} and it takes {1}\n".format(nameOfRecipe, numberOfItemsOfRecipe)
        
        text += "------------------------------------------------------\n"
        return text



itemsOfFactorio = {} #dictionary where the key is the name of the item and the value is the item object

with open("All items of factorio", "wb") as allItemsOfFactorio:

    #Creates an item object
    for item in doc.find_all(class_ = "item"):
        recipe = {}
        name = item["data-products"].split(",")[0].replace("-", " ")#gets the name of the item
        numberOfProducts = item["data-products"].split(",")[1]#gets the number of products it produces


        dataIngredients = item["data-ingredients"].split(",")
        ingredientsAndTime = dataIngredients[0:len(dataIngredients) - 2] #get the ingredients and timewhich are all but the last two elements
        ingredients = ingredientsAndTime[::2] #gets the ingredients
        numberOfItemsOfIngredients = ingredientsAndTime[1::2] #gets the number of items

        timeToProduce = dataIngredients[len(dataIngredients) - 1] 

        #traverse trough ingredients and the numbers of items that it needs and put it in the dictionary
        for nameOfRecipe, numberOfItems in zip(ingredients, numberOfItemsOfIngredients):

            recipe[nameOfRecipe.replace("-", " ")] = numberOfItems

        itemCreated = Item(name, recipe, numberOfProducts, timeToProduce)
        itemsOfFactorio[itemCreated.name] = itemCreated


    pickle.dump(itemsOfFactorio, allItemsOfFactorio)




