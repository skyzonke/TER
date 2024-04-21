import requests
import datetime
import menu
import api

########################################

 # Clé API gratuite d'APIWeather
api_keys = "3e86dd8cd10c7445621c8421eb186c93"

# lieu : (Orléans, France)
location = "Orléans, France"

########################################


if __name__ == '__main__' :

    menu.menu()
    choice = input(f"Faites un choix de données : ")
    
    match choice :
        case 1 :
            start_date = (datetime.datetime.now() - datetime.timedelta(days=730)).strftime("%Y-%m-%d")
            end_date = datetime.datetime.now().strftime("%Y-%m-%d")
            url = f"https://api.weatherstack.com/historical?access_key={api_keys}&query={location}&historical_date_start={start_date}"
            data = api.meteo_data(url, start_date, end_date)
            
        case 2 :
            pass
        