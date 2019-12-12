# License: Apache 2.0

from __future__ import print_function

# from glyphNameFormatter.data import name2unicode_AGD
from mutatorMath.ufo.document import DesignSpaceDocumentWriter, DesignSpaceDocumentReader
from designSpaceDocument import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor, RuleDescriptor
#from fontTools.designspaceLib import DesignSpaceDocument, SourceDescriptor, InstanceDescriptor, AxisDescriptor, RuleDescriptor

from fontmake.font_project import FontProject
from fontTools.varLib import build
from fontTools.varLib.mutator import instantiateVariableFont
from defcon import Font
import shutil
from distutils.dir_util import copy_tree
import os

	
def buildDesignSpace(sources, instances, axes):
	# use DesignSpaceDocument because it supports axis labelNames
	doc = DesignSpaceDocument()
	
	for source in sources:
		s = SourceDescriptor()
		s.path = source["path"]
		s.name = source["name"]
		s.copyInfo = source["copyInfo"]
		s.location = source["location"]
		s.familyName = source["familyName"]
		s.styleName = source["styleName"]
		doc.addSource(s)
	
	for instance in instances:
		i = InstanceDescriptor()
		i.location = instance["location"]
		i.familyName = instance["familyName"]
		i.styleName = instance["styleName"]
		doc.addInstance(i)
	
	for axis in axes:
		a = AxisDescriptor()
		a.minimum = axis["minimum"]
		a.maximum = axis["maximum"]
		a.default = axis["default"]
		a.name = axis["name"]
		a.tag = axis["tag"]
		for languageCode, labelName in axis["labelNames"].items():
			a.labelNames[languageCode] = labelName
		a.map = axis["map"]
		doc.addAxis(a)
		
	return doc

def buildGlyphSet(dflt, fonts):
	# fill the glyph set with default glyphs
	for font in fonts:
		for glyph in dflt:
			glyphName = glyph.name
			if glyphName not in font and glyphName not in composites:
				font.insertGlyph(glyph)
				font[glyphName].lib['com.typemytype.robofont.mark'] = [0, 0, 0, 0.25] # dark grey

# def buildComposites(composites, fonts):
# 	# build the composites
# 	for font in fonts:
# 		for glyphName in composites.keys():
# 			font.newGlyph(glyphName)
# 			composite = font[glyphName]
# 			composite.unicode = name2unicode_AGD[glyphName]
			
# 			value = composites[glyphName]
# 			items = value.split("+")
# 			base = items[0]
# 			items = items[1:]
	
# 			component = composite.instantiateComponent()
# 			component.baseGlyph = base
# 			baseGlyph = font[base]
# 			composite.width = baseGlyph.width
# 			composite.appendComponent(component)
	
# 			for item in items:
# 				baseName, anchorName = item.split("@")
# 				component = composite.instantiateComponent()
# 				component.baseGlyph = baseName
# 				anchor = _anchor = None
# 				for a in baseGlyph.anchors:
# 					if a["name"] == anchorName:
# 						anchor = a
# 				for a in font[baseName].anchors:
# 					if a["name"] == "_"+anchorName:
# 						_anchor = a
# 				if anchor and _anchor:
# 					x = anchor["x"] - _anchor["x"]
# 					y = anchor["y"] - _anchor["y"]
# 					component.move((x, y))
# 				composite.appendComponent(component)
# 			composite.lib['com.typemytype.robofont.mark'] = [0, 0, 0, 0.5] # grey

def setGlyphOrder(glyphOrder, fonts):
	# set the glyph order
	for font in fonts:
		font.glyphOrder = glyphOrder

def clearAnchors(fonts):
	# set the glyph order
	for font in fonts:
		for glyph in font:
		    glyph.clearAnchors()

def saveMasters(fonts, master_dir="master_ufo"):
	# save in master_ufo directory
	for font in fonts:
		path = os.path.join(master_dir, os.path.basename(font.path))

		#added this check because the "master_ufo" folder is getting removed at the beginning of this script
		if not os.path.exists(path):
			os.makedirs(path)
		font.save(path)

with open("sources/Amstelvar-NewSpaceNames/Amstelvar.enc") as enc:
	glyphOrder = enc.read().splitlines()

