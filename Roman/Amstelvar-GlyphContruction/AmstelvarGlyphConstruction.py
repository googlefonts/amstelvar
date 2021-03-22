

font = CurrentFont()

for glyph in font.glyphOrder:
    rglyph = font[glyph]
    if len(rglyph.components) > 0:
        glyphContruction = ""
        count = 1
        for comp in rglyph.components:
            glyphContruction += comp.baseGlyph
            if count < len(rglyph.components):
                glyphContruction += str("+")
            count+=1
        print (rglyph.name + str("=") + glyphContruction + str("|") + hex(font[str(rglyph.name)].unicode))