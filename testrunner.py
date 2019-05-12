import json

import rest

# load data from local json file
with open('json/apilist.json') as f:
    json_data = json.load(f)

# print(apilist)
# print(apilist["urls"][0]["name"])
# Pretty Printing JSON string back
# print(json.dumps(apilist, indent = 4, sort_keys=True))

# loop json data
for myapilist in json_data:
    # print(myapilist)
    # for each api
    for api in json_data[myapilist]:

        # get api url
        url = api["url"]

        # for each of the verbs
        for verbs in api["verbs"]:

            # get the parameters if any
            name = verbs["name"]
            verbs = verbs["params"]
            print(name, verbs)

            # test if params null
            if verbs is None:
                print('verbs is None')
                rest.get(url)
