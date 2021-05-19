import os, json

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    os.chdir(os.path.dirname(__file__) + "/../")

theLibrary = []
for root, dirs, files in os.walk(".", topdown = False):
    for name in files:
        if name[-7:] == ".ntjson":
            theModel = { "name": name[:-7], "folder": root[2:], "path": os.path.join(root, name)[2:].replace(" ", "%20") }
            theLibrary.append(theModel)

folders = []

for item in theLibrary:
    if item['folder'] not in folders:
        folders.append(item['folder'])

folders = sorted(folders, key = str.lower)

NTANGO_PLAYER = "https://netlogoweb.org/nettango-player?playMode=true&netTangoModel="
NTANGO_EDITOR = "https://netlogoweb.org/nettango-builder?netTangoModel="
GITHUB_REPO   = "https://raw.githubusercontent.com/NetLogo/nt-models/main/"

f = open(os.getcwd() + "/LIBRARY.md", "w")
libraryDict = []
f.write("# Preliminary NetTango Models Library Directory\n\n")
for folder in folders:
    f.write("## " + folder + "\n")
    for model in sorted(theLibrary, key = lambda i: i['name']):
        if folder == model['folder']:
            f.write("""*  [{name}]({playLink}) [(editable)]({editLink})\n\n""".format(name=model['name'],
                                                                  playLink=(NTANGO_PLAYER + GITHUB_REPO + model['path']),
                                                                  editLink=(NTANGO_EDITOR + GITHUB_REPO + model['path'])
                                                                 ))
            libraryDict.append({ 'name': model['name'], 'path': model['path'], 'url': NTANGO_PLAYER + GITHUB_REPO + model['path'] })
f.close()

with open(os.getcwd() + "/library.json", "w") as outfile:
    libraryDict = { 'success': True, 'models': libraryDict }
    json.dump(libraryDict, outfile)
