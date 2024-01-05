def magic_string(list=[]):
    list += [1]
    return "BestSchool" + (", BestSchool" * (len(list) - 1))
