from sqlite3 import connect
from os.path import isfile


def conn():
    if not isfile('persons.db'):
        db = connect('persons.db')
        db.execute('CREATE TABLE persons (name TEXT PRIMARY KEY, age INT, profession TEXT)')
        db.commit()
    else:
        db = connect('persons.db')

    return db


class PersonDescriptor(object):
    db = conn()

    def __set__(self, instance, value):
        if value[0] is None:
            self.db.execute('UPDATE persons SET age = ?, profession = ? WHERE name = ?', value)
            self.db.commit()
        else:
            self.db.execute('UPDATE persons SET age = ?, profession = ? WHERE name = ?', value)
            self.db.commit()
            print('Данные обновлены')


class Person(object):
    db = conn()
    x = PersonDescriptor()

    def __init__(self, name):
        self.name = name
        self.cursor = self.db.execute('SELECT name, age, profession FROM persons')
        self.persons = {name: {'age': age, 'profession': profession} for name, age, profession in self.cursor}
        print(self.persons)
        if name not in self.persons:
            self.db.execute("INSERT INTO persons values (?, ?, ?)", (name, None, None))
            self.db.commit()


_name = input('Введите имя: ')
_age = int(input('Введите возраст: '))
_profession = input('Введите имя: ')

print('Имеющиеся данные из таблицы: ')
person = Person(_name)
person.x = (_age, _profession, _name)
