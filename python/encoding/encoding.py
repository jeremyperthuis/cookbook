d = dict({"a" : b"test","b" : "strnormal","c" : b"huehude"})
print(d)
for key, value in d.items():
    try:
        d[key] = value.decode("UTF-8")
    except (UnicodeDecodeError, AttributeError):
        pass


print(d)
