import json

SLOT_URL = './speech_assets/customSlotTypes/LIST_OF_{}'


def make_slot_types():
    with open('data.json') as f:
        data = json.load(f)
    for k in data:
        print SLOT_URL.format(k.upper())
        with open(SLOT_URL.format(k.upper()), 'w+') as fw:
            fw.write('\n'.join(map(lambda x: x.lower(), data[k])))

if __name__ == '__main__':
    make_slot_types()