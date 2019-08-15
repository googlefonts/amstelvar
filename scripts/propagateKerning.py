from drawbotlab.math import lerp, norm
import os
# get point indexes from glyph
def getValueFromGlyphIndex(g, index):
    """
    Given a glyph and a point index, return that point.
    """
    index = int(index)
    i = 0
    for c in g:
        for p in c.points:
            if i == index:
                return (p.x, p.y)
            i += 1


paths = ['/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-36.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-84-wghtmin.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-84.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-max-wdthmin-wghtmax.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-max-wghtmin.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-max.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-opsz-min.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wdthmax.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wdthmin.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wghtmax.ufo', '/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman-wghtmin.ufo']

default = OpenFont('/Users/david/Desktop/workspace/FB/fb-Amstelvar/sources/Amstelvar-NewCharset/Roman/Amstelvar-Roman.ufo', showUI=False)
defaultXopqValue = getValueFromGlyphIndex(default['H'], 22)[0] - getValueFromGlyphIndex(default['H'], 11)[0]

print('default', defaultXopqValue)

for path in paths:
    f = OpenFont(path, showInterface=False)
    xopqValue = getValueFromGlyphIndex(f['H'], 22)[0] - getValueFromGlyphIndex(f['H'], 11)[0]
    m = xopqValue / defaultXopqValue
    print(os.path.split(path)[1], m, xopqValue)
    
    f.groups.clear()
    f.kerning.clear()
    for groupName, groupGlyphs in default.groups.items():
        f.groups[groupName] = groupGlyphs
    
    f.kerning.update(default.kerning.asDict())
    for pair in f.kerning:
        value = f.kerning[pair]
        f.kerning[pair] = int(round(value * m))
    f.save()
print('done')