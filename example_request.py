import requests
import pandas as pd
import json


url = 'http://127.0.0.1:8000/predict/'

'''
JSON sample for a normal record with values.
'''
myobj = {"borough": "BX", "firecomp": "E239", "sanitsub": "5C", "zonedist1": "R6A", "splitzone": "Y", "irrlotcode": "N",
         "zonemap": "16D", "block": 1004, "lot": 54, "schooldist": 15.0, "council": 39.0, "zipcode": 11215.0,
         "policeprct": 78.0, "healthcenterdistrict": 39.0, "healtharea": 4600.0, "sanitboro": 3.0, "sanitdistrict": 6.0,
         "landuse": 4.0, "proxcode": 0.0, "lottype": 5.0, "bsmtcode": 5.0, "yearbuilt": 1920, "tract2010": 137,
         "easements": 0, "lotarea": 1845, "bldgarea": 3075, "comarea": 1435, "resarea": 1640, "officearea": 0,
         "retailarea": 1435, "garagearea": 0, "strgearea": 0, "factryarea": 0, "otherarea": 0, "numbldgs": 1,
         "numfloors": 3.0, "unitstotal": 4, "lotfront": 20.5, "lotdepth": 90.0, "bldgfront": 20.5, "bldgdepth": 40.0,
         "assessland": 19075, "assesstot": 110487, "exemptland": 0, "exempttot": 0, "builtfar": 1.67, "xcoord": 987885.0,
         "ycoord": 183293.0}

x = requests.post(url, json=myobj, headers = {"token": "2023"})
print(x.text)


'''
JSON sample for records with Nan values. If a feature has Nan value it must be represented by `None` in JSON or
remove its field from JSON.
'''
myobj = {'borough': None, 'block': None, 'lot': None, 'schooldist': None, 'council': None, 'zipcode': None, 'firecomp': None,
        'policeprct': None, 'healthcenterdistrict': None, 'healtharea': None, 'sanitboro': None, 'sanitdistrict': None,
        'sanitsub': None, 'zonedist1': None, 'zonedist2': None, 'zonedist3': None, 'zonedist4': None, 'overlay1': None,
        'overlay2': None, 'spdist1': None, 'spdist2': None, 'spdist3': None, 'ltdheight': None, 'splitzone': None,
        'landuse': None, 'easements': None, 'lotarea': None, 'bldgarea': None, 'comarea': None, 'resarea': None,
        'officearea': None, 'retailarea': None, 'garagearea': None, 'strgearea': None, 'factryarea': None, 'otherarea': None,
        'numbldgs': None, 'numfloors': None, 'unitstotal': None, 'lotfront': None, 'lotdepth': None, 'bldgfront': None,
        'bldgdepth': None, 'ext': None, 'proxcode': None, 'irrlotcode': None, 'lottype': None, 'bsmtcode': None,
        'assessland': None, 'assesstot': None, 'exemptland': None, 'exempttot': None, 'yearbuilt': None, 'yearalter1': None,
        'yearalter2': None, 'histdist': None, 'landmark': None, 'builtfar': None, 'tract2010': None, 'xcoord': None,
        'ycoord': None, 'zonemap': None
         }


x = requests.post(url, json=myobj, headers = {"token": "2023"})
print(x.text)

