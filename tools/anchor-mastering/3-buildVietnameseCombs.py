from glyphConstruction import ParseGlyphConstructionListFromString, GlyphConstructionBuilder

# define glyph constructions
txt = '''\
brevetildecomb=brevecomb+tildecomb@top
brevehookabovecomb=brevecomb+hookabovecomb@center,110%
brevegravecomb=brevecomb+gravecomb@40%,110%
breveacutecomb=brevecomb+acutecomb@60%,110%
circumflexhookabovecomb=circumflexcomb+hookabovecomb@90%
circumflexacutecomb=circumflexcomb+acutecomb@90%
circumflexgravecomb=circumflexcomb+gravecomb@90%
circumflextildecomb=circumflexcomb+tildecomb@center,130%
brevetildecomb.case=brevecombstack.case+tildecombstack.case@top
brevehookabovecomb.case=brevecombstack.case+hookabovecombstack.case@center,110%
brevegravecomb.case=brevecombstack.case+gravecombstack.case@40%,110%
breveacutecomb.case=brevecombstack.case+acutecombstack.case@60%,110%
circumflexhookabovecomb.case=circumflexcombstack.case+hookabovecombstack.case@90%
circumflexacutecomb.case=circumflexcombstack.case+acutecombstack.case@90%
circumflexgravecomb.case=circumflexcombstack.case+gravecombstack.case@90%
circumflextildecomb.case=circumflexcombstack.case+tildecombstack.case@center,130%
'''

# get constructions from text
constructions = ParseGlyphConstructionListFromString(txt)

font = CurrentFont()

for construction in constructions:

    
    # build a construction glyph
    constructionGlyph = GlyphConstructionBuilder(construction, font)
    
    print (construction)

    # if the construction for this glyph was preceded by `?`
    # and the glyph already exists in the font, skip it
    
    #if constructionGlyph.name in font:
    #    continue

    # get the destination glyph in the font
    glyph = font.newGlyph(constructionGlyph.name)
    
    glyph.clear(anchors=False)
    
    # draw the construction glyph into the destination glyph
    constructionGlyph.draw(glyph.getPen())

    # copy construction glyph attributes to the destination glyph
    glyph.name = constructionGlyph.name
    glyph.unicode = constructionGlyph.unicode
    glyph.width = constructionGlyph.width
    #glyph.markColor = 1, 1, 0, 0.5
    glyph.decompose()

    # if no unicode was given, try to set it automatically
    #if glyph.unicode is None:
    #    glyph.autoUnicodes()
    
    