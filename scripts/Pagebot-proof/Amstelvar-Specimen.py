# -----------------------------------------------------------------------------
#
#     P A G E B O T
#
#     Copyright (c) 2016+ Buro Petr van Blokland + Claudia Mens
#     www.pagebot.io
#     Licensed under MIT conditions
#
#     Supporting DrawBot, www.drawbot.com
#     Supporting Flat, xxyxyz.org/flat
# -----------------------------------------------------------------------------
#
#     ShowFontContent.py
#
#     Print the values of the specified font for naming, info and features
#     and generate a simple 1000 x 1000 PDF, showing part of the glyph set.
#     This is the simple demo version of the FontSpecimen.py that will generate 
#     a full specimen of the font.
#
import pagebot
from pagebot import getContext
from pagebot.fonttoolbox.fontpaths import getTestFontsPath
from pagebot.fonttoolbox.objects.font import findFont, Font
from pagebot.document import Document
from pagebot.style import *
from pagebot.elements import * # Import all types of page-child elements for convenience
from pagebot.toolbox.color import color
from pagebot.toolbox.units import em, p, pt, mm, inch, px
from pagebot.conditions import * # Import all conditions for convenience.
from pagebot.constants import *
from pagebot.fonttoolbox.variablefontbuilder import getVarFontInstance

c = getContext()
EXPORT_PATH = '_export/FontContent.pdf'

#Load Font
DEFAULT_FONT_PATH = 'fonts/'
FONT_PATH = DEFAULT_FONT_PATH + 'Amstelvar-Roman-VF.ttf'
FONT_PATH2= DEFAULT_FONT_PATH + 'Amstelvar-Italic-VF.ttf'

# Function to know if the fonts is loading
f = Font(FONT_PATH)
if f is None:
    print('%s cannot be found' % FONT_PATH)
else:
    print('Done')

f2 = Font(FONT_PATH2)
if f2 is None:
    print('%s cannot be found' % FONT_PATH2)
else:
    print('Done')

#Default Axes Descriptions
axesDescriptions = { 'wght': 'Weight', 'wdth': 'Width', 'opsz': 'Optical size',}

# Get the axis of the font that is loaded
for axisName, (minValue, defaultValue, maxValue) in f.axes.items():
    print(axisName, minValue, defaultValue, maxValue, axesDescriptions.get(axisName, 'unknown axis'))
for axisName, (minValue, defaultValue, maxValue) in f2.axes.items():
    print(axisName, minValue, defaultValue, maxValue, axesDescriptions.get(axisName, 'unknown axis'))

#ROMAN FONTS
MAXOPTICAL = getVarFontInstance(f.path, dict(opsz=144.0))
MINOPTICAL = getVarFontInstance(f.path, dict(opsz=8.0))
H2OPTICAL = getVarFontInstance(f.path, dict(opsz=100))
#ITALICFONTS
MAXOPTICALIT = getVarFontInstance(f2.path, dict(opsz=144.0))
MINOPTICALIT = getVarFontInstance(f2.path, dict(opsz=8.0))
H2OPTICALIT = getVarFontInstance(f2.path, dict(opsz=100))

