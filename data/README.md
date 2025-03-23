# CS 1440 Project 4.1: Object-Oriented Design - Picture Gallery

Many of these files are not compatible with Project 4.0, but may be used in Project 4.1.

The colors produced by your program will not match these samples.  This is because your color palettes differ from mine.  The overall shape should still be recognizable when you render these images with your program.  If your images lack definition, increase the contrast between colors in your palette.


### bsj-caterpillar.frac

~~~config
# Zoom on the central spur on the left side of the Burning Ship Julia
# You'll need to implement this formula yourself to make your program produce this image
Type:       Burningshipjulia
Creal:      -.598
Cimag:      .9225
CenterX:    -0.69
Centery:    0
Axislength: .16
Pixels:     768
Iterations: 178
~~~

![./assets/bsj-caterpillar.png](./assets/bsj-caterpillar.png "Image generated from bsj-caterpillar.frac")


### bsj-take-off-every-zig.frac

~~~config
# A close up of one of the "eyes" in a Burning Ship Julia fractal.
# I see lots of small space ships departing from the mother ship.
# You'll need to implement this formula yourself to make your program produce this image
type:       burningshipjulia
creal:      -.598
cimag:      .9225
centerx:    0.347
centery:    0.945
axislength: 0.1
pixels:     768
iterations: 148
~~~

![./assets/bsj-take-off-every-zig.png](./assets/bsj-take-off-every-zig.png "Image generated from bsj-take-off-every-zig.frac")


### bs-miniship.frac

~~~config
# A miniature Burning Ship shape found at the tip of the overall fractal
# You'll need to implement this formula yourself so your program can produce this image
Iterations: 124
Pixels: 768
AxisLength: 0.210
Centery: -0.025
CenterX: -1.77
Type: Burningship
~~~

![./assets/bs-miniship.png](./assets/bs-miniship.png "Image generated from bs-miniship.frac")


### bs-prow.frac

~~~config
# Front section of the Burning Ship fractal
# You'll need to implement this formula yourself so your program can produce this image
type: burningship
pixels: 512
axislength: 1.1910
iterations: 128
centery: -0.125
centerx: -1.37
~~~

![./assets/bs-prow.png](./assets/bs-prow.png "Image generated from bs-prow.frac")


### bs-stern.frac

~~~config
# Burning Ship fractal zoomed in to the back
# You'll need to implement this formula yourself so your program can produce this image
Type: Burningship
Pixels: 512
Iterations: 144
Axislength: 0.8910
Centery: -1.55
Centerx: 0.9
~~~

![./assets/bs-stern.png](./assets/bs-stern.png "Image generated from bs-stern.frac")


### bs-towers.frac

~~~config
# Towers growing out of the top of the ship
# If you design a color palette that uses blues and reds cleverly, it will look
# like a ship caught in a raging inferno.
#
# (The apperance of this fractal improves when you flip it vertically in an image editor)
# You'll need to implement this formula yourself so your program can produce this image
Type: Burningship
Pixels: 640
Iterations: 128
CenterX: -1.7472
CenterY: -0.037233
AxisLength: 0.11038
~~~

![./assets/bs-towers.png](./assets/bs-towers.png "Image generated from bs-towers.frac")


### bs-wake.frac

~~~config
# A miniature Burning Ship shape found by zooming in on the frothy wake of the larger ship
# You'll need to implement this formula yourself so your program can produce this image
Type: burningship
pixels: 512
iterations: 144
axislength: 0.062
centery: -1.527
centerx: 0.875
~~~

![./assets/bs-wake.png](./assets/bs-wake.png "Image generated from bs-wake.frac")


### burningship.frac

~~~config
# A basic Burning Ship fractal
# You'll need to implement this formula yourself to make your program produce this image
Type: Burningship
centerX: 0
centerY: 0
axisLength: 3.7
pixels: 768
iterations: 96
~~~

![./assets/burningship.png](./assets/burningship.png "Image generated from burningship.frac")


### burningshipjulia.frac

~~~config
# A basic Burning Ship Julia fractal
# You'll need to implement this formula yourself to make your program produce this image
type: burningshipjulia
creal: -.598
cimag: .9225
centerx: 0
centery: 0
axislength: 4
pixels: 768
iterations: 128
~~~

