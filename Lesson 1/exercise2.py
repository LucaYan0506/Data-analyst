import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import requests

#clear console terminator   
import os
clear = lambda: os.system('cls')
clear()

#download data from github
if not os.path.exists('data/database.db'):
    r = requests.get('https://github.com/LucaYan0506/Data-analyst/raw/master/Lesson%201/data/sakila.db')
    file = 'data/database.db'
    with open(file, 'wb') as f:
        f.write(r.content)
        print ("DB downloaded")

conn = sqlite3.connect('data/database.db')

df = pd.read_sql('''
    SELECT
        rental.rental_id, rental.rental_date, rental.return_date,
        customer.last_name AS customer_lastname,
        store.store_id,
        city.city AS rental_store_city,
        film.title AS film_title, film.rental_duration AS film_rental_duration,
        film.rental_rate AS film_rental_rate, film.replacement_cost AS film_replacement_cost,
        film.rating AS film_rating
    FROM rental
    INNER JOIN customer ON rental.customer_id == customer.customer_id
    INNER JOIN inventory ON rental.inventory_id == inventory.inventory_id
    INNER JOIN store ON inventory.store_id == store.store_id
    INNER JOIN address ON store.address_id == address.address_id
    INNER JOIN city ON address.city_id == city.city_id
    INNER JOIN film ON inventory.film_id == film.film_id
    ;
''', conn, index_col='rental_id', parse_dates=['rental_date', 'return_date'])