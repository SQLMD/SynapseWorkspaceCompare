import json

from os import listdir,remove,makedirs
from os.path import join

ARMFilename = 'data/TemplateForWorkspace.json'

with open(ARMFilename) as f:
    all_data = json.load(f)

resources = all_data['resources']

# dirs = ['datasets','linkedServices','notebooks','others','pipelines','sqlscripts','triggers','integrationRuntimes','dataflows','credentials','bigDataPools','sqlPools']
dirs = ['datasets','linkedServices','pipelines']
folderNumber = "1"

for dir in dirs:

    file_dir = 'data/'+dir+folderNumber
    try:
        makedirs(file_dir)
        if dir == "others":
            makedirs("data/others"+folderNumber+"/default")
    except Exception as e:
        pass
    try:
        makedirs("data/"+dir + "_diffs")
    except:
        pass
    
    filelist = [ f for f in listdir(file_dir) if f.endswith(".json") ]
    for f in filelist:
        remove(join(file_dir, f))

for  resource in resources:
    resource_name = resource['name']
    folder = "data" + resource['type'][28:] # "Microsoft.Synapse/workspaces/pipelines":
    
    filename = resource_name[39:-3]
    resource_filename = folder+folderNumber+'/'+filename+'.json'
#    print(resource_filename)
    with open(resource_filename, 'w') as f:
        json.dump(resource, f, indent=4)



