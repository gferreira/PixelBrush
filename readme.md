PixelBrush
==========

A simple tool to draw pixel fonts (outline-based bitmap fonts) in FontLab Studio.

Credits
-------

Pixel brush was developed by [Hartmut Bohnacker](http://hartmut-bohnacker.de/) in 2005, based on one of the macro tools included in FontLab.

Additional versions contributed by [Paul van der Laan](http://type-invaders.com/) (pixel size variable according to FontLab grid preferences) and [Frederik Berlaen](http://typemytype.com/) (cross stitch brush).

Distributed by [Gustavo Ferreira](http://hipertipo.com/).

Installation
------------

1. download the file Pixel125.py
2. put it inside the folder `/Library/Application Support/FontLab/Studio 5/Macros/System/Tool`
3. re-start FontLab

Using the brush
---------------

1. Create a new font (or open an existing one).
2. Make sure the grid size of the glyph window is the same as the size of your brush (in `Preferences/Glyph Window/Grid Step`).
3. Open a glyph window.
4. In the Macro toolbar, choose `Pixel125` from the tools drop-down menu.
5. Click on the canvas to start painting pixels.
6. Have fun!

Customizing the brush
---------------------

The size of the brush is set by the attribute `self.size` (in line 11 of the code). Change this value if you want other element sizes.

License
-------

[BSD License](http://www.opensource.org/licenses/bsd-license.php)
