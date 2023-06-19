1# -------------------------------------------------------

#Projektityö viikko 15

#versio 3.1

#(C) Janne Bragge, Sastamala, Suomi

#janne.bragge@edu.sasky.fi

# 6.5.2022

# -------------------------------------------------------

#tehtävässä tarvittavat kirjastot
import os
os.system("cls")

from datetime import date, timedelta
import time
import random
import requests


#funktio hakee tämän päivän päivämäärän
def tama_paiva():
        date_today = str((date.today()))
        pvm = date.today()
        apod(date_today, pvm)

#funktio hakee edellisen päivän päivämäärän
def eilinen():
        date_yesterday = str((date.today() + timedelta(days=-1)))
        pvm = (date.today() + timedelta(days=-1))
        apod(date_yesterday, pvm)

#funktio arpoo satunnaisen päivämäärän
def satunnainen():
        date_random = str((date.today() + timedelta(days=satunnainen_paiva())))
        pvm = (date.today() + timedelta(days=satunnainen_paiva()))
        apod(date_random, pvm)

#funktio määrittelee raja-arvon satunnaisen päivämäärän hakemiseksi
def satunnainen_paiva():
    first_date, last_date = date(1995, 6, 16), date.today()
    dates_bet = first_date - last_date
    total_days = dates_bet.days
    satunnainen_pv = random.randrange(total_days, 0)
    return satunnainen_pv

#funktio hakee verkosta Nasan sivuilta pyydetyn päivämäärän mukaisen kuvan datan
def apod(annettu_paiva, pvm):

    #muodostaa kansion päivämäärän mukaan

    year = str(pvm.year)
    month = str(pvm.month)
    
   
    # tarvittaessa luodaan kansio vuodelle
    if year not in os.listdir():
        os.mkdir(year)
    
    # tarvittaessa luodaan kansio kuukaudelle
    if month not in os.listdir(year):
        os.mkdir(os.path.join(year, month))
        
    
    # luodaan tiedostolle polku tallennusta varten
    file_path = os.path.join(year, month, pvm.strftime("%Y-%m-%d"))
    file_path = file_path + '.jpg'



    #määrittele päivän kuva
    kuva_url = 'https://api.nasa.gov/planetary/apod?'
    avain = 'api_key=Mg5WooOsSpyIWL6B398IODdl8vev2rx6pvOFZYvR'
    paiva ="&date=" + annettu_paiva
    
    #kutsutaan kuvaa
    kuva_avain_pvm = kuva_url + avain + paiva

    response = requests.get(url=kuva_avain_pvm)
    print(response)
    data = response.json()
    url = data['url']
    title = data['title']
    image_response = requests.get(url)

    #muodostaa tiedoston päivän kuvasta päivämäärän mukaiseen kansioon
    with open(file_path, 'wb') as tiedosto:
        tiedosto.write(image_response.content)
        tiedosto.close()
        print("\nKuvan lataaminen onnistui:\n", "tiedostopolku: ", file_path)
        print("\nKuvan nimi: ", title)


def main():
    """
    
    Tekee: hakee Nasan tallentaman päivän kuvan (APOD) Nasan sivuilta
    Argumentit: valinta 1. päivän kuva, 2. eilisen päivän kuva, 3. satunnaisen päivän kuva, 4. lopettaa ohjelman
    Palauttaa: tallentaa kuvan ja avaa kuvan url-polusta

    """

    #valikko jossa pyydetään käyttämää määrittelemään minkä päivämäärän kuva haetaan (tämä päivä, eilinen, satunnainen päivämäärä tai ohjelman lopetus)
    print("\nviikko 15 - projektityö\n")
    def paaohjelma():
        print("")
        while True:
            print("\n1 - Ladata tämän päivän astronomisen kuvan\n2 - Ladata eilisen päivän astronomisen kuvan\n3 - Ladata satunnaisen astronomisen kuvan väliltä: 16.6.1995 - (tämä päivä)\n0 - Lopettaa ohjelma\n")
            valinta = input("Valinta: ")
            if valinta == "1":
                tama_paiva()
            elif valinta == "2":
                eilinen()
            elif valinta == "3":
                satunnainen()
            elif valinta == "0":
                print("Kiitos ohjelman käytöstä")
                break
            elif valinta == "":
                print("valinta virheellinen, valitse uudelleen.")
            else:
                print("Valinta on virheellinen, valitse uudelleen.")
    paaohjelma()

if __name__ == '__main__':
    main()





#eof