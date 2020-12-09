
def Country_Data():
    with open('.country.txt', 'r') as f:
        data = f.read()
        return data
