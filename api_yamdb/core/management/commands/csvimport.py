import csv

from django.core.management.base import BaseCommand
from reviews.models import Categories, Comment, Genres, Review, Title
from users.models import CustomUser

CSV_CATEGORIESS = 'static/data/category.csv'
CSV_GENRES = 'static/data/genre.csv'
CSV_GENRE_TITLE = 'static/data/genre_title.csv'
CSV_TITLES = 'static/data/titles.csv'
CSV_USERS = 'static/data/users.csv'
CSV_REVIEWS = 'static/data/review.csv'
CSV_COMMENTS = 'static/data/comments.csv'


class Command(BaseCommand):
    help = 'Import CSV'

    def handle(self, *args, **kwargs):
        import_categories()
        import_genres()
        import_titles()
        import_genre_title()
        import_users()
        import_reviews()
        import_comments()


def import_categories():
    print("Начинаем импорт Категорий.")
    with open(CSV_CATEGORIESS, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            obj = Categories(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
            obj.save()
        print("Импорт Категорий успешно завершен!")
    print("=======")


def import_genres():
    print("Начинаем импорт Жанров.")
    with open(CSV_GENRES, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            obj = Genres(
                id=row[0],
                name=row[1],
                slug=row[2]
            )
            obj.save()
        print("Импорт Жанров успешно завершен!")
    print("=======")


def import_genre_title():
    print("Начинаем импорт Промежуточной таблицы Titles_Genre.")
    with open(CSV_GENRE_TITLE, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            if not Title.genre.through.objects.filter(
                title_id=row[1], genres_id=row[2]
            ).exists():
                obj = Title.genre.through(
                    id=row[0],
                    title_id=row[1],
                    genres_id=row[2]
                )
                obj.save()
        print("Импорт Промежуточной таблицы Titles_Genre успешно завершен!")
    print("=======")


def import_titles():
    print("Начинаем импорт Произвдений.")
    with open(CSV_TITLES, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            obj = Title(
                id=row[0],
                name=row[1],
                year=row[2],
                category=Categories.objects.get(pk=row[3])
            )
            obj.save()
        print("Импорт Произведений успешно завершен!")
    print("=======")


def import_users():
    print("Начинаем импорт Пользователей.")
    with open(CSV_USERS, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            obj = CustomUser(
                id=row[0],
                username=row[1],
                email=row[2],
                role=row[3],
                bio=row[4],
                first_name=row[5],
                last_name=row[6]
            )
            obj.save()
        print("Импорт Пользователей успешно завершен!")
    print("=======")


def import_comments():
    print("Начинаем импорт Пользователей.")
    with open(CSV_COMMENTS, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            obj = Comment(
                id=row[0],
                review=Review.objects.get(pk=row[1]),
                text=row[2],
                author=CustomUser.objects.get(pk=row[3]),
                pub_date=row[4]
            )
            obj.save()
        print("Импорт Пользователей успешно завершен!")
    print("=======")


def import_reviews():
    print("Начинаем импорт Отзывов.")
    with open(CSV_REVIEWS, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        next(csvreader)
        for row in csvreader:
            obj = Review(
                id=row[0],
                title=Title.objects.get(pk=row[1]),
                text=row[2],
                author=CustomUser.objects.get(pk=row[3]),
                score=row[4],
                pub_date=row[5]
            )
            obj.save()
        print("Импорт Отзывов успешно завершен!")
    print("=======")
