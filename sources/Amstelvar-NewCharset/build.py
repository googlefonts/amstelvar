from fontmake.font_project import FontProject
from fontTools.varLib import build
import shutil
import os
import sys

# Roman

romans = [
	"Roman/Amstelvar-Roman.ufo",
	"Roman/Amstelvar-Roman-opsz-min.ufo",
	"Roman/Amstelvar-Roman-opsz-36.ufo",
	"Roman/Amstelvar-Roman-opsz-84.ufo",
	"Roman/Amstelvar-Roman-opsz-max.ufo",
	"Roman/Amstelvar-Roman-wdthmax.ufo",
	"Roman/Amstelvar-Roman-wdthmin.ufo",
	"Roman/Amstelvar-Roman-wghtmin.ufo",
	"Roman/Amstelvar-Roman-wghtmax.ufo",
	
	"Roman/Amstelvar-Roman-XOPQmax.ufo",
	"Roman/Amstelvar-Roman-XOPQmin.ufo",
	"Roman/Amstelvar-Roman-XTRAmax.ufo",
	"Roman/Amstelvar-Roman-XTRAmin.ufo",
	"Roman/Amstelvar-Roman-YOPQmax.ufo",
	"Roman/Amstelvar-Roman-YOPQmin.ufo",
	
	#"Roman/Amstelvar-Roman-opsz-max-wgthmin.ufo",
	#"Roman/Amstelvar-Roman-opsz-max-wgthmax.ufo",

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


project = FontProject()
project.run_from_ufos(
	romans, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Roman-005.designspace"
outfile = "../../fonts/Amstelvar-Roman-VF.ttf"
finder = lambda s: s.replace("Roman/", "master_ttf/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print ("Saving Variable Font...")
varfont.save(outfile)
print ("DONE!")

# Italic


italics = [
	"Italic/Amstelvar-Italic.ufo",
	"Italic/Amstelvar-Italic-opsz-min.ufo",
	"Italic/Amstelvar-Italic-opsz-max.ufo",
	"Italic/Amstelvar-Italic-wdthmax.ufo",
	"Italic/Amstelvar-Italic-wdthmin.ufo",
	"Italic/Amstelvar-Italic-wghtmin.ufo",
	"Italic/Amstelvar-Italic-wghtmax.ufo",

]

project = FontProject()
project.run_from_ufos(
	italics, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Italic-001.designspace"
outfile = "../../fonts/Amstelvar-Italic-VF.ttf"
finder = lambda s: s.replace("Italic/", "master_ttf/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print ("Saving Variable Font...")
varfont.save(outfile)
print ("DONE!")

