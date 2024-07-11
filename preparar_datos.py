import pandas as pd

# Leer el archivo CSV de libros
books = pd.read_csv('libros.csv')

# Codificar el género
genre_mapping = {genre: idx for idx, genre in enumerate(books['genero'].unique())}
books['genre_encoded'] = books['genero'].map(genre_mapping)

# Guardar el DataFrame procesado en un archivo CSV
books.to_csv('libros_procesados.csv', index=False)

print("Archivo libros_procesados.csv creado con éxito.")
