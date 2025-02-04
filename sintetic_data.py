import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

num_usuarios = 10
num_interacciones = 100

usuarios = [f"Usuario_{i+1}" for i in range(num_usuarios)]

comentarios = [
    "Gran noticia!", "No lo creo...", "Esto es interesante", "Información errónea",
    "Muy convincente", "Necesito más detalles", "Alerta de fake news", "Revisa esta fuente",
    "Increíble", "Totalmente de acuerdo", "Me parece dudoso", "¿Alguien más lo vio?"
]

etiquetas = ["Política", "Economía", "Deportes", "Cultura", "Tecnología", "Salud", "Mundo"]

def generar_comentario_y_etiquetas():
    comentario = random.choice(comentarios)
    num_etiquetas = random.choice([1, 2])
    etiquetas_seleccionadas = random.sample(etiquetas, num_etiquetas)
    return comentario, etiquetas_seleccionadas

def fecha_aleatoria():
    hoy = datetime.now()
    inicio = hoy - timedelta(days=30)
    random_date = inicio + timedelta(seconds=random.randint(0, int((hoy - inicio).total_seconds())))
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

datos_interacciones = []

for i in range(num_interacciones):
    emisor, receptor = random.sample(usuarios, 2)
    
    comentario, etiquetas_seleccionadas = generar_comentario_y_etiquetas()
    
    timestamp = fecha_aleatoria()
    
    tipo_interaccion = random.choice(["mención", "respuesta", "retweet", "compartir"])
    
    datos_interacciones.append({
        "id_interaccion": i+1,
        "emisor": emisor,
        "receptor": receptor,
        "comentario": comentario,
        "etiquetas": ", ".join(etiquetas_seleccionadas),
        "tipo_interaccion": tipo_interaccion,
        "timestamp": timestamp
    })

df_interacciones = pd.DataFrame(datos_interacciones)

df_interacciones.to_csv("data/sintetic_data.csv", index=False)