![./assets/burningshipjulia.png](./assets/burningshipjulia.png "Image generated from burningshipjulia.frac")


### j-connected.frac

~~~config
# A connected Julia set fractal
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: .26
cimag: .0016
centerx: 0
centery: 0
axislength: 2.17
pixels: 512
iterations: 64

# See also unconnected.frac
~~~

![./assets/j-connected.png](./assets/j-connected.png "Image generated from j-connected.frac")


### j-fjords.frac

~~~config
# Maybe it's the shoreline of some fjords?

# You'll need to implement this formula yourself so your program can produce this image

# Found in http://bl.ocks.org/syntagmatic/raw/3736720/ with these parameters
#
# Their rendering algorithm outputs this image upside-down relative to ours

type: julia
cReal: -1.0125
cImag: 0.275
pixels: 512
centerx: -0.339230468501458
centery: 0.417970758224314
axislength: 0.164938488846612
iterations: 48
~~~

![./assets/j-fjords.png](./assets/j-fjords.png "Image generated from j-fjords.frac")


### j-hourglass.frac

~~~config
# I think this looks like an hourglass
# You'll need to implement this formula yourself so your program can produce this image
Type: Julia
creal: -1
Cimag: 0
pixels: 1024

# I guess "X marks the spot" works, too.  Naming stuff is hard, okay?

Centerx: 0.618
centerY: 0.0
axisLength: 0.017148277367054
iterations: 78
~~~

![./assets/j-hourglass.png](./assets/j-hourglass.png "Image generated from j-hourglass.frac")


### j-lace-curtains.frac

~~~config
# My grandmother has lace curtains that look JUST LIKE THIS!
# You'll need to implement this formula yourself so your program can produce this image
type:   Julia
pixels: 640
iterations: 256
centerX:   -1.0153
centerY:    0.2521
axisLength: 0.0121
cReal: -1.0
cImag: 0.0
# Disregard these comments...
# minReal:-1.0234586445652 maxReal:-1.00729578671778
# minImag:0.243364355580952 maxImag:0.255486498966514
~~~

![./assets/j-lace-curtains.png](./assets/j-lace-curtains.png "Image generated from j-lace-curtains.frac")


### julia-1.0.frac

~~~config
# The full julia set, but these creal and cimag values are BORING
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: -1.0
cimag: 0.0
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78
~~~

![./assets/julia-1.0.png](./assets/julia-1.0.png "Image generated from julia-1.0.frac")


### julia-1.1301.frac

~~~config
# The full julia set, but with different creal and cimag values
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: -1.1301
cimag: 0.262
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78
~~~

![./assets/julia-1.1301.png](./assets/julia-1.1301.png "Image generated from julia-1.1301.frac")


### julia.frac

~~~config
# The full Julia set in all its glory
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: -1.0125
cimag: 0.275
pixels: 1024
centerx: 0.0
centery: 0.0
axislength: 4.0
iterations: 78
~~~

![./assets/julia.png](./assets/julia.png "Image generated from julia.frac")


### j-unconnected.frac

~~~config
# An unconnected Julia set fractal
# You'll need to implement this formula yourself so your program can produce this image
type: julia
creal: .26
cimag: .0015
centerx: 0
centery: 0
axislength: 2.17
pixels: 512
iterations: 64

# See also connected.frac
~~~

![./assets/j-unconnected.png](./assets/j-unconnected.png "Image generated from j-unconnected.frac")


### j-x-marks-the-spot.frac

~~~config
# X Marks The Spot!

# You'll need to implement this formula yourself so your program can produce this image
type:   Julia

pixels: 640

iterations: 256

cReal: -1.0125

cImag: 0.275

centerX: -0.251833357526491

centerY: 0.202938441870375

axisLength: 0.0120869329407663
~~~

![./assets/j-x-marks-the-spot.png](./assets/j-x-marks-the-spot.png "Image generated from j-x-marks-the-spot.frac")


### m3-antlers.frac

~~~config
# Antlers in the Mandelbrot^3 set
# You'll need to implement this formula yourself to make your program produce this image
type: Mandelbrot3
pixels: 640
centerx: 0.651324
centery: 0.5112312
axislength: 0.122301
iterations: 128
~~~

