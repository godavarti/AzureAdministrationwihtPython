from azure.mgmt.resource import ResourceManagementClient
from azure.identity import AzureCliCredential
import os
import json

# Acquire a credential object using CLI-based authentication.
credential = AzureCliCredential()


# Retrieve subscription ID from environment variable.
subscription_id = "4206bb26-a87b-45c4-bfb8-b2223094823f"
resource_client = ResourceManagementClient(credential, subscription_id)
#read List of resourcegrpups in subscription
"""resourcegroups_list = resource_client.resource_groups.list()
for resource_group in resourcegroups_list:
    print(resource_group.name)
    print(resource_group.location)"""
    
#read List of resoruces in resource group     
  
resoruce_page_collection =  resource_client.resources.list_by_resource_group("DES_UAT_GlobalListAPI")  #Returns an object of type ItemPaged 
#print(resoruce_page_collection.by_page())
resource_collection =[]

for r in resoruce_page_collection:
    rpage_str =str(r)
    rpage_str.replace("'","\"")
    rpage_str =rpage_str[1:len(rpage_str)-1]
    stringcollection = rpage_str.split(",")
    resource_collection.extend(stringcollection)
    #for s in stringcollection:
        #print(s)
        
#print(resource_collection)
number_of_resoruces = len(resource_collection)
print ("number of collections :",number_of_resoruces )
for i in range(0,number_of_resoruces):
    if (resource_collection[i].find("name")!=-1):
        print(resource_collection[i])
    if (resource_collection[i].find("type")!=-1):
         print(resource_collection[i])
    #print(resource_collection[i])   


    




    


#resource_list =resoruce_page_collection.by_page()
#for r in resource_list:
 #   print (r)
  #  break    
     


