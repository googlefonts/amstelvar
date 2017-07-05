# from https://github.com/fonttools/fonttools/blob/master/Lib/fontTools/varLib/mutator.py
from fontTools.misc.py23 import *
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
from fontTools.varLib import _GetCoordinates, _SetCoordinates
from fontTools.varLib.models import VariationModel, supportScalar, normalizeLocation
import os

def generateInstance(varfilename, location, targetDirectory=None, styleName=None):
	u"""
	Instantiate an instance of a variation font at the specified location.
	Keyword arguments:
	    varfilename -- a variation font file path
	    location -- a dictionary of axis tag and value {"wght": 0.75, "wdth": -0.5}
	"""
	# make a custom file name from the location e.g. VariationFont-wghtXXX-wdthXXX.ttf
	instanceName = ""
	for k,v in location.items():
		instanceName += "-%s%s" % (k, v)
	
	if not styleName:
		styleName = instanceName[1:]
	
	outfile = os.path.splitext(os.path.basename(varfilename))[0] + instanceName + '.ttf'
	
	if targetDirectory:
		if not os.path.exists(targetDirectory):
			os.makedirs(targetDirectory)
		outfile = os.path.join(targetDirectory, outfile)

	#print "Loading GX font"
	varfont = TTFont(varfilename)
	
	# Set the instance name IDs in the name table
	platforms=((1, 0, 0), (3, 1, 0x409)) # Macintosh and Windows
	for platformID, platEncID, langID in platforms:
		"""
		familyName = varfont['name'].getName(1, platformID, platEncID, langID) # 1 Font Family name
		if not familyName:
			continue
		familyName = familyName.toUnicode() # NameRecord to unicode string
		"""
		familyName = unicode("AmstelvarAlpha")
		styleName = unicode(styleName)
		fullFontName = " ".join([familyName, styleName])
		postscriptName = fullFontName.replace(" ", "-")
		varfont['name'].setName(styleName, 2, platformID, platEncID, langID) # 2 Font Subfamily name
		varfont['name'].setName(fullFontName, 4, platformID, platEncID, langID) # 4 Full font name
		varfont['name'].setName(postscriptName, 6, platformID, platEncID, langID) # 6 Postscript name for the font
		varfont['name'].setName(familyName, 1, platformID, platEncID, langID) # 2 Font Subfamily name
		identifier = "Version 0.000;NONE;%s %s" % (familyName, styleName)
		varfont['name'].setName(identifier, 3, platformID, platEncID, langID) # 3 Unique font identifier (e.g. Version 0.000;NONE;Promise Bold Regular)
		varfont['name'].setName(styleName, 17, platformID, platEncID, langID)
		# Other important name IDs
		# 25 Variations PostScript Name Prefix

	fvar = varfont['fvar']
	axes = {a.axisTag:(a.minValue,a.defaultValue,a.maxValue) for a in fvar.axes}
	# TODO Round to F2Dot14?
	location = normalizeLocation(location, axes)
	# Location is normalized now
	#print "Normalized location:", location

	gvar = varfont['gvar']
	for glyphname,variations in gvar.variations.items():
		coordinates,_ = _GetCoordinates(varfont, glyphname)
		for var in variations:
			scalar = supportScalar(location, var.axes)
			if not scalar: continue
			# TODO Do IUP / handle None items
			varcoords = []
			for coord in var.coordinates:
				# TODO temp hack to avoid NoneType
				if coord is None:
					varcoords.append((0, 0))
				else:
					varcoords.append(coord)
			coordinates += GlyphCoordinates(varcoords) * scalar
			#coordinates += GlyphCoordinates(var.coordinates) * scalar
		_SetCoordinates(varfont, glyphname, coordinates)

	#print "Removing GX tables"
	for tag in ('fvar','avar','gvar'):
		if tag in varfont:
			del varfont[tag]

	print "Saving instance font", outfile
	varfont.save(outfile)
