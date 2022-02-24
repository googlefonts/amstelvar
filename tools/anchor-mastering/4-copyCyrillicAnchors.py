srcFont = CurrentFont()

# iterate over selected glyphs in the source font

selectedGlyphsUC = { 'A':'Acyr', 'E':'Ie', 'K':'Ka' }
selectedGlyphslc = { 'a':'acyr', 'e':'ie', 'o':'ocyr', 'y':'ucyr' }

def copyAnchors(selectedGlyphs):

    for src, dst in selectedGlyphs.items():
    
        # get the source glyph
        srcGlyph = srcFont[src]
        
        # if the glyph doesn't have any anchors, skip it
        if not len(srcGlyph.anchors):
            continue
            
        print( srcFont[src].name )

        # if the glyph doesn't have any anchors, skip it
        if not len(srcGlyph.anchors):
            continue

        # get the destination glyph
        dstGlyph = srcFont[dst]
        
        dstGlyph.clearAnchors()
        
        #print( srcFont[src].anchors )
        
        # iterate over all anchors in the source glyph
        for anchor in srcGlyph.anchors:
            print( anchor )
            # copy anchor to destination glyph
            if anchor.name == 'top' or anchor.name == 'bottom':
                dstGlyph.appendAnchor(anchor.name, (anchor.x, anchor.y))
            
# Copy UC anchors
#copyAnchors(selectedGlyphsUC, dstFont.info.capHeight)

# Copy lc anchors
#copyAnchors(selectedGlyphslc, dstFont.info.xHeight)

# Copy UC anchors
#copyAnchors(selectedGlyphsAccentsUC, dstFont.info.capHeight)

# Copy lc anchors
#copyAnchors(selectedGlyphsAccentslc, dstFont.info.xHeight)

# Copy UC anchors
copyAnchors(selectedGlyphsUC)

# Copy lc anchors
copyAnchors(selectedGlyphslc)

print('Done!')
