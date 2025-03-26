import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Cargar los tweets desde el archivo CSV
df = pd.read_csv("tweets.csv")

# Unir todos los tweets en un solo texto
texto = " ".join(df["Tweet"])

# Crear la nube de palabras
nube_palabras = WordCloud(width=800, height=400, background_color="white").generate(texto)

# Mostrar la imagen generada
plt.figure(figsize=(10, 5))
plt.imshow(nube_palabras, interpolation="bilinear")
plt.axis("off")
plt.title("Nube de Palabras de Tweets sobre Inteligencia Artificial")
plt.show()
