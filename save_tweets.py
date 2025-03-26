import tweepy
import pandas as pd
import time

# Configuración del cliente de Twitter (API v2)
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAEuv0AEAAAAAcYYrPaeaEn14g1RpuQPVka%2Fsr5k%3DnZQIzW4zdJ8YlNz8lOZoVwN8VHksWgaQnYPLepDI1pOOh2GSlv"
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Lista para almacenar tweets
datos = []

# Definir el tema de búsqueda
tema = "inteligencia artificial -is:retweet lang:es"

# Manejo de excepciones para evitar fallos por límite de solicitudes
try:
    # Buscar tweets recientes (máximo 20)
    tweets = client.search_recent_tweets(query=tema, max_results=20, tweet_fields=["author_id"])
    
    # Guardar tweets en la lista
    if tweets.data:
        for tweet in tweets.data:
            datos.append([tweet.id, tweet.text])
    
    # Convertir la lista en un DataFrame
    df = pd.DataFrame(datos, columns=["ID", "Tweet"])
    
    # Guardar los tweets en un archivo CSV
    df.to_csv("tweets.csv", index=False, encoding="utf-8")
    print("Tweets guardados en tweets.csv")
except tweepy.errors.TooManyRequests:
    print("Has alcanzado el límite de solicitudes. Intenta nuevamente más tarde.")