![./assets/m3-antlers.png](./assets/m3-antlers.png "Image generated from m3-antlers.frac")


### m3-seven-arms.frac

~~~config
# Seven-armed spiral in the Mandelbrot^3 fractal
# You'll need to implement this formula yourself to make your program produce this image
type: mandelbrot3
pixels: 640

centerx: -0.2786
centery: -0.74285

axislength: 0.016
iterations: 128
~~~

![./assets/m3-seven-arms.png](./assets/m3-seven-arms.png "Image generated from m3-seven-arms.frac")


### m4-curls.frac

~~~config
# Curls made of curls in the Mandelbrot^4 fractal
# You'll need to implement this formula yourself to make your program produce this image

type: mandelbrot4
pixels: 640

iterations: 384

centerX: -0.24756781
centerY: 0.46511148

axisLength: 0.000600098
~~~

![./assets/m4-curls.png](./assets/m4-curls.png "Image generated from m4-curls.frac")


### m4-swirls.frac

~~~config
# Swirls deep in the Mandelbrot^4 fractal
# You'll need to implement this formula yourself to make your program produce this image

Type: Mandelbrot4

CenterX: 0.3491936
CenterY: -0.7073472

Pixels: 640

Iterations: 384
AxisLength: 0.001259061
~~~

![./assets/m4-swirls.png](./assets/m4-swirls.png "Image generated from m4-swirls.frac")


### m-8-points.frac

~~~config
# The characteristic Mandelbrot shape embedded within an 8-pointed compass
type: Mandelbrot

centerY: -0.0
centerX: -1.999774061505
axisLength: 0.000000361314
iterations: 350
pixels: 1024
~~~

![./assets/m-8-points.png](./assets/m-8-points.png "Image generated from m-8-points.frac")


### mandelbrot.frac

~~~config
# Basic mandelbrot set, fully zoomed out
type: mandelbrot
pixels: 640
axislength: 2.55

iterations: 96

centerx: -0.7
centery: 0.0
~~~

![./assets/mandelbrot.png](./assets/mandelbrot.png "Image generated from mandelbrot.frac")


### mandelbrot-zoomed.frac

~~~config
# Basic mandelbrot set, zoomed in a bit and with more iterations
type: mandelbrot
pixels: 640
axislength: 1.0

iterations: 256

centery: 0.0
centerx: -1.0
~~~

![./assets/mandelbrot-zoomed.png](./assets/mandelbrot-zoomed.png "Image generated from mandelbrot-zoomed.frac")


### mandel-pow3.frac

~~~config
# Mandelbrot^3, fully zoomed out
# You'll need to implement this formula yourself to make your program produce this image
Type: Mandelbrot3
axisLength: 2.7

centerX: 0.0
centerY: 0.0

pixels: 640
iterations: 96
~~~

![./assets/mandel-pow3.png](./assets/mandel-pow3.png "Image generated from mandel-pow3.frac")


### mandel-pow4.frac

~~~config
# Mandelbrot^4, fully zoomed out
# You'll need to implement this formula yourself to make your program produce this image
type: mandelbrot4
axislength: 2.4

centerx: -0.2
centery: 0.0

pixels: 640
iterations: 96
~~~

![./assets/mandel-pow4.png](./assets/mandel-pow4.png "Image generated from mandel-pow4.frac")


### m-branches@0064.frac

~~~config
# A branching spiral, rendered to 64 iterations
# Don't adjust your screen - there really is nothing to see here
type: mandelbrot
pixels: 640
iterations: 64
centerx: 0.354957789387306
centery: -0.338644137198173
axislength: 5.05822370716613e-06
~~~

![./assets/m-branches@0064.png](./assets/m-branches@0064.png "Image generated from m-branches@0064.frac")


### m-branches@0128.frac

~~~config
# A branching spiral, rendered to 128 iterations
# More interesting than before
type: mandelbrot
pixels: 640
iterations: 128
centerx: 0.354957789387306
centery: -0.338644137198173
axislength: 5.05822370716613e-06
~~~

![./assets/m-branches@0128.png](./assets/m-branches@0128.png "Image generated from m-branches@0128.frac")


