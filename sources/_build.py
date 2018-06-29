from fontmake.font_project import FontProject
from fontTools.varLib import build
from fontTools.ttLib import TTFont
import os
import shutil
from fontParts.world import OpenFont

# options
addMissingGlyphsFromDefault = True
buildSlugs = True

slugs = {
    'uni01C7': (['L', 'J'], 455),
    'uni01C8': (['L', 'j'], 456),
    'uni01C9': (['l', 'j'], 457),
    'uni01CA': (['N', 'J'], 458),
    'uni01CB': (['N', 'j'], 459),
    'uni01CC': (['n', 'j'], 460),
    'uni01C4': (['D', 'Zcaron'], 452),
    'uni01C5': (['D', 'zcaron'], 453),
    'uni01C6': (['d', 'zcaron'], 454),
    }
 
spaces = [
    (
        "Amstelvar-Roman.designspace", # designspace 
        [   # masters
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
            "Roman/Amstelvar-Roman-YTSE-min.ufo",
            "Roman/Amstelvar-Roman-YTSE-max.ufo",
            "Roman/Amstelvar-Roman-XOPQ-min.ufo",
            "Roman/Amstelvar-Roman-XOPQ-max.ufo",
            "Roman/Amstelvar-Roman-YOPQ-min.ufo",
            "Roman/Amstelvar-Roman-YOPQ-max.ufo",
            "Roman/Amstelvar-XTRA-max.ufo",
            "Roman/Amstelvar-XTRA-min.ufo",

        ],
        "../fonts/Amstelvar-Roman-VF.ttf", # outfile
        "Roman/", # pathreplace
    ),
    (
        "Amstelvar-Italic.designspace", # designspace 
        [   # masters
            "Italic/Amstelvar-Italic-opsz-min.ufo",
            "Italic/Amstelvar-Italic-opsz-max.ufo",
            "Italic/Amstelvar-Italic-3.ufo"
        ],
        "../fonts/Amstelvar-Italic-VF.ttf", # outfile
        "Italic/", # pathreplace
    )
]


def setSlug(f, gname, components, kerning=True, decompose=False, clear=True):
    '''
    Generates composite
    '''
    if gname not in f:
        g = f.newGlyph(gname)
    if clear:
        f[gname].clear()

    left = f[components[0]].leftMargin
    right = f[components[-1]].rightMargin
    tick = 0
    xoffset = 0
    for component in components:
        if f.has_key(component):
            xoffset = xoffset
            kern = 0
            if (tick+1) < len(components) and kerning is True:
                nextComponent = components[tick+1]
                if f.kerning.has_key((component,nextComponent)):
                    kern = f.kerning[(component,nextComponent)]
            f[gname].appendComponent(component,(xoffset,0))
            xoffset = xoffset + f[component].width + kern
        else:
            print 'Skipping component', component, 'in', TX.font2Name(f) +'. Glyph does not exist.'
        tick = tick + 1
    # set sidebearings
    f[gname].leftMargin = left
    f[gname].rightMargin = right
    if decompose:
        f[gname].decompose()


for space in spaces:

    designSpace, masters, outfile, pathReplace = space

    if addMissingGlyphsFromDefault or buildSlugs:
        masters2 = []
        base = os.path.split(__file__)[0]
        temp = os.path.join(base, 'temp')
        if os.path.exists(temp):
            shutil.rmtree(temp, ignore_errors=True)
        if not os.path.exists(temp):
            os.mkdir(temp)
            os.mkdir(os.path.join(temp, pathReplace))
    
        for i, master in enumerate(masters):
            srcPath = os.path.join(base, master)
            destPath = os.path.join(temp, master)
            shutil.copytree(srcPath, destPath)
            if i == 0:
                f = OpenFont(destPath)
                src = OpenFont(destPath)
            else:
                f = OpenFont(destPath)
            
            if buildSlugs:   
                print "Building slugs..."                    
                for slug in slugs.items():
                    slugName, slugInfo = slug
                    slugComponents, slugUnicode = slugInfo
                    setSlug(f, slugName, slugComponents)
                    f[slugName].unicodes = [slugUnicode]
            
            if i != 0 and addMissingGlyphsFromDefault:
                print "Adding missing glyphs in sources from default..."                    
                for gname in src.keys():
                    g = src[gname]

                    if g.name not in f or ( g.name in f and not f[g.name].contours and not f[g.name].components ):
                        f.insertGlyph(g, name=g.name)


            
        
            f.save()
            masters2.append('temp/'+master)
    else:
        masters2 = masters
    print masters2

    project = FontProject()
    project.run_from_ufos(
        masters2, 
        output=("ttf-interpolatable"), # FIXME this also build master_ttf and should not.
        remove_overlaps=False, 
        reverse_direction=False, 
        use_production_names=False)

    finder = lambda s: s.replace(pathReplace, "master_ttf_interpolatable/").replace(".ufo", ".ttf")
    varfont, _, _ = build(designSpace, finder)
    print "Saving Variable Font..."
    varfont.save(outfile)

    print 'Adding avar table...'
    f= TTFont(outfile)
    f.importXML(os.path.join(os.path.split(__file__)[0], 'avar.ttx'))
    os.remove(outfile)
    f.save(outfile)

    print "DONE!"

    shutil.rmtree(temp, ignore_errors=True)




