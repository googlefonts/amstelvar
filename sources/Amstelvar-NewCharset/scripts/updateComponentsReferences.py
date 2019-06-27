
oldGlyphName = "grave"
newGlyphName = "gravecomb"


#print(glyph)"
font = CurrentFont()

for g in font:
#    print(g.components)
    if len(g.components) != 0:
        for c in g.components:
            if c.baseGlyph == oldGlyphName:
                c.baseGlyph = newGlyphName
                print("New name:" + g.name + c.baseGlyph)