### m-branches@0256.frac

~~~config
# A branching spiral, rendered to 256 iterations
# Now we're getting somewhere!
type: mandelbrot
pixels: 640
iterations: 256
centerx: 0.354957789387306
centery: -0.338644137198173
axislength: 5.05822370716613e-06
~~~

![./assets/m-branches@0256.png](./assets/m-branches@0256.png "Image generated from m-branches@0256.frac")


### m-branches@0512.frac

~~~config
# A branching spiral, rendered to 512 iterations
# Mind == Blown
type: mandelbrot
pixels: 640
iterations: 512
centerx: 0.354957789387306
centery: -0.338644137198173
axislength: 5.05822370716613e-06
~~~

![./assets/m-branches@0512.png](./assets/m-branches@0512.png "Image generated from m-branches@0512.frac")


### m-branches@1024.frac

~~~config
# A branching spiral, rendered to 1024 iterations
# About as good as it gets - more iterations at this scale aren't worth the time
type: mandelbrot
pixels: 640
iterations: 1024
centerx: 0.354957789387306
centery: -0.338644137198173
axislength: 5.05822370716613e-06
~~~

![./assets/m-branches@1024.png](./assets/m-branches@1024.png "Image generated from m-branches@1024.frac")


### m-coral.frac

~~~config
# This one reminds me of coral
type: Mandelbrot
pixels: 1024
centerX: -0.693792639088625
centerY: -0.36850658033037173
axisLength: 0.005
pixels: 640
iterations: 512
~~~

![./assets/m-coral.png](./assets/m-coral.png "Image generated from m-coral.frac")


### m-elephants.frac

~~~config
# Can you see elephants swinging their trunks?
type: mandelbrot
pixels:     640
centerx:    0.3015
centery:    -0.0200
axislength: 0.03
iterations: 100
~~~

![./assets/m-elephants.png](./assets/m-elephants.png "Image generated from m-elephants.frac")


### m-enhance.frac

~~~config
# Enhance.  Enhance.  ENHANCE!!
pixels:     512
centerx:    -1.48
centery:    0.0
axislength: 0.01
iterations: 300
type: mandelbrot
~~~

![./assets/m-enhance.png](./assets/m-enhance.png "Image generated from m-enhance.frac")


### m-leaf.frac

~~~config
# Veins on a leaf.  I found this one in GNU XaoS.
type: mandelbrot
pixels: 640
centerx:     -1.543577002
centery:     -0.000058690069
axislength:  0.000051248888
iterations: 96
~~~

![./assets/m-leaf.png](./assets/m-leaf.png "Image generated from m-leaf.frac")


### m-minibrot.frac

~~~config
# uWu... it's just so cute and TINY!
Type:       Mandelbrot
pixels:     1024
centerx:   -1.40812110900879
centery:   -0.136344909667969
axislength: 0.0028839111328125
iterations: 350
~~~

![./assets/m-minibrot.png](./assets/m-minibrot.png "Image generated from m-minibrot.frac")


### m-rabbit-hole.frac

~~~config
# Down the rabbit  h o l e   y  o  u       g     o
centerx: -0.76
centery: 0.117684887459807
pixels: 640
type:   mandelbrot
axislength: 0.204501607717042
iterations: 256
~~~

![./assets/m-rabbit-hole.png](./assets/m-rabbit-hole.png "Image generated from m-rabbit-hole.frac")


### m-seahorse.frac

~~~config
# I can sea the horse.  Can you?
type:         mandelbrot
pixels:       640
centerx:   -0.748
centery:   -0.102
axislength: 0.008
iterations: 384
~~~

![./assets/m-seahorse.png](./assets/m-seahorse.png "Image generated from m-seahorse.frac")


### m-spiral0.frac

~~~config
# spiral0 from the original starter code
axislength: 0.00497817993164062
iterations: 512

type:   mandelbrot
pixels: 640


centerx: -0.761335372924805
centery: 0.0835704803466797
~~~

![./assets/m-spiral0.png](./assets/m-spiral0.png "Image generated from m-spiral0.frac")


### m-spiral1@0256.frac

