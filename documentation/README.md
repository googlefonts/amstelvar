# Amstelvar Documentation

## I. Introduction

### Overview

AmstelvarAlpha-Variations.ttf is an exploratory OpenType 1.8 font made with a combination of Font Bureau's python font tools and the fontmake tool developed by Google; 
the latter requires two or more font styles with compatible contours, and meta-data concerning the relationship of the font styles, to combine two or more styles into a style axis of variation.
The font produced is an OpenType 1.8 Variation Font, containing a default design, and cumulative design masters that are designed to be interpolated between that default.

### Design

Amstelvar is a serif typeface design with references to oldstyle and modern typeface designs and so is apt for uses requiring such a style. Variation technology adds adeptness to the design for use at many sizes, with variety of weights, and widths at any size, as well as grades (a change of weight without change to width), another variety via a contrast axis, E.g. control over the difference between horizontal and vertical strokes and finally for all the glyphs, an axis to flatten the serif rise, changing the style from old style to slab serif. For the lowercase and selected glyphs with relation to the lowercase height, there is also an x-height axis.

### Specification notes

The design is produced on a 2000 unit per em grid, in quadratic Bézier curves and contains overlapping contours. The "Alpha" tag is indicative of the lack of a substantial glyph repertoire, currently only contains ASCII, as well as lacking any glyph positioning, glyph substitution, or conforms to the entire new open type 1.8 specification. This includes new tables of great importance including the stat table.

## II. The axis of AmstelvarAlpha

### Overview

The 5 axes initially published in the first version of Amstelvar Alpha are a combination of "registered" and "unregistered" axes, that either contain one or two styles in addition to the default, or regular style, in forming their axes.
The regular style itself is designed as a 12 point size master, "medium" weight, and wide, with low contrast for this style of type, as is apt for its size.
The axes are given unit per em values for the parametric change embodied in each axis, as is representable by one value, along with the required, -1, 0, +1 for UI presentation. 

### The Axes

#### 1. ParaWeight

A familiar weight axis has typically been seen through discrete fonts within a font family, progressing from thin to regular to black.

While there is no universal definition for the way their parameters are manipulated, here it is defined as a typeface's weight changing from light to heavy, without changing its apparent width, x-height or the angles of it strokes.
That is, the Weight axis of Amstelvar is parametric, as the progress of darkening and lightening only effects those parts, and as much as possible does not effect other parts, particularly the white space. 
So as Amstelvar gets bolder or lighter on the ParaWeight axis, the internal white spaces of the letters remain consistent, leaving their control to the ParaWidth axis. This is also the only current Amstelvar axis that uses two styles, one thinner than the regular and one bolder than the regular.

-1 is 10/2000, 0 176/2000 and 1 is 1000/2000, or half the em.

#### 2. ParaWidth

A familiar width axis has typically been seen through discrete font families within font superfamilies. 
It seeks to maintain the same characteristics of the wider or narrower styles, with whatever changes to contrast and weight are required for the given width, usually being used at a different size, and often being used at a very much larger size than the regular style (e.g. for headlines.)

The ParaWidth axis of Amstelvar is a reciprocal parametric axis, relative to the weight axis. 
It simply controls whitespace, reducing from the regular width, to very narrow white spaces inside and on either side of the glyphs.
It leaves the weight of the main stems as a parametric a match to the regular as well as leaving the contrast the same as the regular causing minimal collateral loss of blank space, except more beneficial like the length of serifs.
The axis currently only uses one style that takes it in the narrow were direction relative to the regular.

-1 is a white space of 84/2000 and 0, the default font has a white space of 804/2000.

#### 3. Contrast

Unlike the axes above, Contrast is not a registered axis in the OpenType 1.8 format specification.
But variety in contrast has a rich history in the type styles of many scripts, ranging from the subtleties of contrast's presence in most common sans serif fonts, to its obvious presence in type with ultra-thin serifs and connecting strokes as if under the direction of a sharp writing tool, and then into the "show down" realm of reverse contrast and reverse stress designs.

Amstelvar's Contrast axis provides only higher contrast (thinner contrasting strokes), relative to the default. It's effect is on the serifs, without changing the serif rise axis, and on many horizontal strokes, collecting into collateral effects on the internal and external white spaces of letters as it increases.

0 is the default contrast and is 100/2000, and -1 is high contrast and 8/2000 units per em. 

#### 4. Optical Size

An optical size axis normally mixes parametric values (as do “normal” width and weights in a typeface family of static styles.)
In “normal” optical sizing, the lowercase height, the weight, contrast and width, all vary to form the adapt style of a font, be they for readability at small sizes, or for compact and impactful use in large sizes.  

Contrary to an optical size axis, the x-Height axis of Amstelvar only modifies how tall the lowercase is, a subset of the parametric values that vary in 'high level' axes like optical size, width, and weight.

-1 has a lowercase of 890/2000, the default lowercase height is 1000/2000 and the +1 is at 1200/2000.

#### 5. Serif Rise

The Serif Rise is an unregistered axis, and has one required function in the style as designed: To lighten the serifs in the second of two ways. 
The first way to ligthen the serifs is to use the Contrast axis, which gives the design space control over the height of the serif base. 
The second way, which this axis controls, is to vary the diagonal rise of the segments connecting to the main stems, both straight and curved.

-1 has a serif rise of zero units and the default is a rise of 35/2000.

## III. Design space, User Space, and the combinatorial explosion of deltas.

The eight masters currently creating the Variation font’s design space encompass a large number of combinations of the 3 registered axes. 
The delta values of the main axes, weight, width and contrast, cover quite large ranges for each of those parameters respectively. 
So the design space of Amstelvar is quite large compared to what most font families contain stylistically.

Additonally, there currently is no difference between the design space and user space.
This is allowed by the new font format, but not yet implemented.

5 full axes, i.e. with style change at both -1 and +1 in each axis,  combine to create 120 extrapolated styles of effected by from 2 to 5 axes.
There are two instances in such an example with all five axes at +1, and all five axes at -1, and then a lot with just four at +1, and one at -1, and so on.
I’d call these, in an example 5-axes variation font, duovars, triovars, quadravars, and the two pentavars.

Axes with collections of extreme deltas often create wild contours as the deltas add up in ways not intended by the type designer.
Part of this wildness is not finding the exact right position for every control point in the entire design space, and some wildness is uncontrollable as a result of the delta range, or the need tof intermediate instances to tame the contours.
One immediate solution is the type designer’s intervention, correcting the extrapolations and adding them back to the design space where the result of two or more axes would otherwise extrapolate incorrectly.
Amstelvar contains some corrected duovars in the design and user space, but in this early alpha there is plenty of qualitative wilderness around the edges of things.
