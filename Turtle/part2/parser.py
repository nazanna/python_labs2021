with open('font.txt', 'r') as old:
    with open('font.json', 'w') as new:
        lines = old.read().split('\n')
        font = []
        for el in lines:
            font.append(list(map(int, el.split(' '))))
        json = {"font size": 50}

        for i, el in enumerate(font):
            json[str(i)] = el

        json_string = "{\n"

        for key, value in json.items():
            json_string += f"\t\"{key}\" : {value},\n"
        json_string = json_string[:-2] + "\n}"
        new.write(json_string)
# print(json)