# dictionary of glyph construction used to build the composite accents
composites = {
	"Agrave": "A+grave@top",
	"Aacute": "A+acute@top",
	"Acircumflex": "A+circumflex@top",
	"Atilde": "A+tilde@top",
	"Adieresis": "A+dieresis@top",
	"Aring": "A+ring@top",
	"Ccedilla": "C+cedilla@bottom",
	"Egrave": "E+grave@top",
	"Eacute": "E+acute@top",
	"Ecircumflex": "E+circumflex@top",
	"Edieresis": "E+dieresis@top",
	"Igrave": "I+grave@top",
	"Iacute": "I+acute@top",
	"Icircumflex": "I+circumflex@top",
	"Idieresis": "I+dieresis@top",
	"Ntilde": "N+tilde@top",
	"Ograve": "O+grave@top",
	"Oacute": "O+acute@top",
	"Ocircumflex": "O+circumflex@top",
	"Otilde": "O+tilde@top",
	"Odieresis": "O+dieresis@top",
	"Ugrave": "U+grave@top",
	"Uacute": "U+acute@top",
	"Ucircumflex": "U+circumflex@top",
	"Udieresis": "U+dieresis@top",
	"Yacute": "Y+acute@top",
	"agrave": "a+grave@top",
	"aacute": "a+acute@top",
	"acircumflex": "a+circumflex@top",
	"atilde": "a+tilde@top",
	"adieresis": "a+dieresis@top",
	"aring": "a+ring@top",
	"ccedilla": "c+cedilla@bottom",
	"egrave": "e+grave@top",
	"eacute": "e+acute@top",
	"ecircumflex": "e+circumflex@top",
	"edieresis": "e+dieresis@top",
	"igrave": "dotlessi+grave@top",
	"iacute": "dotlessi+acute@top",
	"icircumflex": "dotlessi+circumflex@top",
	"idieresis": "dotlessi+dieresis@top",
	"ntilde": "n+tilde@top",
	"ograve": "o+grave@top",
	"oacute": "o+acute@top",
	"ocircumflex": "o+circumflex@top",
	"otilde": "o+tilde@top",
	"odieresis": "o+dieresis@top",
	"ugrave": "u+grave@top",
	"uacute": "u+acute@top",
	"ucircumflex": "u+circumflex@top",
	"udieresis": "u+dieresis@top",
	"yacute": "y+acute@top",
	"ydieresis": "y+dieresis@top",
}

print ("Cleaning up...")

# clean up previous build
if os.path.exists("instances"):
	shutil.rmtree("instances", ignore_errors=True)
if os.path.exists("master_ttf"):
	shutil.rmtree("master_ttf", ignore_errors=True)
if os.path.exists("master_ufo"):
	shutil.rmtree("master_ufo", ignore_errors=True)
if os.path.exists("master_ttf_interpolatable"):
	shutil.rmtree("master_ttf_interpolatable", ignore_errors=True)

# Remove temporary 1-drawings
if os.path.exists("sources/1-drawings"):
	shutil.rmtree("sources/1-drawings", ignore_errors=True)


# New
src = {	"sources/Amstelvar-NewSpaceNames/Italic",
		
		}
	

src_dir = "sources/1-drawings"
master_dir = "master_ufo"
instance_dir = "instances"

# Copy sources to temporary 1-drawings
for source in src:
	copy_tree(source, src_dir)


# use a temporary designspace to build instances with mutator math
familyName = "Amstelvar"
tmpDesignSpace = "tmp.designspace"
doc = DesignSpaceDocumentWriter(tmpDesignSpace)
# sources
doc.addSource(path="sources/1-drawings/Amstelvar-Italic.ufo", name="Amstelvar-Italic.ufo", location=dict(wght=0, wdth=0, opsz=0), styleName="Italic", familyName=familyName, copyLib=False, copyGroups=False, copyInfo=False, copyFeatures=False, muteKerning=False, muteInfo=False, mutedGlyphNames=None)

# axes
doc.addAxis(tag="wght", name="wght", minimum=100, maximum=900, default=400, warpMap=None)
doc.addAxis(tag="wdth", name="wdth", minimum=50, maximum=125, default=100, warpMap=None)
doc.addAxis(tag="opsz", name="opsz", minimum=8, maximum=144, default=14, warpMap=None)






