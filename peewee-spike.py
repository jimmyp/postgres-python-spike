from peewee import *
from datetime import date
from playhouse.migrate import *


db = SqliteDatabase('test.db')
psql_db = PostgresqlDatabase(
    'peewee-spike', host='db', user='postgres', password='postgres')
migrator = PostgresqlMigrator(psql_db)


class Person(Model):
    name = CharField()
    birthday = DateField()
    favourite_color = CharField()

    class Meta:
        database = psql_db


db.connect()

# does not throw if table already exists, only runs if table does not exist
db.create_tables([Person])

# migrate(
#     migrator.add_column('person', 'favourite_color', CharField(null=True))) # throws if table already exists

Person.create(name='Bob', birthday=date(
    1960, 1, 15), favourite_color='blue')

bob = Person.select().where(Person.name == 'Bob').get()

print(bob.name, bob.birthday)

bob.name = 'Robert'

bob.save()

bob2 = Person.select().where(Person.name == 'Robert').get()

print(bob2.name, bob2.birthday)

db.close()
