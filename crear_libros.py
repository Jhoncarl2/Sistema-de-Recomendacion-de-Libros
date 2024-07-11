import pandas as pd

# Crear un DataFrame con los datos de libros
data = {
    'id_libro': list(range(1, 51)),
    'titulo': [
        'Matar a un ruiseñor', '1984', 'Harry Potter y la piedra filosofal', 'El gran Gatsby', 'El guardián entre el centeno',
        'El hobbit', 'Fahrenheit 451', 'Jane Eyre', 'Orgullo y prejuicio', 'El Señor de los Anillos',
        'Crónica de una muerte anunciada', 'Don Quijote de la Mancha', 'La sombra del viento', 'Los juegos del hambre', 'El nombre de la rosa',
        'El alquimista', 'El código Da Vinci', 'La catedral del mar', 'El retrato de Dorian Gray', 'La carretera',
        'Un mundo feliz', 'El psicoanalista', 'La chica del tren', 'El club de la lucha', 'El jinete de bronce',
        'El Terror', 'El día que se perdió la cordura', 'La ladrona de libros', 'El último deseo', 'El príncipe',
        'La niña alemana', 'Las chicas de la 305', 'El hombre en el castillo', 'El país de las sombras largas', 'Los pilares de la Tierra',
        'El lobo de Wall Street', 'El guerrero del amanecer', 'Los siete hábitos de la gente altamente efectiva', 'La guía del autoestopista galáctico',
        'El arte de la guerra', 'La esposa del viajero en el tiempo', 'El jardín secreto', 'El niño con el pijama de rayas',
        'El último samurái', 'La casa de los espíritus', 'El hobbit', 'La casa en el confín de la tierra', 'El hombre que susurraba a los caballos',
        'El médico', 'El corazón de las tinieblas'
    ],
    'autor': [
        'Harper Lee', 'George Orwell', 'J.K. Rowling', 'F. Scott Fitzgerald', 'J.D. Salinger',
        'J.R.R. Tolkien', 'Ray Bradbury', 'Charlotte Brontë', 'Jane Austen', 'J.R.R. Tolkien',
        'Gabriel García Márquez', 'Miguel de Cervantes', 'Carlos Ruiz Zafón', 'Suzanne Collins', 'Umberto Eco',
        'Paulo Coelho', 'Dan Brown', 'Ildefonso Falcones', 'Oscar Wilde', 'Cormac McCarthy',
        'Aldous Huxley', 'John Katzenbach', 'Paula Hawkins', 'Chuck Palahniuk', 'Paullina Simons',
        'Dan Simmons', 'Javier Castillo', 'Markus Zusak', 'Andrzej Sapkowski', 'Nicolás Maquiavelo',
        'Armando Lucas Correa', 'Ana González Duque', 'Philip K. Dick', 'Hans Ruesch', 'Ken Follett',
        'Jordan Belfort', 'David Gemmell', 'Stephen R. Covey', 'Douglas Adams', 'Sun Tzu',
        'Audrey Niffenegger', 'Frances Hodgson Burnett', 'John Boyne', 'Helen DeWitt', 'Isabel Allende',
        'J.R.R. Tolkien', 'William Hope Hodgson', 'Nicholas Evans', 'Noah Gordon', 'Joseph Conrad'
    ],
    'genero': [
        'Crecimiento Personal', 'Ciencia Ficción', 'Aventura', 'Crecimiento Personal', 'Crecimiento Personal',
        'Aventura', 'Ciencia Ficción', 'Romántico', 'Romántico', 'Aventura',
        'Crecimiento Personal', 'Crecimiento Personal', 'Suspenso', 'Ciencia Ficción', 'Suspenso',
        'Aventura', 'Suspenso', 'Suspenso', 'Crecimiento Personal', 'Ciencia Ficción',
        'Ciencia Ficción', 'Terror', 'Suspenso', 'Acción', 'Romántico',
        'Terror', 'Suspenso', 'Crecimiento Personal', 'Aventura', 'Crecimiento Personal',
        'Crecimiento Personal', 'Suspenso', 'Ciencia Ficción', 'Crecimiento Personal', 'Crecimiento Personal',
        'Crecimiento Personal', 'Acción', 'Crecimiento Personal', 'Ciencia Ficción', 'Crecimiento Personal',
        'Romántico', 'Romántico', 'Romántico', 'Aventura', 'Crecimiento Personal', 'Ciencia Ficcion',
        'Terror', 'Romántico', 'Aventura', 'Crecimiento Personal'
    ],
    'calificacion': [
        4.8, 4.7, 4.9, 4.6, 4.4, 4.8, 4.5, 4.7, 4.8, 4.9,
        4.6, 4.9, 4.8, 4.7, 4.7, 4.5, 4.4, 4.8, 4.5, 4.6,
        4.7, 4.4, 4.5, 4.6, 4.8, 4.7, 4.6, 4.9, 4.8, 4.5,
        4.6, 4.7, 4.8, 4.9, 4.5, 4.8, 4.7, 4.9, 4.5, 4.6,
        4.7, 4.4, 4.8, 4.5, 4.9, 4.6, 4.5, 4.6, 4.7, 4.9
    ],
    'image_url': [
        'images/downloaded_image_1.jpg', 'images/downloaded_image_2.jpg', 'images/downloaded_image_3.jpg', 'images/downloaded_image_4.jpg', 'images/downloaded_image_5.jpg',
        'images/downloaded_image_6.jpg', 'images/downloaded_image_7.jpg', 'images/downloaded_image_8.jpg', 'images/downloaded_image_9.jpg', 'images/downloaded_image_10.jpg',
        'images/downloaded_image_11.jpg', 'images/downloaded_image_12.jpg', 'images/downloaded_image_13.jpg', 'images/downloaded_image_14.jpg', 'images/downloaded_image_15.jpg',
        'images/downloaded_image_16.jpg', 'images/downloaded_image_17.jpg', 'images/downloaded_image_18.jpg', 'images/downloaded_image_19.jpg', 'images/downloaded_image_20.jpg',
        'images/downloaded_image_21.jpg', 'images/downloaded_image_22.jpg', 'images/downloaded_image_23.jpg', 'images/downloaded_image_24.jpg', 'images/downloaded_image_25.jpg',
        'images/downloaded_image_26.jpg', 'images/downloaded_image_27.jpg', 'images/downloaded_image_28.jpg', 'images/downloaded_image_29.jpg', 'images/downloaded_image_30.jpg',
        'images/downloaded_image_31.jpg', 'images/downloaded_image_32.jpg', 'images/downloaded_image_33.jpg', 'images/downloaded_image_34.jpg', 'images/downloaded_image_35.jpg',
        'images/downloaded_image_36.jpg', 'images/downloaded_image_37.jpg', 'images/downloaded_image_38.jpg', 'images/downloaded_image_39.jpg', 'images/downloaded_image_40.jpg',
        'images/downloaded_image_41.jpg', 'images/downloaded_image_42.jpg', 'images/downloaded_image_43.jpg', 'images/downloaded_image_44.jpg', 'images/downloaded_image_45.jpg',
        'images/downloaded_image_46.jpg', 'images/downloaded_image_47.jpg', 'images/downloaded_image_48.jpg', 'images/downloaded_image_49.jpg', 'images/downloaded_image_50.jpg'
    ]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('libros.csv', index=False)

print("Archivo libros.csv creado con éxito.")
