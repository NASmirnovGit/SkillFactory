import json
import os


with open(os.path.join('test', 'json_example_QAP.json'), encoding='utf8') as f:
    templates = json.load(f)


def checkInt(item):
    return isinstance(item, int)


def checkStr(item):
    return isinstance(item, str)


def checkBool(item):
    return isinstance(item, bool)


def checkUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False


def checkStrValue(item, val):
    if isinstance(item, str):
        return item in val
    else:
        return False


def errorLog(item, value, string):
    error.append({item: f'{value},{string}'})


list_of_items = {'timestamp': 'int', 'item_price': 'int', 'referer': 'url', 'location': 'url', 'item_url': 'url',
                 'remoteHost': 'str', 'partyId': 'str', 'sessionId': 'str', 'pageViewId': 'str', 'item_id': 'str',
                 'basket_price': 'str', 'userAgentName': 'str', 'eventType': 'val', 'detectedDuplicate': 'bool',
                 'detectedCorruption': 'bool', 'firstInSession': 'bool'}

error = []
for items in templates:
    for item in items:
        if item in list_of_items:
            if list_of_items[item] == 'int':
                if not checkInt(items[item]):
                    errorLog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'str':
                if not checkStr(items[item]):
                    errorLog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'bool':
                if not checkBool(items[item]):
                    errorLog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'url':
                if not checkUrl(items[item]):
                    errorLog(item, items[item], f'ожидали тип {list_of_items[item]}')
            elif list_of_items[item] == 'val':
                if not checkStrValue(items[item], ['itemBuyEvent', 'itemViewEvent']):
                    errorLog(item, items[item], f'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                errorLog(item, items[item], 'неожиданное значение')
        else:
            errorLog(item, items[item], 'неизвестная переменная')

if error == []:
    print('Pass')
else:
    print('Faill')
    print(error)
