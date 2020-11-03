import os
import sys
import re
import json

def main():
    filename = sys.argv[1]
    print("opening", filename)
    file = open(filename, 'r')

    spec = {}
    currentBlock = ""
    currentPart = ""
    currentProperty = ""
    propetyDetails = 0
    partblock = None
    for line in file.readlines():
        if bool(re.match('^# ', line)): # Block
            currentBlock = line.strip().replace("# ","")
            if currentBlock != "key":
                spec[currentBlock] = []
        elif currentBlock == "key":
            continue
        elif bool(re.match('^## ', line)): # Part
            currentPart = line.strip().replace("## ","")
            if (partblock != None):
                spec[currentBlock].append(partblock)
            partblock = {}
            partblock["title"] = currentPart
            partblock["type"] = "object"
            partblock["required"] = []
            partblock["properties"] = {}
        elif bool(re.match('^\* ', line)): # properties, construct JSON schema data here
            currentProperty = line.strip().replace("* ","")
            partblock["properties"][currentProperty] = {}
            propertyDetails = 0
        elif bool(re.match('^    * ', line)): # property details, construct JSON schema data here
            fieldProperty = line.strip().replace("* ","")
            if propertyDetails == 0:
                # First field, assume description
                partblock["properties"][currentProperty]["description"] = fieldProperty
                propertyDetails = propertyDetails + 1
            else:
                if "required" in fieldProperty:
                    partblock["required"].append(currentProperty)
                if fieldProperty.startswith("unit:"):
                    partblock["properties"][currentProperty]["comment"] = "units of " + fieldProperty.replace("unit:","").strip()
                if fieldProperty.startswith("type:"):
                    if "float" in fieldProperty or "int" in fieldProperty:
                        partblock["properties"][currentProperty]["type"] = "numeric"
                    elif "string" in fieldProperty:
                        partblock["properties"][currentProperty]["type"] = "string"
                if fieldProperty.startswith("format:"):
                        partblock["properties"][currentProperty]["examples"] = []
                        for example in fieldProperty.replace("format:", "").split(','):
                            partblock["properties"][currentProperty]["examples"].append(example.strip())
        else:
            continue

    # print(spec)
    with open('spec.json', 'w') as outfile:
        json.dump(spec, outfile, indent=4)



if __name__ == "__main__":
    main()