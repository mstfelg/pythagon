# CLAPS Language

CLAPS is an optimized geometric notation for presenting the algorithm (i. e the set of instructions) to build complicated geometric diagrams.

## Motivation

Currently, there are many tools for drawing geometric diagrams and figures. Therefore some kind of a unified system of input is needed for that.

 Every geometry drawing is a special case. Therefore, geometric construction involve 3 parts:

1. Semantics:  All this part provides is the raw instructions.
1. Numerics: An average example of the drawing.
1. Style: How to draw it. What colors, linestyles, decorations, etc... you should use.

Claps name comes from:

- C - circle
- L - line
- A - angle
- P - point
- S - segment

## Goals

Project goals and raw ideas:

* Program an **<u>algebraic calculator</u>** of geometric objects.
* Optimize **<u>geometry notation</u>** (CLAPS)
  * Notation for academic writing
  * Notation for computer programming
* Write a **<u>protocol</u>** for parsing and converting between geometric constructions. (e.g: Convert between CLAPS to GeoGebra execute code)

## Features

1. Abstract, overloaded, and general.
1. Generalized:
   1. Every line is a circle of radius infinity
   1. Every point is a circle of radius zero

## Standard conventions

Points -1 capitalized latin letters written in anti-clockwise order, with A above.

Segments - small latin letters, in triangles, each letter is assigned to the non-adjacent side. In other polygons it's written in the following order a = AB, b = BC, c = CA, ...

Lines - for general lines - small letters starting from l, for specific lines: just AB, BC, CA...

Angles - when there is no ambigiouity, an angle is referred to by its vertex.