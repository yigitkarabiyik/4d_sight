# 4d_sight

purpuse of this study is to find 4 corner coordinates of small area images in 
the large image.

there is a find_kernel function in the basic.py file which takes two inputs
large and small image. Transpose, mirror image by origin, x axis, y axis
of small image obtained with first for loop. In the second for loop, get array 
of small image with rotated 90, 180 and 270 degree. In last two for loops 
create kernel to run in the large image and compare both of it. If catched the
same image print 4 corner coordinate as output. find_kernel function called
with images paths at the last line.

This program gave output for small_area.png. However, there was not any output
for small_area_rotate.png.
