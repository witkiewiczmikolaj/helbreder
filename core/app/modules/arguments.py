args = []
def arguments(data):
    for i in data:
        if data[i] != "":
            args.append(data[i])
    return args