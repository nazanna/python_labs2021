import json

with open('font.txt', 'r') as old:
    with open('font.json', 'w') as new:
        lines = old.read().split('\n')
        font = []
        for el in lines:
            font.append(tuple(map(int, el.split(' '))))
        json_content = {"font size": 50}

        for i, el in enumerate(font):
            json_content[str(i)] = el

        
        new.write(json.dumps(json_content, indent=4))
