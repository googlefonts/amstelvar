import os
import subprocess
import shutil
import random
from drawbotlab.vfont import VFInstance
from drawbotlab.math import lerp, norm

base = os.path.split(os.path.split(__file__)[0])[0]
srcPath = os.path.join(base, 'fonts/Amstelvar-Roman-VF.ttf')

txt = '''AÀÁÂÃÄÅĀĂĄǺȀȂẠẢẤẦẨẪẬẮẰẲẴẶBCÇĆĈĊČDĎEÈÉÊËĒĔĖĘĚȄȆẸẺẼẾỀỂỄỆFGĜĞĠĢǦHĤIÌÍÎÏĨĪĬĮİȈȊỈỊJĴKĶLĹĻĽMNÑŃŅŇOÒÓÔÕÖŌŎŐƠǪȌȎȪȬȰỌỎỐỒỔỖỘỚỜỞỠỢPQRŔŖŘȐȒSŚŜŞŠȘTŢŤȚUÙÚÛÜŨŪŬŮŰŲƯȔȖỤỦỨỪỬỮỰVWŴẀẂẄXYÝŶŸȲỲỴỶỸZŹŻŽÆǼÐØǾÞĐĦĿŁŊŒŦƏẞµaàáâãäåāăąǻȁȃạảấầẩẫậắằẳẵặbcçćĉċčdďeèéêëēĕėęěȅȇẹẻẽếềểễệfgĝğġģǧhĥiìíîïĩīĭįȉȋỉịjĵkķlĺļľmnñńņňoòóôõöōŏőơǫȍȏȫȭȱọỏốồổỗộớờởỡợpqrŕŗřȑȓsśŝşšștţťțuùúûüũūŭůűųưȕȗụủứừửữựvwŵẁẃẅxyýÿŷȳỳỵỷỹzźżžßæǽðøǿþđħıĸŀłŋœŧȷəʹʺʼªº0123456789¹²³¼½¾⁴_-‐–—―()[]{}⟨⟩#%‰'"‘’“”‚„‹›«»*†‡.,:;…!¡?¿//\⁄|¦@&§¶№·•′″+−±÷×=<>≤≥≈≠¬⁒∕∙$¢£¤¥₡₣₤₦₧₩₫€ƒ₭₱₲₵₹₺₼₽^~´`˝ˆ¸˛©®™°'''


transitions = [
    (
     {
    'opsz': 12,
    'XOPQ': 62,
    'XTRA': 402,
    'YOPQ': 62,
    'YTLC': 500,
    'YTUC': 750,
    'YTFG': 750,
    'YTDE': -240,
    'YTAS': 750,
    'YTSE': 18,
    'PWHT': 62,
    'PWTH': 462
    },
    {
    'opsz': 12,
    'XOPQ': 31,
    'XTRA': 402,
    'YOPQ': 62,
    'YTLC': 500,
    'YTUC': 750,
    'YTFG': 750,
    'YTDE': -240,
    'YTAS': 750,
    'YTSE': 18,
    'PWHT': 62,
    'PWTH': 462
    },
    (0, 0, 0),
    (0, 0, 0)
    ),
    
    ########
    
    (
     {
    'opsz': 12,
    'XOPQ': 31,
    'XTRA': 402,
    'YOPQ': 62,
    'YTLC': 500,
    'YTUC': 750,
    'YTFG': 750,
    'YTDE': -240,
    'YTAS': 750,
    'YTSE': 18,
    'PWHT': 62,
    'PWTH': 462
    },
    {
    'opsz': 12,
    'XOPQ': 62,
    'XTRA': 402,
    'YOPQ': 62,
    'YTLC': 500,
    'YTUC': 750,
    'YTFG': 750,
    'YTDE': -240,
    'YTAS': 750,
    'YTSE': 18,
    'PWHT': 62,
    'PWTH': 462
    },
    (0, 0, 0),
    (0, 0, 0)
    ),
    
    ########
    
    (
     {
    'opsz': 12,
    'XOPQ': 62,
    'XTRA': 402,
    'YOPQ': 62,
    'YTLC': 500,
    'YTUC': 750,
    'YTFG': 750,
    'YTDE': -240,
    'YTAS': 750,
    'YTSE': 18,
    'PWHT': 62,
    'PWTH': 462
    },
    {
    'opsz': 12,
    'XOPQ': 179,
    'XTRA': 402,
    'YOPQ': 62,
    'YTLC': 500,
    'YTUC': 750,
    'YTFG': 750,
    'YTDE': -240,
    'YTAS': 750,
    'YTSE': 18,
    'PWHT': 62,
    'PWTH': 462
    },
    (0, 0, 0),
    (0, 0, 0)
    ),
    
    
    ]


# frame per seconds
fps = 60
# duration of the movie
seconds = 3
# calculate the lenght of a single frame
duration = 1 / fps
# calculate the amount of frames needed
totalFrames = seconds * fps



for transition in transitions:
    locationMin, locationMax, colorMin, colorMax = transition
    for i in range(fps+1):
        progress = lerp(0, fps, i)
        print progress,
        thisLocation = {}
        for axis in locationMin.keys():
            try:
                thisLocation[axis] = norm(progress, locationMin.get(axis) or 0, locationMax.get(axis) or 0)
            except:
                thisLocation[axis] = 0
        #print thisLocation
        vfi = VFInstance(srcPath, thisLocation)

        thisColorR = norm(progress, colorMin[0], colorMax[0])
        thisColorG = norm(progress, colorMin[1], colorMax[1])
        thisColorB = norm(progress, colorMin[2], colorMax[2])

        letterColorR = norm(progress, colorMax[0], colorMin[0])
        letterColorG = norm(progress, colorMax[1], colorMin[1])
        letterColorB = norm(progress, colorMax[2], colorMin[2])
     
        newPage(1000, 1000)
        frameDuration(.1)
    
        #fill(thisColorR, thisColorG, thisColorB)
        #rect(0, 0, width(), height())

        #fill(letterColorR, letterColorG, letterColorB)

        installFont(vfi.getPath())
        fontSize(24)
        tracking(5)
        font(vfi.getName())
        textBox(txt, (100, 100, 800, 800), align="left")
        uninstallFont(vfi.getPath())
        
        vfi.remove()



saveImage(os.path.join(base, 'AmstelvarAnimation-XOPQ.mov'))



for axis, data in listFontVariations().items():
    print((axis, data))
    
