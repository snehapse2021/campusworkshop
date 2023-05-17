"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7j4bhp8u7g2ed7g8g-a.oregon-postgres.render.com",
        database="todo_8np4",
        user="root",
        password="V0w8ggRsyYOK8g1FewlXcOsTmvl3mguq")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
