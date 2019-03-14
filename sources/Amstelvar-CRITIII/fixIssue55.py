from defcon import Font

fonts = [
Font("Italic/Amstelvar-Italic-3.ufo"),
Font("Italic/Amstelvar-Italic-opsz-max.ufo"),
Font("Italic/Amstelvar-Italic-opsz-min.ufo"),
Font("Roman/Amstelvar-Roman-3.ufo"),
Font("Roman/Amstelvar-Roman-opsz-max.ufo"),
Font("Roman/Amstelvar-Roman-opsz-min.ufo"),
]

glyphNames = [
    "DZcaron",
    "Dzcaron",
    "dzcaron",
    "LJ",
    "Lj",
    "lj",
    "NJ",
    "Nj",
    "nj",
]

for font in fonts:
    for glyphName in glyphNames:
        
        if glyphName in font:
            del font[glyphName]
        
        font.newGlyph(glyphName)
        glyph = font[glyphName]
        print glyph.name
        a, b = glyphName[0], glyphName[1:]
        
        component1 = glyph.instantiateComponent()
        component1.baseGlyph = a
        component2 = glyph.instantiateComponent()
        component2.baseGlyph = b
        width1 = font[a].width
        width2 = font[b].width
        
        glyph.appendComponent(component1)
        component2.move((width1, 0))
        glyph.appendComponent(component2)
        glyph.width = width1+width2
        
    font.save()