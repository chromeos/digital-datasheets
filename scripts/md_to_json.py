import os
import sys
import re
import json

fw_required = ["battery charger",
"PMIC",
"power sequencing",
"audio codec",
"wlan module",
"wwan module",
"microcontroller/ec/asic",
"usb-c port controller",
"usb-c redriver/retimer",
"usb-c mux",
"usb-c mux/port controller",
"redriver",
"bridge chip",
"accelerometer",
"accelerometer/gyro",
"magnetic sensor",
"ssd",
"sd card reader",
"dram",
"rom"]

default_required = ["datasheetVersion", "manufacturer","mpn"]

sw_required = fw_required
sw_required.append("display backlight driver")

def main():
    filename = sys.argv[1]
    print("opening", filename)
    file = open(filename, 'r')

    spec = {} # Represents the whole spec
    currentBlock = "" # Represents the name/key of the current category
    currentPart = "" # represents the name/key of the part in the category
    currentProperty = "" # represents the property of the current part
    propetyDetails = 0 # represents one of the details of the current property
    partblock = None
    for line in file.readlines():
        if bool(re.match('^# ', line)): # Block
            if (partblock != None and currentBlock != None):
                spec[currentBlock]["oneOf"].append(partblock)
            currentBlock = line.strip().replace("# ","")
            if currentBlock != "key":
                spec[currentBlock] = {
                    "$id": "https://github.com/chromeos/digital-datasheets/blob/main/part-spec/" + currentBlock + ".json",
                    "$schema": "http://json-schema.org/draft-07/schema#",
                    "type": "object",
                    "title": currentBlock,
                    "oneOf": []
                }
                currentPart = ""
        elif currentBlock == "key":
            continue
        elif bool(re.match('^## ', line)): # Part
            if partblock != None and partblock != {}  :
                if currentPart in sw_required:
                    partblock["properties"]["softwareVersion"] = {
                        "description":"software version of the part",
                        "type":"string"
                        }
                if (currentPart in fw_required):
                    partblock["properties"]["firmwareVersion"] = {
                        "description":"firmware version of the part",
                        "type":"string"
                        }
                partblock["properties"]["rohs"] = {
                    "description": "whether a part is rohs compliant",
                    "type": "string",
                    "enum": ["yes", "no"]}

                partblock["properties"]["automotive"] = {
                    "description": "whether a part is automotive qualified",
                    "type": "string",
                    "enum": ["yes", "no"]
                }
                partblock["properties"]["pins"] = {
                    "description": "array of pin objects with associated properties",
                    "type": "array",
                    "items": {"$ref": "definitions.json#/pinSpec"}
                }
                spec[currentBlock]["oneOf"].append(partblock)
            currentPart = line.strip().replace("## ","")
            partblock = {}
            partblock["title"] = currentPart
            partblock["type"] = "object"
            partblock["required"] = []
            partblock["properties"] = {}
            partblock["properties"]["manufacturer"] = {
                "description": "company that manufacturers the part",
                "type": "string"
            }
            partblock["required"].append("manufacturer")
            partblock["properties"]["mpn"] = {
                "description": "manufacturer part number",
                "type": "string"
            }
            partblock["required"].append("mpn")
            if currentPart != "testpoint":
                partblock["required"].append("datasheetVersion")
                partblock["properties"]["datasheetVersion"] = {
                    "description": "datasheet version encoded in this document",
                    "type": "string"
                }
                partblock["properties"]["eolDate"] = {
                    "description": "date this part will no longer be supported by manufacturer",
                    "type": "string",
                    "format": "date"
                }



# "manufacturer",
# "mpn"
# "datasheetVersion"
# "eolDate"
# <any other fields for that part>
# "firmwareVersion"
# "softwareVersion"
# "rohs"
# "automotive"

        elif bool(re.match('^\* ', line)): # properties, construct JSON schema data here
            currentProperty = line.strip().replace("* ","")
            # Make this conditional
            if currentProperty not in partblock["properties"].keys():
                partblock["properties"][currentProperty] = {}
            propertyDetails = 0
        elif bool(re.match('^    * ', line)): # property details, construct JSON schema data here
            fieldProperty = line.strip().replace("* ","")
            if propertyDetails == 0:
                # First field, assume description
                partblock["properties"][currentProperty]["description"] = fieldProperty
                propertyDetails = propertyDetails + 1
            else:
                if fieldProperty.startswith("required"):
                    if currentProperty not in default_required:
                        partblock["required"].append(currentProperty)
                elif "required" in fieldProperty and "optional" in fieldProperty:
                    partblock["properties"][currentProperty]["conditionallyRequired"] = True
                elif fieldProperty.startswith("unit"):
                    partblock["properties"][currentProperty]["comment"] = "units of " + fieldProperty.split(':')[1].strip()
                elif fieldProperty.startswith("type"):
                    if "float" in fieldProperty or "int" in fieldProperty:
                        partblock["properties"][currentProperty]["type"] = "number"
                    elif "string" in fieldProperty:
                        partblock["properties"][currentProperty]["type"] = "string"
                    else:
                        print("unrecognized json type", fieldProperty)
                elif fieldProperty.startswith("format:"):
                        partblock["properties"][currentProperty]["examples"] = []
                        for example in fieldProperty.replace("format:", "").split(','):
                            partblock["properties"][currentProperty]["examples"].append(example.strip())
                # elif fieldProperty.startswith("firmwareVersion"):
                #     partblock["properties"][currentProperty]["firmwareVersion"]
                # elif fieldProperty.startsith("softwareVersion")
                # elif fieldProperty.startswith("eolDate")
                # elif fieldProperty.startswith("automotivew")
                # elif fieldProperty.startswith("rohs")
                # elif fieldProperty.startswith("datasheetVersion")
                else:
                    if not fieldProperty.startswith("optional"):
                        print("unrecognized property", fieldProperty)
        else:
            continue

    # print(spec)
    for block in spec.keys():
        with open('part-spec/' + block.replace('/', '_').replace(' ', '_') + '.json', 'w') as outfile:
            json.dump(spec[block], outfile, indent=4)



if __name__ == "__main__":
    main()