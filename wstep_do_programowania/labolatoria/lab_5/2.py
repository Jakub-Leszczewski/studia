# Napisz funkcję, która będzie tworzyć profil użytkownika z obowiązkowym imieniem oraz adresem
# email i dowolnymi dodatkowymi informacjami (min. 3). Funkcja zwraca słownik zawierający
# wszystkie dane profilu. Wykorzystaj funkcję isinstance() oraz strip().

def create_profile(name: str, email: str, **kwargs):
    new_profile = { 'name': name.strip(), 'email': email.strip() }

    for key, value in kwargs.items():
        if isinstance(value, str):
            new_profile[key] = value.strip()
        else:
            new_profile[key] = value

    return new_profile


print(create_profile('Jakub', 'jakub@example.com', phone='123456789', city='Rzeszów'))
print(create_profile('Jakub 2', 'jakub2@example.com', phone='431231232', city='Warszawa', age=24))