~~~config
# spiral1 from the original starter code, but rendered to 256 iterations
iterations: 256
pixels: 640
centerx: -0.747
centery: 0.1075
axislength: 0.002
type: mandelbrot
~~~

![./assets/m-spiral1@0256.png](./assets/m-spiral1@0256.png "Image generated from m-spiral1@0256.frac")


### m-spiral1@0512.frac

~~~config
# spiral1 from the original starter code, but rendered to 512 iterations
iterations: 512
type: mandelbrot
pixels: 640
centerx: -0.747
centery: 0.1075
axislength: 0.002
~~~

![./assets/m-spiral1@0512.png](./assets/m-spiral1@0512.png "Image generated from m-spiral1@0512.frac")


### m-spiral1@1024.frac

~~~config
# spiral1 from the original starter code, but rendered to 1024 iterations
iterations: 1024
type: mandelbrot
pixels: 640
centerx: -0.747
centery: 0.1075
axislength: 0.002
~~~

![./assets/m-spiral1@1024.png](./assets/m-spiral1@1024.png "Image generated from m-spiral1@1024.frac")


### m-spiral1.frac

~~~config
# spiral1 from the original starter code
iterations: 100
type: mandelbrot
pixels: 640
centerx: -0.747
centery: 0.1075
axislength: 0.002
~~~

![./assets/m-spiral1.png](./assets/m-spiral1.png "Image generated from m-spiral1.frac")


### m-spiral-jetty.frac

~~~config
# An homage to Utah's official work of art
# Have you ever visited the northeast shore of the Great Salt Lake?

iterations: 1024
pixels: 1024
type: mandelbrot
centerx: -0.761335372924805
centery: 0.0835704803466797
axislength: 0.00497817993164062
~~~

![./assets/m-spiral-jetty.png](./assets/m-spiral-jetty.png "Image generated from m-spiral-jetty.frac")


### m-starfish.frac

~~~config
# Reminds me of a starfish... you can see it, too, right?
type:   Mandelbrot
pixels: 640
iterations: 312
centerX: -0.463595023481762
centerY: 0.598380871135558
axisLength: 0.00128413675654471
~~~

![./assets/m-starfish.png](./assets/m-starfish.png "Image generated from m-starfish.frac")


### m-wholly-squid.frac

~~~config
# Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn!
type: mandelbrot
pixels: 640
iterations: 256
centerx: -0.744740098129553
centery: 0.209610393372855
axislength: 0.00160629282219288
~~~

![./assets/m-wholly-squid.png](./assets/m-wholly-squid.png "Image generated from m-wholly-squid.frac")


### n-braid.frac

~~~config
# A braid within the Newton set
# You'll need to implement this formula yourself so your program can produce this image
type: newton
pixels: 1080

axisLength: 0.232
centerX: -0.398
iterations: 200

centerY: 0.195
~~~

![./assets/n-braid.png](./assets/n-braid.png "Image generated from n-braid.frac")


### newton.frac

~~~config
# Basic Newton fractal, fully zoomed out
# You'll need to implement this formula yourself so your program can produce this image

AxisLength: 4.0
iterations: 100

Type: Newton
pixels: 640

centerx: 0.0
CenterY: 0.0
~~~

![./assets/newton.png](./assets/newton.png "Image generated from newton.frac")


### newton-zoomed.frac

~~~config
# Newton fractal, zoomed in to the center
# You'll need to implement this formula yourself so your program can produce this image
Type: Newton

pixels: 640

centerx: 0.0
centery: 0.0

axislength: 0.01

iterations: 100
~~~

![./assets/newton-zoomed.png](./assets/newton-zoomed.png "Image generated from newton-zoomed.frac")


### p-feathers.frac

~~~config
# Phoenix Fractal - Peacock tail

type: phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
centerY: -0.363287878200906
centerX: 0.381197981824009
axisLength: 0.0840187115019564
pixels: 512
iterations: 101
~~~

![./assets/p-feathers.png](./assets/p-feathers.png "Image generated from p-feathers.frac")


### phoenix.frac

~~~config
# Phoenix Fractal by Brock

type: phoenix
# P and C values taken from http://usefuljs.net/fractals/docs/mandelvariants.html, "Variations on the Mandelbrot Set Formula"
preal: -0.5
pimag: 0.0
creal: 0.5667
cimag: 0.0
centerx: 0
centery: 0
axislength: 3.25
pixels: 512
iterations: 101
~~~

