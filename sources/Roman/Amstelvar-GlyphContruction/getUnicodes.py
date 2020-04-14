
font = CurrentFont()

with open("list.txt") as txt:
	glyphs = txt.read().splitlines()
	
	for g in glyphs:
	    
	    glyphname= str(g[0:g.index('=')])
	    
	    #print (glyphname)
	    
	    newConstructionRule = g[0:g.index('|')] + ' | ' + str(hex(font[glyphname].unicode))
	    
	    print(newConstructionRule)