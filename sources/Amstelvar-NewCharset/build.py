from fontmake.font_project import FontProject
from fontTools.varLib import build

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
	
	"Roman/Amstelvar-Roman-opsz-max-wgthmin.ufo",
	"Roman/Amstelvar-Roman-opsz-max-wgthmax.ufo",
	"Roman/Amstelvar-Roman-opsz-max-wgthmax-wdthmax.ufo",
	"Roman/Amstelvar-Roman-opsz-max-wgthmax-wdthmin.ufo",

]

project = FontProject()
project.run_from_ufos(
	romans, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Roman-003.designspace"
outfile = "../../fonts/Amstelvar-Roman-VF.ttf"
finder = lambda s: s.replace("Roman/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"

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
finder = lambda s: s.replace("Italic/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"
