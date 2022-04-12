The goal of Jomatra is a unified graphics language conversion through a common geometry protocol: `JomatPy`. It is the equivalent of Pandoc but for graphics.

1. JomatPy <--> GeoGebra
2. JomatPy <--> Asymptote
3. JomatPy <--> TikZ
4. JomatPy <--> Manim

## Motivation

Currently, there are many tools for drawing geometric diagrams and figures. Therefore some kind of a unified system of input is needed for that.

 Every geometry drawing is a special case. Therefore, geometric construction involve 3 parts:

1. Semantics:  All this part provides is the raw instructions.
1. Numerics: An average example of the drawing.
1. Style: How to draw it. What colors, linestyles, decorations, etc... you should use.