# instances
instances = [
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wght100-wdth125.ufo", location=dict(wght=100, wdth=125, opsz=144), styleName="opsz144-wght100-wdth125", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wght100-wdth075.ufo", location=dict(wght=100, wdth=87, opsz=144), styleName="opsz144-wght100-wdth075", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wght100-wdth50.ufo", location=dict(wght=100, wdth=75, opsz=144), styleName="opsz144-wght100-wdth50", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
	
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wght900-wdth125.ufo", location=dict(wght=900, wdth=125, opsz=144), styleName="opsz144-wght900-wdth125", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wght900-wdth075.ufo", location=dict(wght=900, wdth=76, opsz=144), styleName="opsz144-wght900-wdth075", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wght900-wdth50.ufo", location=dict(wght=900, wdth=75, opsz=144), styleName="opsz144-wght900-wdth50", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
	
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wdth125.ufo", location=dict(wght=400, wdth=125, opsz=144), styleName="opsz144-wdth125", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wdth075.ufo", location=dict(wght=400, wdth=80, opsz=144), styleName="opsz144-wdth075", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
#	dict(fileName="instances/Amstelvar-Italic-opsz144-wdth50.ufo", location=dict(wght=400, wdth=75, opsz=144), styleName="opsz144-wdth50", familyName=familyName, postScriptFontName=None, styleMapFamilyName=None, styleMapStyleName=None),
]
for instance in instances:
	doc.startInstance(**instance)
	doc.writeInfo()
	doc.writeKerning()
	doc.endInstance()

doc.save()
# read and process the designspace
doc = DesignSpaceDocumentReader(tmpDesignSpace, ufoVersion=2, roundGeometry=False, verbose=False)
print ("Reading DesignSpace...")
doc.process(makeGlyphs=True, makeKerning=True, makeInfo=True)
os.remove(tmpDesignSpace) # clean up

# update the instances with the source fonts
# print str(instances) + ' instances! '
for instance in instances:
	fileName = os.path.basename(instance["fileName"])
	source_path = os.path.join(src_dir, fileName)
	instance_path = os.path.join(instance_dir, fileName)
	source_font = Font(source_path)
	instance_font = Font(instance_path)
	# insert the source glyphs in the instance font
	for glyph in source_font:
		instance_font.insertGlyph(glyph)
	master_path = os.path.join(master_dir, fileName)
	instance_font.save(master_path)

