#!/usr/bin/env python3

"""
manipulate yaml
"""

# install yaml; not a standard lib
import yaml

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]
        
    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)
    
    # ## open a new file in write mode
    # with open("galaxyguide.yaml", "w") as zfile:
    
    #     ## use the YAML library
    #     ## USAGE: yaml.dump(input data, file like object)
    #     ## unlike JSON, the YAML lib uses .dump() to
    #     ## create YAML strings and write to files
    #     ## the JSON lib uses .dump() to create a string and .dumps() to write to files
    #     yaml.dump(hitchhikers, zfile)
    
    ## Create the YAML string
    yamlString = yaml.dump(hitchhikers)
    
    ## Display a single string of YAML
    print(yamlString)
    print(type(yamlString))

    ## Open a blob of YAML data
    with open("./api_lab8_json/myYAML.yml", "r") as yf:
        ## convert YAML into Python data structures (lists and dictionaries)
        pyyammy = yaml.load(yf)
    # display our new Python data
    print(pyyammy)
    print(type(pyyammy))

    pyyammy[0]['apps'].append('minecraft')
    ## Did the Python data change?
    print(pyyammy)
    ## open a file to dump out to
    with open("./api_lab8_json/myYAML.yml.updated", "w") as myf:
    ## use the YAML library
    ## USAGE: yaml.dump(input data, file like object)
        yaml.dump(pyyammy, myf)
    
if __name__ == "__main__":
    main()
