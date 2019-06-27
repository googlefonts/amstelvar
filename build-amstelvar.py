from fontmake.font_project import FontProject
from fontTools.varLib import build
import shutil
import os
import sys


buildNumberRoman = 116
buildNumberItalic = buildNumberRoman 
#buildNumberItalic = 116

# Roman

romans = [
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-min.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-36.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-84.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-max.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-max-wghtmin.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-84-wghtmin.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-max-wdthmin-wghtmax.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wdthmax.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wdthmin.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wghtmin.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wghtmax.ufo",
	
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-XOPQmax.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-XOPQmin.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-XTRAmax.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-XTRAmin.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-YOPQmax.ufo",
	"sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-YOPQmin.ufo",


]

print ("Cleaning up...")

# clean up previous build
if os.path.exists("instances"):
	shutil.rmtree("instances", ignore_errors=True)
	os.makedirs("instances")
if os.path.exists("master_ttf"):
	shutil.rmtree("master_ttf", ignore_errors=True)
	os.makedirs("master_ttf")
if os.path.exists("master_ufo"):
	shutil.rmtree("master_ufo", ignore_errors=True)
	os.makedirs("master_ufo")
if os.path.exists("master_ttf_interpolatable"):
	shutil.rmtree("master_ttf_interpolatable", ignore_errors=True)
	os.makedirs("master_ttf_interpolatable")


if not os.path.exists("fonts"):
	os.makedirs("fonts")



project = FontProject()
project.run_from_ufos(
	romans, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)










#designSpace = "sources/Amstelvar-NewCharset/Amstelvar-Roman-006.designspace"
designSpace = "sources/Amstelvar-NewCharset/Amstelvar-Roman-008.designspace"






#outfile = "Amstelvar-Roman-VF.ttf"
outfile = "fonts/Amstelvar-Roman-VF.ttf"



finder = lambda s: s.replace("sources/Amstelvar-NewCharset/Roman/", "master_ttf/").replace(".ufo", ".ttf")

varfont, _, _ = build(designSpace, finder)
print ("Saving Variable Font...")





varfont.save(outfile)
print ("DONE!")


# duplicate latest version of Roman with build number
old_name = outfile
base, ext = os.path.splitext(outfile)
new_name = base+str(buildNumberRoman) +ext

shutil.copy(old_name, new_name)





# Italic


italics = [
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-opsz-min.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-opsz-36.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-opsz-84.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-opsz-max.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-wdthmax.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-wdthmin.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-wghtmin.ufo",
	"sources/Amstelvar-NewCharset/Italic/Amstelvar-Italic-wghtmax.ufo",

]

project = FontProject()
project.run_from_ufos(
	italics, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "sources/Amstelvar-NewCharset/Amstelvar-Italic-002.designspace"




outfile = "fonts/Amstelvar-Italic-VF.ttf"



finder = lambda s: s.replace("sources/Amstelvar-NewCharset/Italic/", "master_ttf/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print ("Saving Variable Font...")
varfont.save(outfile)

# duplicate latest version of Italic with build number
old_name = outfile
base, ext = os.path.splitext(outfile)
new_name = base+str(buildNumberItalic) +ext

shutil.copy(old_name, new_name)


print ("DONE!")