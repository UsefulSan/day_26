import csv



def read_file(authors, addresses, ads):

    with open('ads.csv', encoding='utf-8') as file:
        file_reader = csv.DictReader(file, delimiter=',')
        for row in file_reader:
            authors.append(row["author"])
            addresses.append(row["address"])
        return authors, addresses, ads

def write_file_author(name_file, data):
    with open('fk_' + name_file + '.csv', mode='w', encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=',', lineterminator='\r')
        for i in range(len(data)):
            file_writer.writerow([i+1, data[i]])




def main():
    authors = []
    addresses = []
    ads = []
    read_file(authors, addresses, ads)
    authors = list(set(authors))
    addresses = list(set(addresses))
    write_file_author('authors', authors)
    write_file_author('addresses', addresses)




if __name__ == '__main__':
    main()


