
# from datetime import datetime, timedelta

# ajd = datetime.now()

# un_jour= timedelta(days = 1)
# hier = ajd - un_jour
# print("day : " + str(ajd - un_jour))


# Departement = "marne"
# Pays = "France"
# if Pays == "France":
#     if Departement in ("marne", \ 
#                       "ardenne", "aube"):
#         taxe= 0.06
#     elif Departement == "haute marne":
#         taxe = 0.15
# else : 
#         taxe=0.5
# print(taxe)



# moyenne_classe = float(input("note moyenne ? "))
# note_minimale = float(input("note minimale ?"))

# if moyenne_classe >= 0.85 and note_minimale >= 0.70 : 
#     major_promo = "True"
# else:
#     major_promo = "false"
#     print(str(major_promo))




# # Dictionnaire 
# personne = {'premier' : 'yasser'}
# personne['produit'] = "Elden Ring"
# personne['prix'] = '69.99'
# personne['fournisseur'] = 'FS'

# print(personne)




# from array import array 
# score = array("d")
# score.ap class array(
# print(s)



# #listes

# nom = ["yasser", "diego", "nicolas"]
# score = []
# score.append(97)
# score.append(98)
# score.append(100)
# print(score)



# nom = ['yasser', 'diego']

# nom.insert(0, 'Bastian')
# print(nom)
# nom.sort()
# print(nom)



# # 
# nom = ['yasser', 'bastian', 'leo', 'Ronaldo']
# presents = nom[1:3]
# print(presents)
# L=[nom[0], nom[3]]
# print(L)



# # Dictionnaire 
# for nom in range(100): 
#     print(indice)



# # Dictionnaire 
# for nom in ['bastian', 'schweinsteiger']
#     print(nom)



# #loop avec conditions 

# nom = ['Bastian', 'Schweinsteiger']
# indice = 0

# while indice < len(nom): 
#     print(nom[indice])
#     indice = indice + 1 



# # loop avec condition 2 

nom = ['Alice', 'bob', 'charlie', 'david']
indice = 1

while indice < len(nom): 
    print(nom[indice])
    indice = indice + 1 



# #loop avec conditions 3 

# capacite_maximale = 10 
# capacite_actuelle = 3 

# while capacite_actuelle < capacite_maximale : 
#     print(capacite_actuelle)
#     capacite_actuelle=capacite_actuelle + 1



# loop avec condition 4 

# races_de_chien = ['golden retriever', 'chihuahua', 'terrier', 'carlin']
# for chien in races_de_chien:
#     print(chien)

# for x in range(5): 
#     print(x)

# for x in range(10):
#     print(f'{x} bouteilles de champagne !' )



##### DEBUT SCRAPPING ###### EXO PL TEAMS 

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.skysports.com/premier-league-table"

# r  = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")
# league_table = soup.find("table", class_='standing-table__table callfn')

# teams_data = []

# #Elimination des informations qui ne nous interessent pas 
# for team in league_table.find_all('tbody'):
#     rows = team.find_all('tr')
#     for row in rows :
#         pl_team = row.find('td', class_ = 'standing-table__cell standing-table__cell--name').text.strip()
#         #print(pl_team)
#         pl_point = row.find_all("td", class_= 'standing-table__cell')[9].text
#         print (pl_team, pl_point)
#         team_data



#SCRAP BOOK 
# import requests
# from bs4 import BeautifulSoup

# url = "https://books.toscrape.com/"

# r = requests.get(url)
# soup = BeautifulSoup(r.text, "html.parser")


# article = soup.find_all(div_class = "product_pod")
# print(article)



# EXO GITHUB #
# import requests
# from bs4 import BeautifulSoup

# url = "https://realpython.github.io/fake-jobs/"

# r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')

# jobs = soup.find_all("div", class_ = 'column is half')

# for poste in jobs:
#     titre = poste.find('h2', class_ = 'title is-5').text.strip()
#     société = poste.find('h3', class_ = 'subtitle is-6 company').text
#     ville = poste.find('p', class_ = 'location').text
#     date = poste.find('time', class_ = 'is-small has-text-grey').text

#     print(titre)
#     print(société)
#     print(ville)
#     print(date)
#      



# exo github pas finis #


# import requests
# from bs4 import BeautifulSoup

# url = "https://quotes.toscrape.com/"

#  r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')

# quotes = soup.find_all("div", class_ = "quote")

# for quote in quotes:
#     texte = quote.find('span', class_ = "text")
#     author : quote

#     print(author)
#     print(texte)
#     print("-" * 50)



# BOOKSCRAP #


# import requests
# from bs4 import BeautifulSoup

# for x in range(0,51):
#     url= f'https://books.toscrape.com/catalogue/page-2{x}.html'

# r = requests.get(url)

#     soup = BeautifulSoup(r.text, 'html.parser')
#     article = soup.find_all("article", class_="product_pod")

#     for livre in article :
#         titre = livre.find_all('a')[1]['title']
#         Prix = livre.find('p', class_ = "price_color").text[2:]
#         stock = livre.find('p', class_ = "instock availability").text.strip()
        
#         print(titre)
#         print(Prix)
#         print(stock)
#         print('-' * 50)



# github exo jobs #

# import requests
# from bs4 import BeautifulSoup

# url = "https://realpython.github.io/fake-jobs/"

# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')

# job = soup.find_all("div", class_ = "card-content")

# for taf in job : 
#     title = taf.find("h2", class_ = "title is-5").text
#      title = taf.find("h3", class_ = "subtitle is-6 company").text
#      title = taf.find("P", class_ = "location" ).text.strip()
#      title = taf.find("time", class_ = "is-small has-text-grey").text.strip()



# EXO POKEMON GITHUB #

# import requests
# from bs4 import BeautifulSoup

# url = "https://pokemondb.net/pokedex/national"
# r = requests.get(url)

# soup = BeautifulSoup(r.text, 'html.parser')

# product = soup.find_all('div', class_ = 'infocard-list infocard-list-pkmn-lg')


# for pokemon in product:
#     nom = pokemon.find('a', class_ = "ent-name").text
#     element = pokemon.find("a",  class_ = "intype")
#     if len(element) == 2:
#         type1, type2 = type[0].text.strip(), type[1].text.strip




