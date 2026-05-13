You may need to get the difflib library [your mileage may very depending on what version of python/pip is installed]:

$ python -m pip install --user difflib 


Steps to compare two Synapse workspaces:

1) Copy the ARM template for Workspace 1 from the Azure Repo workspace_publish branch : https://dev.azure.com/BannerBankCorp-LDW/_git/LDW?path=/ldw-dev-synapse/TemplateForWorkspace.json

 Save it in a folder called Data that is a sub-directory of the directory with the python scripts as data/TemplateForWorkspace.json.

2) Copy the ARM template for Workspace 2 from the Azure Repo workspace_publish branch : https://dev.azure.com/BannerBankCorp-LDW/LDW/_git/LDW-Synapse?path=/ldw-dev-synapse-2/TemplateForWorkspace.json

 Save it in a folder called Data that is a sub-directory of the directory with the python scripts data/TemplateForWorkspace2.json.

3) Run the template.py script (it will create most of the folders and store the json objects for each of the resources for workspace 1)

4) Run the template2.py script (it will create most of the folders and store the json objects for each of the resources for workspace 2) [NOTE: I customized these for our two envionments because the managed vnet workspace has some different resources]

5) Run the compare_files.py script. This will create a data/diff.txt file that lists all of the differences and the detail for each of the differences will be in the corresponding folder (e.g. pipelines_diff)





