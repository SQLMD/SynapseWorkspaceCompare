import json

from os import listdir,remove,makedirs
from os.path import join

ARMFilename = 'data/TemplateForWorkspace2.json'

with open(ARMFilename) as f:
    all_data = json.load(f)

resources = all_data['resources']

#dirs = ['datasets','linkedServices','notebooks','others','pipelines','sqlscripts','triggers','integrationRuntimes','dataflows','credentials','bigDataPools','sqlPools','managedVirtualNetworks']
dirs = ['datasets','linkedServices','pipelines']
folderNumber = "2"

for dir in dirs:

    file_dir = 'data/'+dir+folderNumber

    try:
        makedirs(file_dir)
    except Exception as e:
        pass
    try:
        if dir == "others" :
            makedirs(file_dir+"/default")
    except: 
        pass

    try:
        if dir == "managedVirtualNetworks" :
            makedirs(file_dir+"/managedPrivateEndpoints2")
    except:
            pass
    
    try:
        if dir == "managedVirtualNetworks" :
            makedirs(file_dir+"/managedPrivateEndpoints2/default")
    except:
        pass

    try:
        makedirs('data/'+dir + "_diffs")
    except:
        pass
    
    filelist = [ f for f in listdir(file_dir) if f.endswith(".json") ]
    for f in filelist:
        remove(join(file_dir, f))

for  resource in resources:
    resource_name = resource['name']
    folder = "data" + resource['type'][28:] # "Microsoft.Synapse/workspaces/pipelines":
    if folder == "data/managedVirtualNetworks/managedPrivateEndpoints":
        folder = "data/managedVirtualNetworks2/managedPrivateEndpoints"

    filename = resource_name[39:-3]

    resource_filename = folder+folderNumber+'/'+filename+'.json'


    with open(resource_filename, 'w') as f:
        json.dump(resource, f, indent=4)



