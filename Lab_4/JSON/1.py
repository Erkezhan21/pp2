import json
import pathlib

with open(r'\Users\Пользователь\PycharmProjects\pp2\Lab_4\JSON\sample-data.json') as txt:
    txt = txt.read()
    y = json.loads(txt)

l=""
maxx=-9999

print("Interface Status")
print("=======================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")

for x in y['imdata']:
    l += x["l1PhysIf"]["attributes"]["dn"]
    if len(l) > maxx:
        maxx = len(l)
    l = ""
for x in y['imdata']:
    l += x["l1PhysIf"]["attributes"]["dn"]
    l += (maxx-len(l))*' ' + 9 * ' '
    l += x["l1PhysIf"]["attributes"]["descr"]
    l += ' '*22
    l += x["l1PhysIf"]["attributes"]["speed"]+'  '
    l += x["l1PhysIf"]["attributes"]["mtu"]
    print(l)
    l = ""