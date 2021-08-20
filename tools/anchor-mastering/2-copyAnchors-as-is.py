# get source and destination fonts
srcFont = AllFonts()[1]
dstFont = CurrentFont()

# iterate over selected glyphs in the source font

selectedGlyphsUC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'AE', 'Oslash']

selectedGlyphslc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'idotless', 'jdotless', 'ae', 'oslash']

#selectedGlyphsAccents = ['brevecomb', 'acutecomb', 'tildecomb', 'dblgravecomb', 'macroncomb', 'dotaccentcomb', 'horncomb', 'dieresiscomb', 'ringcomb', 'circumflexcomb', 'breveinvertedcomb', 'gravecomb', 'caroncomb', 'hookabovecomb', 'hungarumlautcomb', 'breveacutecomb', 'circumflexgravecomb', 'circumflexhookabovecomb', 'circumflextildecomb', 'brevehookabovecomb', 'circumflexacutecomb', 'brevetildecomb', 'brevegravecomb', 'circumflexacutecomb.case', 'brevehookabovecomb.case', 'circumflextildecomb.case', 'brevegravecomb.case', 'circumflexhookabovecomb.case', 'breveacutecomb.case', 'circumflexgravecomb.case', 'brevetildecomb.case', 'breve.cyr', 'breve.cyr.case', 'gravecomb.case', 'acutecomb.case', 'circumflexcomb.case', 'tildecomb.case', 'macroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'dieresiscomb.case', 'hookabovecomb.case', 'ringcomb.case', 'hungarumlautcomb.case', 'caroncomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'cedillacomb.case', 'ogonekcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'dotbelowcomb', 'dieresisbelowcomb', 'commaaccentcomb', 'cedillacomb', 'ogonekcomb', 'brevebelowcomb', 'macronbelowcomb', 'caroncomb.alt', 'acutecombstack.case', 'brevecombstack.case', 'circumflexcombstack.case', 'dieresiscombstack.case', 'dotaccentcombstack.case', 'gravecombstack.case', 'hookabovecombstack.case', 'macroncombstack.case', 'tildecombstack.case'  ]

selectedGlyphsAccentsUC = ['circumflexacutecomb.case', 'brevehookabovecomb.case', 'circumflextildecomb.case', 'brevegravecomb.case', 'circumflexhookabovecomb.case', 'breveacutecomb.case', 'circumflexgravecomb.case', 'brevetildecomb.case', 'breve.cyr.case', 'gravecomb.case', 'acutecomb.case', 'circumflexcomb.case', 'tildecomb.case', 'macroncomb.case', 'brevecomb.case', 'dotaccentcomb.case', 'dieresiscomb.case', 'hookabovecomb.case', 'ringcomb.case', 'hungarumlautcomb.case', 'caroncomb.case', 'breveinvertedcomb.case', 'dblgravecomb.case', 'horncomb.case', 'dotbelowcomb.case', 'dieresisbelowcomb.case', 'commaaccentcomb.case', 'cedillacomb.case', 'ogonekcomb.case', 'brevebelowcomb.case', 'macronbelowcomb.case', 'acutecombstack.case', 'brevecombstack.case', 'circumflexcombstack.case', 'dieresiscombstack.case', 'dotaccentcombstack.case', 'gravecombstack.case', 'hookabovecombstack.case', 'macroncombstack.case', 'tildecombstack.case'  ]

selectedGlyphsAccentslc = ['brevecomb', 'acutecomb', 'tildecomb', 'dblgravecomb', 'macroncomb', 'dotaccentcomb', 'horncomb', 'dieresiscomb', 'ringcomb', 'circumflexcomb', 'breveinvertedcomb', 'gravecomb', 'caroncomb', 'hookabovecomb', 'hungarumlautcomb', 'breveacutecomb', 'circumflexgravecomb', 'circumflexhookabovecomb', 'circumflextildecomb', 'brevehookabovecomb', 'circumflexacutecomb', 'brevetildecomb', 'brevegravecomb', 'breve.cyr', 'dotbelowcomb', 'dieresisbelowcomb', 'commaaccentcomb', 'cedillacomb', 'ogonekcomb', 'brevebelowcomb', 'macronbelowcomb', 'caroncomb.alt' ]


def copyAnchors(selectedGlyphs, yPositioning):

    for glyph in selectedGlyphs:
    
        # get the source glyph
        srcGlyph = srcFont[glyph]
        
        # if the glyph doesn't have any anchors, skip it
        if not len(srcGlyph.anchors):
            continue
            
        print( srcFont[glyph].name )
    
        # get the source glyph
        srcGlyph = srcFont[glyph]

        # if the glyph doesn't have any anchors, skip it
        if not len(srcGlyph.anchors):
            continue

        # get the destination glyph
        dstGlyph = dstFont[glyph]
    
        print( srcFont[glyph].anchors )
    
        dstGlyph.clearAnchors()
        # iterate over all anchors in the source glyph
        for anchor in srcGlyph.anchors:
            # copy anchor to destination glyph
            dstGlyph.appendAnchor(anchor.name, (anchor.x, anchor.y))
            
# Copy UC anchors
copyAnchors(selectedGlyphsUC, dstFont.info.capHeight)

# Copy lc anchors
copyAnchors(selectedGlyphslc, dstFont.info.xHeight)

# Copy UC anchors
copyAnchors(selectedGlyphsAccentsUC, dstFont.info.capHeight)

# Copy lc anchors
copyAnchors(selectedGlyphsAccentslc, dstFont.info.xHeight)


print('Done!')
