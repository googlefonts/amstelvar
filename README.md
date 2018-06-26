# Amstelvar

### About the Design

Amstelvar is a typeface in the style used in The Netherlands and Belgium from the sixteenth century to the development of Times Roman in the 1930s.
It is the first public demonstration of the Type Network "Parametric Axes" approach to the OpenType Variable Fonts technology.
Read more about this axis system at [variationsguide.typenetwork.com](https://variationsguide.typenetwork.com), and [petrvanblokland.github.io/VariationsGuide](https://petrvanblokland.github.io/VariationsGuide)

The font is licensed under the SIL Open Font License, which permits unrestricted usage, distribution, and modification, subject to terms in the license. 

### Specification

In early 2017 the project scope expanded from the "Amstelvar Alpha" release of early 2017 for a "2.0"-level release in mid 2018:

* Redraw for highest quality
* Extend language support, with [Latin Plus (600)](https://github.com/TypeNetwork/Amstelvar/blob/master/Character%20Set) character set
* Add true italics

Axis work:

* Reform registered axes (opsz, wght, wdth)
* xopq and yopq will be adjusted, along the opsz axes
* Test to triovars and edit extrema
  * A monovar = opsz min (regular weight, regular width)
  * A duovar = opsz min + wght min
  * A triovar = opsz min + wght min + wdth min

#### Schedule

* February 1, 2018 Alpha
* April 1, 2018 Beta
* July 1, 2018 Final

#### Axes

* wght, wdth, opsz, GRAD, ital
* XTRA, YTRA, XOPQ, YOPQ
* YTLC, YTUC, YTFG, YTAS, YTDE
* YTOS, YTUS, YTAD, YTDD, XTAB, YTSE, VUID, VOTF, YTCH, XTCH, POPS, PWTH, PWHT, UDLN
