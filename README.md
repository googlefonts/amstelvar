# Amstelvar

### About the Design

Amstelvar is a typeface inspired by the typeface designs used in The Netherlands and Belgium from the sixteenth century to the development of Times Roman in the 1930s.

It was the first public demonstration of the Type Network "Parametric Axes" approach to the OpenType Variable Fonts technology.
Read more about how to use this axis system for better typography at [variablefonts.typenetwork.com](https://variablefonts.typenetwork.com).

The font is licensed under the [SIL Open Font License](OFL.txt), which permits unrestricted usage, distribution, and modification, subject to terms in the license. 

### Specification

The first release of "Amstelvar Alpha" was in early 2017. 
In 2018 the project scope expanded to a "1.0"-level release with a Roman redrawn for highest quality, a new Italic, and wider language support with the [Google Latin Plus](https://github.com/googlefonts/gftools/tree/master/Lib/gftools/encodings/GF%20Glyph%20Sets) glyph set (around 600 total: 567 main glyphs + 25 optional + build glyphs).

The variable axis work includes:

1. Reform registered axes (wght, wdth) to idealize them for the default optical size (14 pt)
2. Extend the registered axes for a full range of opsz (8 to 144 pt)
3. Create other blended axis (GRAD)
4. Create the "primary parametric" axes (XTRA,  XOPQ, YOPQ), limited to minor adjustments
5. Create the "Y Transparency bundle" of alignments (YTLC, YTUC, YTFG, YTAS, YTDE, and then YTRA)
6. Create (and define as needed) all the "secondary parametric" axes

#### Axes

* User axes: wght, wdth, opsz, GRAD, ital
* Primary parametric axes: XTRA, YTRA, XOPQ, YOPQ
* Y Tranparency Bundle: YTLC, YTUC, YTFG, YTAS, YTDE
* Secondary parametric axes: YTOS, YTUS, YTAD, YTDD, XTAB, YTSE, VUID, VOTF, YTCH, XTCH, POPS, PWTH, PWHT, UDLN

### Design Progress notes

Feb. 21, 2019

Font Bureau recieved approval of Default roman, opsz min and max, and Default ital opsz min and max, for ASCII

March 8, 2019

Font Bureau's Santiago Orozco started compeltion of glyph repertoires for spec.

March 15, 2019 

Font Bureau's Santiago Orozco completed `Amstelvar-Roman.ufo` according to `CharacterSet.txt`

March 18, 2019 

TypNetwork takes opsz max and min, regular and italics, and Italic default for charset update

April 10, 2019 

Within `Amstelvar/Docs` there is a [AMSTELVAR DESIGNSPACE MAP2.pdf](https://github.com/TypeNetwork/Amstelvar/blob/master/docs/AMSTELVAR%20DESIGNSPACE%20MAP%202.pdf) file with notes on overall design space, and progress display on contols milestone.

[Amstelvar Artboard 2.pdf](https://github.com/TypeNetwork/Amstelvar/blob/master/docs/Amstelvar%20Artboard%202.pdf) shows entire complete glyphs, link to measurement and glyphs [sheet](https://docs.google.com/spreadsheets/d/1EZ6nu8wDf1q3_F4Rabbn0bBvpqG41On4LcoBH0Y8EEI) that contains measured values and other data forvariable font creation. 