designSpace = "sources/Amstelvar-NewSpaceNames/Italic/Amstelvar-Italic-010.designspace"
sources = [
	dict(path="master_ufo/Amstelvar-Italic.ufo", name="Amstelvar-Italic.ufo", location=dict( wght=400, wdth=100, opsz=14, GRAD=0), styleName="Regular", familyName=familyName, copyInfo=True),
	
##	Main 
	dict(path="master_ufo/Amstelvar-Italic-GRAD-1.ufo", name="Amstelvar-Italic-GRAD-1.ufo", location=dict(GRAD=-1), styleName="GRAD-1", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-GRAD1.ufo", name="Amstelvar-Italic-GRAD1.ufo", location=dict(GRAD=1), styleName="GRAD1", familyName=familyName, copyInfo=False),	
	dict(path="master_ufo/Amstelvar-Italic-wght100.ufo", name="Amstelvar-Italic-wght100.ufo", location=dict(wght=100), styleName="wght100", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-wght900.ufo", name="Amstelvar-Italic-wght900.ufo", location=dict(wght=900), styleName="wght900", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz8.ufo", name="Amstelvar-Italic-opsz8.ufo", location=dict(opsz=8), styleName="opsz8", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz36.ufo", name="Amstelvar-Italic-opsz36.ufo", location=dict(opsz=36), styleName="opsz36", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz84.ufo", name="Amstelvar-Italic-opsz84.ufo", location=dict(opsz=84), styleName="opsz84", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz144.ufo", name="Amstelvar-Italic-opsz144.ufo", location=dict(opsz=144), styleName="opsz144", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-wdth50.ufo", name="Amstelvar-Italic-wdth50.ufo", location=dict(wdth=50), styleName="wdth50", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-wdth125.ufo", name="Amstelvar-Italic-wdth125.ufo", location=dict(wdth=125), styleName="wdth125", familyName=familyName, copyInfo=False),

# ##	Parametric
# 	dict(path="master_ufo/Amstelvar-Italic-XOPQmin.ufo", name="Amstelvar-Italic-XOPQmin.ufo", location=dict(XOPQ=36), styleName="XOPQmin", familyName=familyName, copyInfo=False),
# 	dict(path="master_ufo/Amstelvar-Italic-XOPQmax.ufo", name="Amstelvar-Italic-XOPQmax.ufo", location=dict(XOPQ=526), styleName="XOPQmax", familyName=familyName, copyInfo=False),
# 	dict(path="master_ufo/Amstelvar-Italic-XTRAmin.ufo", name="Amstelvar-Italic-XTRAmin.ufo", location=dict(XTRA=444), styleName="XTRAmin", familyName=familyName, copyInfo=False),
# 	dict(path="master_ufo/Amstelvar-Italic-XTRAmax.ufo", name="Amstelvar-Italic-XTRAmax.ufo", location=dict(XTRA=1104), styleName="XTRAmax", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YOPQmin.ufo", name="Amstelvar-Italic-YOPQmin.ufo", location=dict(YOPQ=14), styleName="YOPQmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YOPQmax.ufo", name="Amstelvar-Italic-YOPQmax.ufo", location=dict(YOPQ=125), styleName="YOPQmax", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTLCmin.ufo", name="Amstelvar-Italic-YTLCmin.ufo", location=dict(YTLC=445), styleName="YTLCmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTLCmax.ufo", name="Amstelvar-Italic-YTLCmax.ufo", location=dict(YTLC=600), styleName="YTLCmax", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTUCmin.ufo", name="Amstelvar-Italic-YTUCmin.ufo", location=dict(YTUC=550), styleName="YTUCmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTUCmax.ufo", name="Amstelvar-Italic-YTUCmax.ufo", location=dict(YTUC=850), styleName="YTUCmax", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTASmin.ufo", name="Amstelvar-Italic-YTASmin.ufo", location=dict(YTAS=667), styleName="YTASmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTASmax.ufo", name="Amstelvar-Italic-YTASmax.ufo", location=dict(YTAS=867), styleName="YTASmax", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTDEmin.ufo", name="Amstelvar-Italic-YTDEmin.ufo", location=dict(YTDE=140), styleName="YTDEmin", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-YTDEmax.ufo", name="Amstelvar-Italic-YTDEmax.ufo", location=dict(YTDE=340), styleName="YTDEmax", familyName=familyName, copyInfo=False),
# 
##	Multivars
	dict(path="master_ufo/Amstelvar-Italic-opsz84-wght100.ufo", name="Amstelvar-Italic-opsz84-wght100.ufo", location=dict(wght=100, opsz=84), styleName="opsz84-wght100", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz144-wght100.ufo", name="Amstelvar-Italic-opsz144-wght100.ufo", location=dict(wght=100, opsz=144), styleName="opsz144-wght100", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz144-weight100-width50.ufo", name="Amstelvar-Italic-opsz144-weight100-width50.ufo", location=dict(wght=100, opsz=144, wdth=50), styleName="opsz144-weight100-width50", familyName=familyName, copyInfo=False),
	dict(path="master_ufo/Amstelvar-Italic-opsz144-wght400-width50.ufo", name="Amstelvar-Italic-opsz144-wght400-width50.ufo", location=dict(wght=400, opsz=144, wdth=50), styleName="opsz144-wght400-width50", familyName=familyName, copyInfo=False),
	
]
#instances = []
axes = [
	


	dict(minimum=100, maximum=900, default=400, name="wght", tag="wght", labelNames={"en": "wght"}, map=[]),
	dict(minimum=50, maximum=125, default=100, name="wdth", tag="wdth", labelNames={"en": "wdth"}, map=[]),
	dict(minimum=8, maximum=144, default=14, name="opsz", tag="opsz", labelNames={"en": "opsz"}, map=[]),
	dict(minimum=-1, maximum=1, default=0, name="GRAD", tag="GRAD", labelNames={"en": "GRAD"}, map=[]),
	dict(minimum=444, maximum=1104, default=980, name="XTRA", tag="XTRA", labelNames={"en": "XTRA"}, map=[]),
# 	dict(minimum=36, maximum=526, default=176, name="XOPQ", tag="XOPQ", labelNames={"en": "XOPQ"}, map=[]),
	dict(minimum=14, maximum=125, default=54, name="YOPQ", tag="YOPQ", labelNames={"en": "YOPQ"}, map=[]),
	dict(minimum=445, maximum=600, default=500, name="YTLC", tag="YTLC", labelNames={"en": "YTLC"}, map=[]),
	dict(minimum=550, maximum=850, default=750, name="YTUC", tag="YTUC", labelNames={"en": "YTUC"}, map=[]),
	dict(minimum=667, maximum=867, default=767, name="YTAS", tag="YTAS", labelNames={"en": "YTAS"}, map=[]),
	dict(minimum=140, maximum=340, default=240, name="YTDE", tag="YTDE", labelNames={"en": "YTDE"}, map=[]),

]

doc = buildDesignSpace(sources, instances, axes)


#add rule for dollar. Needs to be after doc = buildDesignSpace() because this doc is a DesignSpaceDocument(), rather than the doc above which is a DesignSpaceDocumentReader() object

# r1 = RuleDescriptor()
# r1.name = "heavy-bars-wght"
# r1.conditions.append(dict(name="wght", minimum=800, maximum=850))
# r1.subs.append(("dollar", "dollar.rvrn2"))
# doc.addRule(r1)
	
r2 = RuleDescriptor()
r2.name = "heavier-bars-wght"
r2.conditions.append(dict(name="wght", minimum=800, maximum=900))
r2.subs.append(("dollar", "dollar.rvrn"))
doc.addRule(r2)


doc.write(designSpace)

default = "Amstelvar-Italic.ufo"
# load the default font
default_path = os.path.join(src_dir, default)
dflt = Font(default_path)

sources = [source.name for source in doc.sources]
# take the default out of the source list
sources.remove(default)

print ("Building masters...")

# load font objects
fonts = []
accentFonts = []
for fileName in sources:
	source_path = os.path.join(src_dir, fileName)
	master_path = os.path.join(master_dir, fileName)
	if os.path.exists(master_path):
		# use this updated instance
		font = Font(master_path)
	else:
		font = Font(source_path)
	if fileName not in ['Amstelvar-Italic-opsz144.ufo', 'Amstelvar-Italic-wght100.ufo', 'Amstelvar-Italic-wght900.ufo', 'Amstelvar-Italic-wdth125.ufo', 'Amstelvar-Italic-wdth50.ufo']:
	    accentFonts.append(font)
	fonts.append(font)
	
buildGlyphSet(dflt, fonts)
allfonts = [dflt]+fonts
#buildComposites(composites, accentFonts)
setGlyphOrder(glyphOrder, allfonts)
clearAnchors(allfonts)
saveMasters(allfonts)

# build Variable Font

ufos = [font.path for font in allfonts]
project = FontProject()
project.run_from_ufos(
	ufos, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

#temp changed rel path to work in same dir, was:  ../fonts/Amstelvar-Italic-VF.ttf
outfile = "Amstelvar-Italic-VF.ttf"

#make folder if it doesn't exist
destFolder = "fonts"
if not os.path.exists(destFolder):
    os.makedirs(destFolder)
outfile = os.path.join(destFolder, outfile)



finder = lambda s: s.replace("master_ufo", "master_ttf").replace(".ufo", ".ttf")



varfont, _, _ = build(designSpace, finder)
print ("Saving Variable Font...")
varfont.save(outfile)

print ("Cleaning up...")

# clean up previous build
if os.path.exists("instances"):
	shutil.rmtree("instances", ignore_errors=True)
if os.path.exists("master_ttf"):
	shutil.rmtree("master_ttf", ignore_errors=True)
if os.path.exists("master_ufo"):
	shutil.rmtree("master_ufo", ignore_errors=True)
if os.path.exists("master_ttf_interpolatable"):
	shutil.rmtree("master_ttf_interpolatable", ignore_errors=True)

# Remove temporary 1-drawings
if os.path.exists("sources/1-drawings"):
	shutil.rmtree("sources/1-drawings", ignore_errors=True)

print ("DONE!")

# SUBSET COMMAND
# pyftsubset Amstelvar-Italic-VF.ttf --text-file=ascii-subset.txt --output-file=Amstelvar-Italic-subset-VF.ttf
