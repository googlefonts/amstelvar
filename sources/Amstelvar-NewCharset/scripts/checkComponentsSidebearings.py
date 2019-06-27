glyph = CurrentGlyph()
print (glyph.name)
print (glyph.leftMargin)
print (glyph.rightMargin)
#print(glyph)

font = CurrentFont()

for g in font:
#    print(g.components)
    if len(g.components) != 0:
        for c in g.components:
            if c.baseGlyph == glyph.name:
                print (g.name)
                print (g.leftMargin)
                print (g.rightMargin)