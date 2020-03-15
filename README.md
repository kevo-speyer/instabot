# InfluBot
Idea del proyecto: replicar esta idea en Python:

https://medium.com/@chrisbuetti/how-i-eat-for-free-in-nyc-using-python-automation-artificial-intelligence-and-instagram-a5ed8a1e2a10

en el directorio instabot_api/ esta la API instabot (https://github.com/instagrambot/instabot) para conectarse a instagram y ejecutar lo que queramos.

Para epezar sugiero armar carpetas 'Igal' 'Santi' 'Kevon' para boludear y a medida que tengamos modulos listos, vamos armando el flujo de trabajo del bot.


 
TO DO:

0)  Preparacion (Unico Depende del Tema )
    a) Revisar nombre de la cuenta
    b) Hashtags relevantes
    c) Escribir captions estandar de subida
    d) Escribir hashtags generales

1) Decarga Fotos (Igal)
    a) Busqueda x hashtagag
    b) Filtrar post basura (muchos tags, link a ota pagina)
    c) Analisis mejores fotos 
    d) Descarga + metada (definir path relativo)

2) Subida Fotos (Igal)
    a) select random de 0c) y 0d)
    b) seleccionar foto de las descargadas. Filtrar fotos de usuarios que ya subimos
    c) Si existe la location en foto original, buscarla
    d) PARA MAS ADELANTE Select random time to uploadSubir todo
    e) Subir foto y guardar data (con timestamp)

2b) Gather data (Igal)
    a) Definir tiempo de medicion (1 dia aprox)
    b) Levantar perfiles de los likes y comments, usuarios ganados, usuarios que no le dimos follow 

3) Follow (Santi)
    a) get users from hashtag
    b) get users from great post from 1c)
    c) Concatenar listas a y b    
    d) Filtrar de c) y followers if not black listed ( 4 algo) )
    e) Follow y guardado de data  (con timestamp)
    
4) Unfollow  (Santi)
    a) Levantar la lista de followers
    b) De 3d, etiquetar "follow back" boolean
    c) Criterio de unfollow ( "follow back"==false, mantener ratio followers/followees alto > 2. Eliminar a los que nunca interactuaron y tengo hace mas tiempo)
    d) Unfollow y guardado de data  
