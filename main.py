import csv


def read_file(authors: list, addresses: list, ads: list) -> tuple[list, list, list]:
    """
    Читает файл и разбивает его на 3 списка
    :param authors: список авторов
    :param addresses: список адресов
    :param ads: список со словарем всех данных из файла ads.csv
    :return: возвращает списки с данными
    """
    with open('ads.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            authors.append(row["author"])
            addresses.append(row["address"])
            ads.append({"Id": row["Id"], "name": row["name"], "author": row["author"],
                        "price": row["price"], "description": row["description"],
                        "address": row["address"], "is_published": row["is_published"]})
        return authors, addresses, ads


def write_file_fk(name: str, data: list) -> None:
    """
    Записывает обработанные данные для foreign key в файл
    """
    with open(name + '.csv', mode='w', encoding='utf-8') as file:
        names = ("Id", f"{name}")
        file_writer = csv.DictWriter(file, lineterminator='\r', fieldnames=names)
        file_writer.writeheader()
        for id_, val in enumerate(data):
            file_writer.writerow({"Id": id_ + 1, f"{name}": val})


def write_file_ads_new(authors: list, addresses: list, ads: list) -> None:
    """
    Заменяет поля авторов и адресов на соответствующие им индексы. Записывает обработанные данные
    для foreign key в файл
    """
    with open('ads_new.csv', mode='w', encoding='utf-8') as file:
        names = ['Id', 'name', 'id_author', 'price', 'description', 'id_address', 'is_published']
        file_writer = csv.DictWriter(file, lineterminator='\r', fieldnames=names)
        file_writer.writeheader()
        for row in ads:
            file_writer.writerow(dict(Id=row["Id"], name=row["name"],
                                      id_author=authors.index(row["author"]) + 1,
                                      price=row["price"],
                                      description=row["description"],
                                      id_address=addresses.index(row["address"]) + 1,
                                      is_published=row["is_published"]))


def main():
    authors = []
    addresses = []
    ads = []

    read_file(authors, addresses, ads)
    authors = list(set(authors))
    addresses = list(set(addresses))
    write_file_fk('authors', authors)
    write_file_fk('addresses', addresses)
    write_file_ads_new(authors, addresses, ads)


if __name__ == '__main__':
    main()
