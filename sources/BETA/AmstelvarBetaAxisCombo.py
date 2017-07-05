from itertools import product, izip
# http://stackoverflow.com/questions/5228158/cartesian-product-of-a-dictionary-of-lists
def my_product(dicts):
    return (dict(izip(dicts, x)) for x in product(*dicts.itervalues()))

options = {
    "wght": [38, 88, 250],
    "wdth": [60, 402],
    "opsz": [10, 14, 72],
    "GRAD": [25, 88, 250],
    }

my_options = []
for item in my_product(options):
    my_options.append(item)   
#print len(my_options)

combos = []

count = 0
for item in my_options:
    defaults = [1 for v in item.values() if v in [88, 402, 14]]
    if len(defaults) == 3:
        continue
    combo = []
    for k, v in item.items():
        if v not in [88, 402, 14]:
            combo.append((k, v))
    combos.append(combo)
    count+=1
print count

locations = {}
for c in combos:
    name = ""
    location = {}
    for a, v in c:
        name+= "%s=%s " % (a, v)
        location[a] = v
    locations[name] = location
    print name
    
from gxmutator import generateInstance
for styleName, location in locations.items():
    try:
        generateInstance('AmstelvarAlpha-VF.ttf', location, targetDirectory="instances", styleName=styleName)
    except:
        print "TTLibError", location
	