![./assets/phoenix.png](./assets/phoenix.png "Image generated from phoenix.frac")


### p-monkey-knife-fight.frac

~~~config
# Phoenix Fractal: Monkey! Knife! Fight!

axisLength: 0.136626506024096
iterations: 101

type: Phoenix
preal: -0.5
pimag: 0.0

# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
pixels: 512

centerY: -0.945542168674699
centerX: 0.232234726688103
~~~

![./assets/p-monkey-knife-fight.png](./assets/p-monkey-knife-fight.png "Image generated from p-monkey-knife-fight.frac")


### p-obconical-kale.frac

~~~config
# I couldn't think of a good name , so I asked ChatGPT what to call this picture

type: phoenix
pixels: 640
iterations: 256
centerX: -0.1925541
centerY: -0.4770098
axisLength: 0.002444398
preal: -0.5
pimag: 0.0
creal: 0.5667
cimag: 0.0
~~~

![./assets/p-obconical-kale.png](./assets/p-obconical-kale.png "Image generated from p-obconical-kale.frac")


### p-oriental-dragons.frac

~~~config
# Phoenix Fractal - A big European dragon composed of smaller Oriental dragons

type: phoenix
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.57
cimag: 0.0

preal: -0.486
pimag: 0.0
pixels: 1024

iterations: 128

centerY: -0.611292072047808
centerX: -0.0428352613957943

axisLength: 0.0097572606582521
~~~

![./assets/p-oriental-dragons.png](./assets/p-oriental-dragons.png "Image generated from p-oriental-dragons.frac")


### p-shrimp-cocktail.frac

~~~config
# Phoenix: Shrimp Cocktail

type: Phoenix
preal: -0.5
pimag: 0.0
# c value taken from http://usefuljs.net/fractals/docs/julia_mandelbrot.html, "Connected and Unconnected Sets"
creal: 0.5667
cimag: 0.0
pixels: 512
iterations: 101

CENTERY: 0.529156626506024
CENTERX: -0.3516077170418
AXISLENGTH: 0.221204819277108
~~~

![./assets/p-shrimp-cocktail.png](./assets/p-shrimp-cocktail.png "Image generated from p-shrimp-cocktail.frac")


### p-tentacles.frac

~~~config
# This picture makes me worry about facing a kraken
pixels: 640
iterations: 384

centerX: -0.165011
axisLength: 0.0352518
centerY: -0.447992

preal: -0.5
pimag: 0.0

creal: 0.5667
cimag: 0.0
~~~

![./assets/p-tentacles.png](./assets/p-tentacles.png "Image generated from p-tentacles.frac")


### s-bridges.frac

~~~config
# Another zoom-in on the spider fractal
# You'll need to implement this formula yourself so your program can produce this image
type: spider
pixels: 640
iterations: 200
axisLength: 0.009541275
centerX: -0.1354762
centerY: -0.6104258
~~~

![./assets/s-bridges.png](./assets/s-bridges.png "Image generated from s-bridges.frac")


### s-island.frac

~~~config
# Spider island
# You'll need to implement this formula yourself so your program can produce this image
Type: Spider
Pixels: 1024
Centerx: 0.018
Centery: 0.700
Axislength: 0.25
Iterations: 256
~~~

![./assets/s-island.png](./assets/s-island.png "Image generated from s-island.frac")


### spider.frac

~~~config
# Basic Spider set, fully zoomed out
# You'll need to implement this formula yourself so your program can produce this image
Type: spider
Pixels: 640
Centerx: -1.0
Centery: 0.0
Axislength: 4.0
Iterations: 100
~~~

![./assets/spider.png](./assets/spider.png "Image generated from spider.frac")


### s-spinneret.frac

~~~config
# The Spider's spinneret
# You'll need to implement this formula yourself so your program can produce this image
Type: Spider
Pixels: 640
Iterations: 245
Centerx: -1.956
Centery: 0.0
AxisLength: 0.1
~~~

![./assets/s-spinneret.png](./assets/s-spinneret.png "Image generated from s-spinneret.frac")
