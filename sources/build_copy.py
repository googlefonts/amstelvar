from fontmake.font_project import FontProject
from fontTools.varLib import build
import os
import shutil
from robofab.world import OpenFont

# Roman

romans = [
	"Roman/Amstelvar-Roman-3.ufo",
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
"Roman/Amstelvar-Roman-YTSE-min.ufo",
"Roman/Amstelvar-Roman-YTSE-max.ufo",
]

romans2 = []
base = os.path.split(__file__)[0]
temp = os.path.join(base, 'temp')
if not os.path.exists(temp):
    os.mkdir(temp)
    os.mkdir(os.path.join(temp, 'Roman'))
    
for i, roman in enumerate(romans):
    srcPath = os.path.join(base, roman)
    destPath = os.path.join(temp, roman)
    shutil.copytree(srcPath, destPath)
    if i == 0:
        src = OpenFont(destPath)
    else:
        f = OpenFont(destPath)
        for g in src:
            if g.name not in f or ( g.name in f and not f[g.name].contours and not f[g.name].components ):
                f.insertGlyph(g)
        f.save()
    romans2.append('temp/'+roman)

project = FontProject()
project.run_from_ufos(
	romans2, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Roman.designspace"
outfile = "../fonts/Amstelvar-Roman-VF.ttf"
finder = lambda s: s.replace("Roman/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"

shutil.rmtree(temp, ignore_errors=True)

"""
# Italic

italics = [
	"Italic/Amstelvar-Italic-3.ufo",
#	"Italic/Amstelvar-ital-opszmax.ufo",
]

project = FontProject()
project.run_from_ufos(
	italics, 
	output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
	remove_overlaps=False, 
	reverse_direction=False, 
	use_production_names=False)

designSpace = "Amstelvar-Italic.designspace"
outfile = "../fonts/Amstelvar-Italic-VF.ttf"
finder = lambda s: s.replace("Italic/", "master_ttf_interpolatable/").replace(".ufo", ".ttf")
varfont, _, _ = build(designSpace, finder)
print "Saving Variable Font..."
varfont.save(outfile)
print "DONE!"
"""