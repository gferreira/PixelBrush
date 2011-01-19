PixelBrush
==========

A simple tool to draw outline pixel fonts in FontLab.

Credits
-------

Developed by [Hartmut Bohnacker](http://www.hartmut-bohnacker.de/), based on one of the macro tools included in FontLab.

Installation
------------

1. download the file Pixel125.py
2. put it inside the folder `FontLab/Data/Macros/System/Tool`
3. start FontLab

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