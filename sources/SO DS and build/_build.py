from fontmake.font_project import FontProject
from fontTools.varLib import build

# Roman

romans = [
	"Roman/Amstelvar-Roman.ufo",
"Roman/Amstelvar-Roman-YTUC-min.ufo",
"Roman/Amstelvar-Roman-YTUC-max.ufo",
"Roman/Amstelvar-Roman-YTLC-min.ufo",
"Roman/Amstelvar-Roman-YTLC-max.ufo",
"Roman/Amstelvar-Roman-YTFG-min.ufo",
"Roman/Amstelvar-Roman-YTFG-max.ufo",
"Roman/Amstelvar-Roman-YTDE-min.ufo",
"Roman/Amstelvar-Roman-YTDE-max.ufo",
"Roman/Amstelvar-Roman-YTAS-min.ufo",
"Roman/Amstelvar-Roman-YTAS-max.ufo",
"Roman/Amstelvar-Roman-opsz-min.ufo",
"Roman/Amstelvar-Roman-opsz-max.ufo",
"Roman/Amstelvar-Roman-YTSE-max.ufo",
"Roman/Amstelvar-Roman-YTSE-min.ufo",
"Roman/Amstelvar-Roman-XOPQ-min.ufo",
"Roman/Amstelvar-Roman-XOPQ-max.ufo",
"Roman/Amstelvar-Roman-YOPQ-min.ufo",
"Roman/Amstelvar-Roman-YOPQ-max.ufo",
"Roman/Amstelvar-Roman-PWTH-min.ufo",
"Roman/Amstelvar-Roman-PWTH-max.ufo",
"Roman/Amstelvar-Roman-PWHT-min.ufo",
"Roman/Amstelvar-Roman-PWHT-max.ufo",
"Roman/Amstelvar-Roman-XTRA-min.ufo",
"Roman/Amstelvar-Roman-XTRA-max.ufo",

"Roman/Amstelvar-Roman-wdth-max.ufo",
"Roman/Amstelvar-Roman-wdth-min.ufo",
"Roman/Amstelvar-Roman-wght-max.ufo",
"Roman/Amstelvar-Roman-wght-min.ufo",

"Roman/Amstelvar-Roman-GRAD-max.ufo",
"Roman/Amstelvar-Roman-GRAD-min.ufo",

]

project = FontProject()
project.run_from_ufos(
	romans, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Roman-dbBlendedonly.designspace"
outfile = "../fonts/Amstelvar-Roman-VF.ttf"
finder = lambda s: s.replace("Roman/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"

# Italic

# italics = [
# 	"Italic/Amstelvar-Italic-3.ufo",
# 	"Italic/Amstelvar-Italic-opsz-max.ufo",
# 	"Italic/Amstelvar-Italic-opsz-min.ufo",
# ]
# 
# project = FontProject()
# project.run_from_ufos(
# 	italics, 
# 	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
# 	remove_overlaps=False, 
# 	reverse_direction=False, 
# 	use_production_names=False)
# 
# designSpace = "Amstelvar-Italic.designspace"
# outfile = "../fonts/Amstelvar-Italic-VF.ttf"
# finder = lambda s: s.replace("Italic/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
# varfont, _, _ = build(designSpace, finder)
# print "Saving Variable Font..."
# varfont.save(outfile)
# print "DONE!"
