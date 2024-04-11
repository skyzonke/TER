import requests
import datetime
from exceptions import BadRequest, Unauthorization


# données météo : Humidité, température, vent de apiweather
def meteo_data (url, start_date, end_date):

    # Initialiser un tableau vide pour stocker les données
    output = {}

    # Boucle par jour pour récupérer les données
    while start_date <= end_date:

        try :
                
            # Requête API pour les données quotidiennes
            response = requests.get(url)
            response.raise_for_status()

            data = response.json() # données json recupérer

            # verification si données pas érroné ou inexistant
            if not data or "list" not in data:
                print("Données météo reçu non valide")
                return None

            # récupération de donées sous forme de dictionnaire
            for day_data in data:

                dt = day_data["dt"]
                main = day_data["main"]
                description = day_data["weather"][0]["description"]

                wind = ["wind"] # vent
                temp_c =  273-main["temp"] if (main["temp"] > 100) else main["temp"] # température en dégré celsius
                humidity = main["humidity"] # humidité
                feel_likes = main["feel_likes"] # resentis
                date_str = datetime.datetime.fromtimestamp(dt).strftime("%Y-%m-%d")
                date_time = datetime.datetime.fromtimestamp(dt).strftime("%H:%M")

                output.append({
                    "vent" : date_str,
                    "temp_c" : temp_c,
                    "humidité" : humidity,
                    "resentis" : feel_likes,
                    "date" : date_str,
                    "description" : description
                })
                
        except BadRequest:
            print(BadRequest.BadRequest.badRequest())
        except Unauthorization:
            print(Unauthorization.Unauthorization.unauthorization())

        # Incrémenter la date de départ d'un jour
        start_date = (datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    # données renvoyer
    return output


# données sur la qualité de l'air
def quality_air() :
    pass