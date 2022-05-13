import pickle
from WebScrapperForItems import Item 
import math

with open("All items of factorio", "rb") as allItemsOfFactorio:
    itemsOfFactorio = pickle.load(allItemsOfFactorio)

iron_ore = Item("iron ore", {}, 1, 2)
copper_ore = Item("copper ore", {}, 1, 2)
stone = Item("stone", {}, 1, 2)
coal = Item("coal", {}, 1, 2)
water = Item("water", {}, 1200, 1)
oil = Item("crude oil", {}, 10, 1)
raw_fish = Item("raw fish", {}, 1, 0)   

