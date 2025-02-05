import pandas as pd
import random
from datetime import datetime, timedelta

def fecha_aleatoria(dias_atras=30):
    hoy = datetime.now()
    inicio = hoy - timedelta(days=dias_atras)
    random_date = inicio + timedelta(seconds=random.randint(0, int((hoy - inicio).total_seconds())))
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

# ================================
# 1. Tabla de Tweets
# ================================
total_users = 15

num_tweets = 10
tweet_categories = ["Política", "Economía", "Deportes", "Cultura", "Tecnología", "Salud", "Mundo"]
tweet_creators = [f"User_{i+1}" for i in range(total_users)]

tweets = []
tweet_id_counter = 1000

for i in range(num_tweets):
    tweet = {
        "tweet_id": tweet_id_counter,
        "creator": random.choice(tweet_creators),
        "category": random.choice(tweet_categories),
        "hashtags": ", ".join(random.sample(["#news", "#trending", "#update", "#breaking", "#info", "#tech", "#world"], random.choice([0, 1, 2]))),
        "tweet_date": fecha_aleatoria(60),
    }
    tweets.append(tweet)
    tweet_id_counter += 1

df_tweets = pd.DataFrame(tweets)
print("Tabla de Tweets:")
print(df_tweets.head())
print("\n")



# ================================
# 2. Tabla de Usuarios
# ================================
countries = ["USA", "España", "México", "Argentina", "Colombia", "Chile", "Perú"]
bios = [
    "Apasionado por la tecnología.",
    "Amante de la música y el cine.",
    "Periodista en busca de la verdad.",
    "Emprendedor y soñador.",
    "Experto en deportes y fitness.",
    "Estudiante de economía.",
    "Fotógrafo aficionado."
]

users = []
for i in range(total_users):
    user = {
        "user_id": f"User_{i+1}",
        "username": f"User_{i+1}",
        "account_creation_date": fecha_aleatoria(365*5),
        "age": random.randint(18, 60),
        "country": random.choice(countries),
        "bio": random.choice(bios),
        "followers_count": random.randint(50, 10000)
    }
    users.append(user)

df_users = pd.DataFrame(users)
print("Tabla de Usuarios:")
print(df_users.head())
print("\n")


# ================================
# 3. Tabla de Interacciones
# ================================
num_interacciones = 50 

interaction_types = ["comment", "like", "repost", "mention"]
interacciones = []
interaction_id_counter = 2000

for i in range(num_interacciones):
    tipo = random.choice(interaction_types)
    tweet_ref = random.choice(df_tweets["tweet_id"].tolist())
    user_from = random.choice(df_users["user_id"].tolist())
    
    if tipo in ["mention"]:
        user_to = random.choice(df_users["user_id"].tolist())
    elif tipo in ["comment"] and random.choice([0,1]) == 1: 
        user_to = random.choice(df_users["user_id"].tolist())
    else:
        user_to = ""

    interaccion = {
        "interaction_id": interaction_id_counter,
        "tweet_id": tweet_ref,
        "user_from": user_from,
        "user_to": user_to,
        "interaction_type": tipo,
        "interaction_date": fecha_aleatoria(30),
    }
    interacciones.append(interaccion)
    interaction_id_counter += 1

df_interacciones = pd.DataFrame(interacciones)
print("Tabla de Interacciones:")
print(df_interacciones.head())
print("\n")

df_tweets.to_csv("data/tweets.csv", index=False)
df_users.to_csv("data/users.csv", index=False)
df_interacciones.to_csv("data/interactions.csv", index=False)