#Function to make the docuemnt
def makeDocument():
    #Parameters of the docuemnt
    context = getContext()
    W, H = pt(1920, 1080)
    padheight = pt(70)
    padside = pt(466)
    PADDING = padheight, padside, padheight, padside
    G = mm(4)
    PW = W - 2*padside 
    PH = H - 2*padheight
    CW = (PW - (G*2))/3 
    CH = PH
    GRIDX = ((CW, G), (CW, 0))
    GRIDY = ((CH, 0),)

    # Function for the first column in the main page layout
    def firstColumnWaterfall(b, fontStyle):
        s = c.newString('', style=dict(font=f))
        CW2 = (PW - (G*2))/3 # Column width
        for n in range(4):
                s += c.newString( b + '\n', style=dict(font=fontStyle, fontSize=pt(12+n*1), leading=pt((12+n*1)+3) ))
        newTextBox(s ,parent=page, w=CW2, h=pt(700),font=f, pt=pt(160), nextElementName='e2',conditions=[Left2Left(),Top2Top(), Overflow2Next()])
        doc.solve()
    
    # Function for the second column in the main page layout
    def secondColumnWaterfall(b, fontStyle):
        s = c.newString('', style=dict(font=f))
        CW2 = (PW - (G*2))/3 # Column width
        for n in range(3):
                s += c.newString( b + '\n', style=dict(font=fontStyle, fontSize=pt(16+n*2), leading=pt((12+n*2)+6) ))
        newTextBox(s ,parent=page, w=CW2, h=pt(700),font=f, pt=pt(160), conditions=[Right2Right(),Top2Top()])
        doc.solve()

    # Function for the Waterfall layout
    def typeWaterfall(x, fontStyle, PageDescription):
        newTextBox(PageDescription, style=subtitle, w=PW, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        st = c.newString('', style=dict(font=f))
        for n in range(7):
            if n < 4:
                fontSize=144-n*24
                leading=(144-n*24)+24
            else:
                fontSize=108-n*12
                leading=None
            st += c.newString( x + '\n', style=dict(font=fontStyle, fontSize=fontSize, leading=leading))
        newTextBox(st ,parent=page, padding=pt(4), x=pt(60), y= pt(950), w=W, font=f,
                    cconditions=[Left2Left(), Top2Top(),  Overflow2Next()],
                    yAlign=TOP, xAlign=LEFT,)
        return doc 
        doc.solve()

    # Create a new document with 1 page. Set overall size and padding.
    doc = Document(w=W, h=H, padding=PADDING, gridX=GRIDX, gridY=GRIDY, context=context)
    view = doc.view
    page = doc[1]

    subtitle = dict(font=f, fontSize=pt(24), leading=pt(28))
    pagePaddings = (50, 50, 50, 50)

    # Page1
    # Function to make the main page layout 
    def mainPage(fontStyle1, fontStyle2):
        # New text box for the Title
        maintitle = context.newString("Amstelvar", style=dict(font=fontStyle1, xTextAlign=CENTER, fontSize=pt(96), leading=pt(115)))
        newTextBox(maintitle, w=PW, h=PH, parent=page, columnAlignY = TOP, xTextAlign=CENTER, conditions=(Center2Center(), Top2Top()))
        subtitle = dict(font=fontStyle2, fontSize=pt(24), leading=pt(28))
        newTextBox("Series by David Berlow", style=subtitle, pt = pt(100), w=PW, h=PH, parent=page, columnAlignY = BOTTOM, xTextAlign=CENTER, conditions=(Center2Center(), Bottom2Bottom()))
        # 3 columns
        heightCol = pt(700)
        textString = "ABCDEFG HIJKLMN OPQRSTU VWXYZ&! abcdefghij klmnopqrs tuvwxyzĸ¢ 1234567890"
        centertext = context.newString(textString, style=dict(font=fontStyle1, xTextAlign=CENTER, fontSize=pt(60), leading=pt(69)))
        CW2 = (PW - (G*2)) # Column width
        style3 = dict(font=f, fontSize=pt(60), leading=pt(69), hyphenation=None, prefix= None, postfix=None)
        newTextBox(centertext, style=style3, w=CW, h=heightCol, pt = pt(148), xTextAlign=CENTER, parent=page, conditions=[Center2Center(), Top2Top()])
        text4 = "Betreed de wereld van de invloedrijke familie Plantin en Moretus. Christophe Plantin bracht zijn leven door in boeken. Samen met zijn vrouw en vijf dochters woonde hij in een imposant pand aan de Vrijdagmarkt. Plantin en Jan Moretus hebben een indrukwekkende drukkerij opgebouwd. Tegenwoordig is dit het enige museum ter wereld dat ..."
        style4 = dict(font=fontStyle2, fontSize=pt(29), leading=pt(35))
        newTextBox(text4, style=style4, xTextAlign=JUSTIFIED, w=CW2, parent=page, conditions=[Left2Left(), Bottom2Bottom()])
        b = ("Hyni në botën e familjes me ndikim Plantin dhe Moretus. Christophe Plantin e kaloi jetën mes librave. Së bashku me gruan dhe pesë bijat e tij, ai jetonte në një pronë imponuese në Vrijdagmarkt. Plantin dhe Jan Moretus krijuan një biznes shtypës mbresëlënës. Sot, ky është muze i vetëm në botë që do të ... \n ")
        firstColumnWaterfall(b, fontStyle2)
        secondColumnWaterfall(b, fontStyle2)
        doc.solve()

    # Parameters of the function
    fontStyle1 = H2OPTICAL.path
    fontStyle2 = f.path
    mainPage(fontStyle1, fontStyle2)

    # Page2
    # Function to make the one column layout
    page = page.next
    def oneColumnPage(fontStyle, textString, PageDescription):
        astring = context.newString(textString, style=dict(font=fontStyle, xTextAlign=CENTER, fontSize=pt(144), leading=pt(163)))
        page.padding = pagePaddings
        padd= pt(100)
        PW2 = W - 2*padd
        newTextBox(astring, pt= pt(130), w=PW2, h=H, hyphenation=False, parent=page, conditions=(Center2Center(), Middle2Middle()))
        newTextBox(PageDescription, style=subtitle, w=PW, hyphenation=False, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        doc.solve()
    
    # Parameters of the function
    textString = "Aa Bb Cc Dd Ee Ff \nGg Hh Ii Jj Kk \nLl Mm Nn Oo Pp \nQq Rr Ss Tt Uu \nVv Ww Xx Yy Zz"
    PageDescription = "Opsz-max camelcase roman"
    fontStyle = MAXOPTICAL.path
    oneColumnPage(fontStyle, textString, PageDescription)

    # Page3
    page = page.next
    PageDescription = "Opsz-default camelcase roman"
    fontStyle = f.path
    oneColumnPage(fontStyle, textString, PageDescription)

    #Page4
    page = page.next
    PageDescription = "Opsz-min camelcase roman"
    fontStyle = MINOPTICAL.path
    oneColumnPage(fontStyle, textString, PageDescription)

    # Page 5
    #Function to make the 3 column layout
    page = page.next 
    def threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription):
        page.padding = pagePaddings
        CW3 = (W-120)/3 # Column width
        cstring = context.newString(textString, style=dict(font=fontStyle1, xTextAlign=CENTER, fontSize=pt(144), leading=pt(163)))
        dstring = context.newString(textString, style=dict(font=fontStyle2, xTextAlign=CENTER, fontSize=pt(144), leading=pt(163), hyphenation=None))
        spreads= dict(font=fontStyle3, fontSize=pt(144), leading=pt(163))
        newTextBox(cstring, w=(CW3+10), parent=page, conditions=[Left2Left(), Middle2Middle()])
        newTextBox(textString, style=spreads, w=CW3, xTextAlign=CENTER, parent=page, conditions=[Center2Center(), Middle2Middle()])
        newTextBox(dstring, w=CW3, parent=page, conditions=[Right2Right(), Middle2Middle()])
        newTextBox(PageDescription, style=subtitle, w=PW, h=PH, parent=page, columnAlignY = TOP, conditions=(Left2Left(), Top2Top()))
        doc.solve()

    # Parameters of the function
    textString = "ABCDE\nFGHIJK\nLMNOP\nQRSTU\nVWXYZ"
    PageDescription = "Opsz-min opsz-default opsz-max uppercase roman"
    fontStyle1 = MINOPTICAL.path
    fontStyle2 = MAXOPTICAL.path
    fontStyle3 = f.path
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription)

    # Page 6
    page = page.next 
    textString = 'abcde\nfghijk\nlmnop\nqrstu\nvwxyz'
    PageDescription = "Opsz-min opsz-default opsz-max lowercase roman"
    fontStyle1 = MINOPTICAL.path
    fontStyle2 = MAXOPTICAL.path
    fontStyle3 = f.path
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription)

    # Page 7
    page = page.next
    page.padding = pagePaddings
    x = 'ABCDEFGHIJKLMNOPQRST'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall uppercase roman'
    typeWaterfall(x, fontStyle, PageDescription)

    # Page 8
    page = page.next
    page.padding = pagePaddings
    x = 'abcdefghijklmnopqrstuvwxyz'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall lowercase roman'
    typeWaterfall(x, fontStyle, PageDescription)

    # Page 9
    page = page.next
    page.padding = pagePaddings
    x = '123456789!@#$%^&*()_+{}|:”<>?/.,’;\]['
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall numerals and punctuation roman'
    typeWaterfall(x, fontStyle, PageDescription)
    
    # Page 10
    page = page.next
    page.padding = pagePaddings
    x = '₡$€£₣₤₦₩₫₭₱₲₵₹₺₼₽'
    fontStyle = MAXOPTICAL.path
    PageDescription = 'Waterfall monetary'
    typeWaterfall(x, fontStyle, PageDescription)
    
    # Page 1 Italic
    page = page.next
    fontStyle1 = H2OPTICALIT.path
    fontStyle2 = f2.path
    mainPage(fontStyle1, fontStyle2)

    # Page 2 Italic
    page = page.next
    textString = "Aa Bb Cc Dd Ee Ff \nGg Hh Ii Jj Kk \nLl Mm Nn Oo Pp \nQq Rr Ss Tt Uu \nVv Ww Xx Yy Zz"
    PageDescription = "Opsz-max camelcase italic"
    fontStyle = MAXOPTICALIT.path
    oneColumnPage(fontStyle, textString, PageDescription)

    # Page 3 Italic
    page = page.next
    PageDescription = "Opsz-default camelcase italic"
    fontStyle = f2.path
    oneColumnPage(fontStyle, textString, PageDescription)

    # Page 4 Italic
    page = page.next
    PageDescription = "Opsz-min camelcase italic"
    fontStyle = MINOPTICALIT.path
    oneColumnPage(fontStyle, textString, PageDescription)

    # Page 5 Italic
    page = page.next
    textString = "ABCDE\nfFGHIJK\nfLMNOP\nfQRSTU\nfVWXYZ"
    PageDescription = "Opsz-min opsz-default opsz-max uppercase italic"
    fontStyle1 = MINOPTICALIT.path
    fontStyle2 = MAXOPTICALIT.path
    fontStyle3 = f2.path
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription)

    # Page 6 Italic
    page = page.next 
    textString = 'abcde\nfghijk\nlmnop\nqrstu\nvwxyz'
    PageDescription = "Opsz-min opsz-default opsz-max lowercase italic"
    fontStyle1 = MINOPTICALIT.path
    fontStyle2 = MAXOPTICALIT.path
    fontStyle3 = f2.path
    threeColumnPage(fontStyle1, fontStyle2, fontStyle3, textString, PageDescription)
    doc.solve()

    # Page 7 Italic
    page = page.next
    page.padding = pagePaddings
    x = 'ABCDEFGHIJKLMNOPQRST'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall uppercase italic'
    typeWaterfall(x, fontStyle, PageDescription)
    doc.solve()

    # Page 8 Italic
    page = page.next
    page.padding = pagePaddings
    x = 'abcdefghijklmnopqrstuvwxyz'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall lowercase italic'
    typeWaterfall(x, fontStyle, PageDescription)
    doc.solve()

    # Page 9 Italic
    page = page.next
    page.padding = pagePaddings
    x = '123456789!@#$%^&*()_+{}|:”<>?/.,’;\]['
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall numerals and punctuation roman'
    typeWaterfall(x, fontStyle, PageDescription)
    doc.solve()

    # Page 10 Italic
    page = page.next
    page.padding = pagePaddings
    x = '₡$€£₣₤₦₩₫₭₱₲₵₹₺₼₽'
    fontStyle = MAXOPTICALIT.path
    PageDescription = 'Waterfall monetary'
    typeWaterfall(x, fontStyle, PageDescription)
    
    page.solve()
    return doc

# Export the document to this PDF file.
doc = makeDocument()
doc.export('_export/Amstelvar-Specimen.pdf') 