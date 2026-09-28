import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    """Возвращает среднюю оценку по каталогу, 
    округленную до одного знака.
    """
    return round(sum(movie['rating'] for movie in movies) / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    """Возвращает кортеж (самый старый фильм в годах, 
    самый новый фильм в годах, среднее).
    """
    ages = [current_year - movie["year"] for movie in movies]
    return (max(ages), min(ages), math.ceil(sum(ages)/len(ages)))

def duration_in_hours(minutes):
    """Переводит минуты в формат "2ч 35м", 
    используя целочисленное деление и остаток от деления."""
    return f'{minutes//60}ч {minutes%60}м'

def rating_tier(rating):
    """Возвращает метку "шедевр" (9+), "хорошо" (7–8.9), "средне" (5–6.9)
    или "слабо" (0–4.9).
    """
    if rating >= 9:
        return 'шедевр'
    elif rating >= 7:
        return 'хорошо'
    else:
        return 'средне' if rating >= 5 else 'слабо'

def decade_label(year):
    """Возвращает метку "новые" (после 2020), "недавние" (2015–2020) 
    или "старые" (раньше 2015).
    """
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

#Фильмы, которые не являются комедиями
for movie in movies:
    if 'comedy' in movie['genres']:
        continue
    print(movie['title'])

idx = 0
while idx != len(movies)-1:
    if movies[idx]['rating'] > 9.0:
        print(movies[idx]['title'])
        break
    idx += 1
else:
    print('Шедевров не найдено')

def count_long_movies(movies, threshold=120):
    """Возвращает количество фильмов, длительность которых превышает threshold минут."""
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count

def normalize_title(title):
    """Приводит строку к формату Title Case (каждое слово с заглавной буквы)."""
    words = title.split()
    return ' '.join([word[0].upper() + word[1:].lower() for word in words])

print(normalize_title("the last bakery"))  # Вывод: "The Last Bakery"