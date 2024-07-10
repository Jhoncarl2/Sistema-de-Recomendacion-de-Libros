Sistema Experto De una Recomendación de Libros Mediante una Red Neuronal

Lenguaje: Python

Librerias Utilizadas:
Flask
tensorflow
pandas
numpy
scikit-learn

Resumen: Es un Modelo previamente entrenado mediante las tecnicas del Machine-Learning que te recomienda libros en base a la misma categoria o genero que sea del libro que previamente seleccionado




Pasos Para Ejecutar el Sistema

# Instalar dependencias
pip install -r requirements.txt

# Crear Libros
python crear_libros.py

# Preparar los datos
python data_preparation.py

# Entrenar el modelo
python train_model.py

# Ejecutar la aplicación web
python app.py

# POR SI EL USUARIO DESEA SABER COMO FUERON LOS RESULTADOS DEL TRENAMIENTO
Puede revisar el training_history.csv

# O si el usuario lo desea ver de forma grafica
python analizar_resultados.py