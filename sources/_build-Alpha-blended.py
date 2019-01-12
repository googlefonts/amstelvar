from fontmake.font_project import FontProject
from fontTools.varLib import build

# Roman

romans = [
	"Alpha/AmstelvarAlphaBlended-Default.ufo",
"Alpha/AmstelvarAlphaBlended-OpticalSizeMin.ufo",
"Alpha/AmstelvarAlphaBlended-OpticalSizeMax.ufo",

"Alpha/AmstelvarAlphaBlended-WidthMin.ufo",

"Alpha/AmstelvarAlphaBlended-WeightMax.ufo",
"Alpha/AmstelvarAlphaBlended-WeightMin.ufo",

"Alpha/AmstelvarAlphaBlended-GradeMax.ufo",
"Alpha/AmstelvarAlphaBlended-GradeMin.ufo",

"Alpha/AmstelvarAlphaBlended-ParaWeightMax.ufo",
"Alpha/AmstelvarAlphaBlended-ParaWeightMin.ufo",

"Alpha/AmstelvarAlphaBlended-ParaWidthMin.ufo",

]

project = FontProject()
project.run_from_ufos(
	romans, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Alpha-blended.designspace"
outfile = "../fonts/AmstelvarAlphaBlended-VF.ttf"
finder = lambda s: s.replace("Alpha/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
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
