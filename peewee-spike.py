from peewee import *
from datetime import date

db = SqliteDatabase('test.db')
psql_db = PostgresqlDatabase(
    'peewee-spike', host='db', user='postgres', password='postgres')


class Person(Model):
    name = CharField()
    birthday = DateField()
    favourite_color = CharField()

    class Meta:
        database = psql_db


db.connect()

db.create_tables([Person])

Person.create(name='Bob', birthday=date(1960, 1, 15), favourite_color='blue')

bob = Person.select().where(Person.name == 'Bob').get()

print(bob.name, bob.birthday)

bob.name = 'Robert'

bob.save()

bob2 = Person.select().where(Person.name == 'Robert').get()

print(bob2.name, bob2.birthday)

db.close()
