import csv


def read_file(authors, addresses, ads):
    with open('ads.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            authors.append(row["author"])
            addresses.append(row["address"])
            ads.append({"Id": row["Id"], "name": row["name"], "author": row["author"],
                        "price": row["price"], "description": row["description"],
                        "address": row["address"], "is_published": row["is_published"]})
        return authors, addresses, ads


def write_file_fk(name_file, data):
    with open('fk_' + name_file + '.csv', mode='w', encoding='utf-8') as file:
        names = ("Id", f"{name_file}")
        file_writer = csv.DictWriter(file, lineterminator='\r', fieldnames=names)
        file_writer.writeheader()
        for i in range(len(data)):
            file_writer.writerow({"Id": i + 1, f"{name_file}": data[i]})


def write_file_ads_new(authors, addresses, ads):
    with open('ads_new.csv', mode='w', encoding='utf-8') as file:
        names = ['Id', 'name', 'id_author', 'price', 'description', 'id_address', 'is_published']
        file_writer = csv.DictWriter(file, lineterminator='\r', fieldnames=names)
        file_writer.writeheader()
        for row in ads:
            file_writer.writerow(
                {"Id": row["Id"], "name": row["name"], "id_author": authors.index(row["author"]) + 1,
                 "price": row["price"],
                 "description": row["description"], "id_address": addresses.index(row["address"]) + 1,
                 "is_published": row["is_published"]})


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
