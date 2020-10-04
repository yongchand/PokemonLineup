#Code Created By Yongchan Hong
#Use hungarian (munkres) algorithm for matching
import requests
import json
from munkres import Munkres, print_matrix


link ="https://pokeapi.co/api/v2/pokemon/"
myList= input("Put Your List of Pokemon. Split By Space: ").split()
opList = input("Put Opponent List of Pokemon. Split By Space. Same Number with Your List of Pokemon Required: ").split()
# myList = ['Rayquaza', 'Koffing', 'Charmander', 'Raichu', 'Pidgeotto', 'Ditto']
# opList = ['Pikachu', 'Ditto', 'Squirtle', 'Butterfree', 'Pidgey', 'Ditto']

pokeArr = []
myArr = []

for i in myList:
    response = requests.get(link+i.lower())
    returnV = response.json()['types'][0]
    poketype = returnV["type"]["name"]
    #TODO: Consider two types pokemon



    nlink = "https://pokeapi.co/api/v2/type/"
    response = requests.get(nlink+poketype)
    returnA = response.json()["damage_relations"]["double_damage_from"]
    returnB = response.json()["damage_relations"]["double_damage_to"]
    returnC = response.json()["damage_relations"]["half_damage_from"]
    returnD = response.json()["damage_relations"]["half_damage_to"]
    nDict = {}
    for i in returnA:
        nDict[i["name"]] = -1

    for i in returnB:
        nDict[i["name"]] = -5

    for i in returnC:
        nDict[i["name"]] = -2

    for i in returnD:
        nDict[i["name"]] = -4
    
    pokeArr.append(nDict)
    
for i in opList:
    response = requests.get(link+i.lower())
    returnV = response.json()['types'][0]
    poketype = returnV["type"]["name"]
    myArr.append(poketype)

pokematrix = [[0 for x in range(len(opList))] for y in range(len(myList))] 
for i_num, i in enumerate(myArr):
    saveDict = {}
    for j_num, j in enumerate(pokeArr):
        if i in j.keys():
            pokematrix[j_num][i_num]= j[i]
        else:
            pokematrix[j_num][i_num] = -3

m = Munkres()
indexes = m.compute(pokematrix)
for row, column in indexes:
    value = pokematrix[row][column]
    print(myList[column]+" should match up with "+opList[row])



    


