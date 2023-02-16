import os, json, re

if os.path.dirname(os.path.abspath(__file__)) == os.getcwd():
    os.chdir(os.path.dirname(__file__) + "/../")

NLOGO_EMPTY_INFO = '(a general understanding of what the model is trying to show or explain)'

def getModelInfo(relativePath):
    with open(relativePath, "r") as f:
        modelJson = json.load(f)

    modelSections = re.split(r"^@#\$#@#\$#@\n", modelJson['code'], flags = re.M)
    infoSection = modelSections[2]
    infoGraphs = infoSection.splitlines()
    i = 0
    while i < len(infoGraphs) and (infoGraphs[i] == '' or infoGraphs[i].strip().startswith('#')):
        i = i + 1
    graphs = []
    while i < len(infoGraphs) and (not infoGraphs[i].strip().startswith('#')):
        if not (infoGraphs[i] in ['', NLOGO_EMPTY_INFO]):
            graphs.append(infoGraphs[i].strip())
        i = i + 1

    info = "" if len(graphs) == 0 else '\n\n'.join(graphs)

    return info

theLibrary = []
for root, dirs, files in os.walk(".", topdown = False):
    for name in files:
        if name[-7:] == ".ntjson":
            relativePath = os.path.join(root, name)[2:]
            escapedPath = relativePath.replace(" ", "%20")

            info = getModelInfo(relativePath)

            theModel = {
                "name": name[:-7]
            ,   "folder": root[2:]
            ,   "path": escapedPath
            ,   "info": info
            }
            theLibrary.append(theModel)

folders = []

for item in theLibrary:
    if item['folder'] not in folders:
        folders.append(item['folder'])

folders = sorted(folders, key = str.lower)

NTANGO_PLAYER = "https://netlogoweb.org/nettango-player?playMode=true&netTangoModel="
NTANGO_EDITOR = "https://netlogoweb.org/nettango-builder?netTangoModel="
GITHUB_REPO   = "https://raw.githubusercontent.com/NetLogo/nettango-models/main/"
TEST_PLAYER   = "https://staging.netlogoweb.org/nettango-player?playMode=true&netTangoModel="
TEST_EDITOR   = "https://staging.netlogoweb.org/nettango-builder?netTangoModel="

def generatePage(file, playerLink, editorLink):
    f = open(os.getcwd() + "/" + file, "w")
    libraryDict = []
    f.write("# Preliminary NetTango Models Library Directory\n\n")

    for folder in folders:
        f.write("## " + folder + "\n\n")

        for model in sorted(theLibrary, key = lambda i: i['name']):
            if folder == model['folder']:
                playLink = (playerLink + GITHUB_REPO + model['path'])
                editLink = (editorLink + GITHUB_REPO + model['path'])
                lineTemplate = """### [{name}]({playLink}) [(editable)]({editLink})\n\n"""
                modelLine = lineTemplate.format(name=model['name'], playLink = playLink, editLink = editLink)
                f.write(modelLine)

                if model['info'] != '':
                    f.write(model['info'] + "\n\n")
                else:
                    f.write("No description has been given for this project.\n\n")

                libraryDict.append({
                    'name': model['name']
                ,   'folder': model['folder']
                ,   'path': model['path']
                ,   'url': playerLink + GITHUB_REPO + model['path']
                ,   'info': model['info']
                })

    f.close()
    return libraryDict

libraryDict = generatePage("LIBRARY.md", NTANGO_PLAYER, NTANGO_EDITOR)
generatePage("test/TESTING.md", TEST_PLAYER, TEST_EDITOR)

with open(os.getcwd() + "/library.json", "w") as outfile:
    libraryDict = { 'success': True, 'models': libraryDict }
    json.dump(libraryDict, outfile, indent = 2)
