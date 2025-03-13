import re
from io import StringIO 
import sys

def print_recipe(recipe):
    for key in recipe:
        print(f"{key}: {recipe[key]}")


#print_recipe ({'wheat flour': 250, 'milk': 50, 'egg': 4, 'butter': 50, 'salt': 1})


def read_recipe (recipe_file_name):
    with open(recipe_file_name , 'r') as infile:
        
        ret = dict()
        lines = infile.read()
        lines = lines.split('\n')
        for line in lines:
            if (line == ''):
                continue
            line = line.split(',')
            
            line[0] = line[0].strip(' \t')
            line[1] = line[1].strip(' \t')
            try:

                ret[line[0]] += int(line[1])
            except:
                ret[line[0]] = int(line[1])
        return ret


#print (read_recipe("testinput"))

def write_recipe(recipe, recipe_file_name):
    
    with open(recipe_file_name , 'w') as outfile:
        for key in recipe:
            outfile.write(f"{key},{recipe[key]}\n")

read_fridge = read_recipe

def is_cookable(recipe_file_name, fridge_file_name):
    fridge_dic = read_fridge(fridge_file_name)
    recipe_dic = read_recipe(recipe_file_name)
    ok = True

    for key in recipe_dic:
        try:
            if (fridge_dic[key] < recipe_dic[key]):
                ok = False
        except:
            ok = False
    return ok

def add_recipes (recipes):
    ret = dict()
    for rec in recipes:
        for key in rec:
            try:
                ret[key] += rec[key]
            except:
                ret[key] = rec[key]

    return ret

def add_to_dict(dic , key , val):
    try:
        dic[key] += val
    except:
        dic[key] = val

def create_shopping_list(recipe_file_names, fridge_file_name):
    recipes = add_recipes( [read_recipe(recipe_file) for recipe_file in recipe_file_names] )

    ret = dict()
    fridge = read_fridge(fridge_file_name)

    for key in recipes:
        try:
            if recipes[key] > fridge[key]:
                add_to_dict(ret , key , recipes[key] - fridge[key])
        except:
            add_to_dict(ret , key , recipes[key])

    return ret
                
def total_price (shopping_list , market_file_name):
    prices = read_recipe(market_file_name)
    ret = sum([prices[key] * shopping_list[key] for key in shopping_list])
    return ret


def find_cheapest(shopping_list, market_file_names):
    ret = min([(total_price (shopping_list , file) , file) for file in market_file_names])
    
    return tuple(reversed(ret))

def update_fridge (fridge_file_name, recipe_file_names, market_file_names, new_fridge_file_name):
    shop_list = create_shopping_list(recipe_file_names, fridge_file_name)
    use_market = find_cheapest(shop_list , market_file_names)
    new_fridge = add_recipes([read_recipe(fridge_file_name) , shop_list])
    write_recipe(new_fridge , new_fridge_file_name)
    
    print("Shopping list:")
    print_recipe(shop_list)
    print(f"Market: {use_market[0]}")
    print(f"Total cost: {use_market[1]}")

def distributed_shopping_list (shopping_list, market_file_names):
    markets = [(read_recipe(file) , file) for file in market_file_names]

    ret = dict()
    for market in market_file_names:
        ret[market] = {}

    for item in shopping_list:
        best = (1e9 , "market00")
        for market in markets:
            try:
                if market[0][item] < best[0]:
                    best = (market[0][item] , market[1])
            except:
                pass
        try:
            ret[best[1]][item] = shopping_list[item]
        except:
            ret[best[1]] = {item : shopping_list[item]}

    return ret

# todays_menu = ['crepes.txt', 'flan.txt', 'madeleines.txt']

# what_we_need = create_shopping_list(todays_menu, 'fridge1.txt')

# supermarkets = ['market1.txt','market2.txt','market3.txt']

# print( distributed_shopping_list(what_we_need, supermarkets))