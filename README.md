# Amstelvar

### About the Design

Amstelvar is a typeface inspired by the typeface designs used in The Netherlands and Belgium from the sixteenth century to the development of Times Roman in the 1930s.

It is the first public demonstration of the Type Network "Parametric Axes" approach to the OpenType Variable Fonts technology.
Read more about this axis system at [variationsguide.typenetwork.com](https://variationsguide.typenetwork.com), and [petrvanblokland.github.io/VariationsGuide](https://petrvanblokland.github.io/VariationsGuide)

The font is licensed under the SIL Open Font License, which permits unrestricted usage, distribution, and modification, subject to terms in the license. 

### Specification

The first release of "Amstelvar Alpha" was in early 2017. 
In 2018 the project scope expanded to a "1.0"-level release with a Roman redrawn for highest quality, a new Italic, and wider language support with the [Google Latin Plus (600)](https://github.com/TypeNetwork/Amstelvar/blob/master/Character%20Set) glyph set.
The variable axis work includes:

* Reform registered axes (opsz, wght, wdth)
* xopq and yopq will be adjusted, along the opsz axes
* Test to triovars and edit extrema
  * A monovar = opsz min (regular weight, regular width)
  * A duovar = opsz min + wght min
  * A triovar = opsz min + wght min + wdth min

#### Axes

* wght, wdth, opsz, GRAD, ital
* XTRA, YTRA, XOPQ, YOPQ
* YTLC, YTUC, YTFG, YTAS, YTDE
* YTOS, YTUS, YTAD, YTDD, XTAB, YTSE, VUID, VOTF, YTCH, XTCH, POPS, PWTH, PWHT, UDLN
