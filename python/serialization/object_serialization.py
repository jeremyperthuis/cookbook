import json

class User():
    def __init__(
        self,
        firstname="",
        lastname="",
        email="",
        phonenumber="",
        listitems = []
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phonenumber = phonenumber
        self.listitems = listitems

    def __dict__(self):
        return {'firstname': self.firstname,
                'lastname' : self.lastname,
                'email' : self.email,
                'phonenumber' : self.phonenumber,
                'listitems' :self.listitems
                }


if __name__ == "__main__":
    a = User("frank", "desherbe", "frank@outlook.com", "0671662533", ['a', 'b', 'c'])
    b = User("richard", "malobo", "richard@outlook.fr", "0987654321", ['a', 'b', 'c'])
    c = dict()
    c[1] = a.__dict__()
    c[2] = b.__dict__()
    print(c)
    # Writing to sample.jsonc
    with open("sample.json", "w+") as outfile:
        outfile.write(json.dumps(c))
        #outfile.write(b.__repr__())
    outfile.close()

    f = open("sample.json", "r")
    data = json.loads(f.read())
    print(data)
    print(type(data))
