import requests

text = requests.get(url="https://api.github.com/repos/pandas-dev/pandas/issues")
convert = text.json()

for i in convert:
    print('\n')
    print('ID (from the original list) ----- ', i["id"])
    print('Avatar URL (from the user) -----', i['user']["avatar_url"])
    for j in i['labels']:
        print('URL (from the label -----)', j['url'])
        text2 = requests.get(url=j['url'])
        convert2 = text2.json()
        try:
            print('ID from the label URL -----', convert2['id'])
        except KeyError:
            print('ID from the label URL ----- that ID does not exist')
        except TypeError:
            pass
        try:
            print('Color from the label URL -----', convert2['color'])
        except KeyError:
            print('Color from the label URL ----- that color does not exist')
        except TypeError:
            pass

