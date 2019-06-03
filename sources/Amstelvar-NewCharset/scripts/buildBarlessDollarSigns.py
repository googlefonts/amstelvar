for f in AllFonts():
    f.insertGlyph(f['dollar'], 'dollar.rvrn')
    g = f['dollar.rvrn']
    g.unicodes = []
    pt1 = g.contours[1].bPoints[3]
    pt2 = g.contours[1].bPoints[4]
    srcY = g.contours[1].bPoints[1].anchor[1] + 1
    yoffset1 = pt1.anchor[1] - srcY
    yoffset2 = pt2.anchor[1] - srcY
    pt1.move((0, -yoffset1 ))
    pt2.move((0, -yoffset2 ))
    pt1 = g.contours[2].bPoints[4]
    pt2 = g.contours[2].bPoints[5]
    srcY = g.contours[2].bPoints[2].anchor[1] - 1
    yoffset1 = pt1.anchor[1] - srcY
    yoffset2 = pt2.anchor[1] - srcY
    pt1.move((0, -yoffset1 ))
    pt2.move((0, -yoffset2 ))
    f.save()
    f.close()