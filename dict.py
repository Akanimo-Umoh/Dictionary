dictionary = {"dict 1" : {"name" : "akanimo", "surname" : "umoh"},
"dict 2" : {"country" : "nigeria", "state" : "akwa ibom"},
"dict 3" : {"city" : "uyo", "tribe" : "ibibio"}}
for key, value in dictionary.items():
    """Accessing the items"""
    print (f"\n{key}")
    for key in value.keys():
        print (key)
    for value in value.values():
        print (value)