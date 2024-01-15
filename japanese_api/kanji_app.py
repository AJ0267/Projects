import requests
from keys import API_KEY, API_HOST
import os
from art import logo

headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": API_HOST
}

def singleKanji(single):
	url = f"https://kanjialive-api.p.rapidapi.com/api/public/kanji/{single}"
	response = requests.get(url, headers=headers)
	print(f"grade : {response.json()['grade']}")
	print(f"meaning : {response.json()['meaning']}")
	print(f"on reading : {response.json()['onyomi_ja_search'][-1]}")
	print(f"kun reading : {response.json()['kunyomi_ja_search'][-1]}")

# single = input("Type single kanji for details:\n")
# singleKanji(single)

def basicInfo(basic):
	url = f"https://kanjialive-api.p.rapidapi.com/api/public/search/{basic}"
	response = requests.get(url, headers=headers)
	print(response.json())

# basic = input("A kanji character, Onyomi reading (katakana), Kunyomi reading (hiragana) or a kanji's simplified English meaning.\n: ")
# basicInfo(basic)
	
def engMeaning(eng):
	url = "https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/"
	querystring = {"kem": eng}
	response = requests.get(url, headers=headers, params=querystring)
	print(response.json())

# eng = input("REQUIRED Simplified English kanji meaning.\n: ")
# engMeaning(eng)

def kunSearch(kun):
	url = "https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/"
	querystring = {"kun": kun}
	response = requests.get(url, headers=headers, params=querystring)
	print(response.json())

# kun = input("REQUIRED Hiragana or romaji,\n: ")
# kunSearch(kun)
	
def onSearch(on):
	url = "https://kanjialive-api.p.rapidapi.com/api/public/search/advanced/"
	querystring = {"on":on}
	response = requests.get(url, headers=headers, params=querystring)
	print(response.json())

# on = input("REQUIRED Hiragana or romaji,\n: ")
# onSearch(on)
	
def studyList(deck):
	url1 = "https://kanjialive-api.p.rapidapi.com/api/public/search/advanced"


	if int(deck) > 11:
		print(f"Invalid deck number! there is no deck no.{deck}.")
		exit()


	querystring = {"list":f"mac:c{11 + int(deck)}"}
	response1 = requests.get(url1, headers=headers, params=querystring)
	data = response1.json()
	srno = 1
	collection = []
	for x in data:
		print(f"{srno}) {x['kanji']['character']}")
		collection.append(x['kanji']['character'])
		srno += 1

	# print(collection)
	specific = input("Type serial number of kanji for more info or type 'exit' to close this.\n: ").lower()
	if specific == 'exit':
		print("thanks for using kanji app!")
	elif int(specific) > len(collection):
		print("invalid kanji number!!!!")
	else:	
		url2 = f"https://kanjialive-api.p.rapidapi.com/api/public/kanji/{collection[int(specific) - 1]}"
		response = requests.get(url2, headers=headers)
		print(f"selected kanji : {collection[int(specific) - 1]}")
		print(f"grade : {response.json()['grade']}")
		print(f"meaning : {response.json()['meaning']}")
		print(f"on reading : {response.json()['onyomi_ja_search'][-1]}")
		print(f"kun reading : {response.json()['kunyomi_ja_search'][-1]}")
    
# deck = input("deck number ranging from 1-11:\n ") #12 - 22
# studyList(deck)
	

kanji_app_on = False


while not kanji_app_on:
    print(logo)
    choice_list = ['kanji search', 'basic search', 'simplified english meaning search', 'search kanji by kun reading', 'search kanji by on reading', 'kanji decks']
    choice = int(input(f"""
    pick a choice:\n
        1){choice_list[0]}.\n
        2){choice_list[1]}.\n
        3){choice_list[2]}.\n
        4){choice_list[3]}.\n
        5){choice_list[4]}.\n
        6){choice_list[5]}.\n
        7)close app.
        
    your choice : """))

    if choice == 0 or choice > 7:
        print("invalid choice!")
    else:
        if choice == 1:
            single = input("Type single kanji for details:\n")
            singleKanji(single)
        elif choice == 2:
            basic = input("A kanji character, Onyomi reading (katakana), Kunyomi reading (hiragana) or a kanji's simplified English meaning.\n: ")
            basicInfo(basic)
        elif choice == 3:
            eng = input("REQUIRED Simplified English kanji meaning.\n: ")
            engMeaning(eng)    
        elif choice == 4:
            kun = input("REQUIRED Hiragana or romaji,\n: ")
            kunSearch(kun)
        elif choice == 5:
            on = input("REQUIRED Hiragana or romaji,\n: ")
            onSearch(on)
        elif choice == 6:
            deck = input("deck number ranging from 1-11:\n ") #12 - 22
            studyList(deck)
        elif choice == 7:
            os.system('cls')
            # kanji_app_on = True
            print("Thanks for using kanji app!!!!")
            exit()
            
    
    should_continue = input('do you want to continue? type "yes" or "no".\n').lower()
    if should_continue == "yes":
        os.system('cls')
    elif should_continue == "no":
        os.system('cls')
        kanji_app_on = True
        print("Thanks for using kanji app!!!!")


