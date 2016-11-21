import os
import sys
import polygons

this = sys.path[0]

sources = (os.path.join(this, "testing/tuatara.svg"),
           os.path.join(this, "testing/tuatara.jpg"))
output = os.path.join(this, "testing/output/{}.svg")

if not os.path.isdir(os.path.dirname(output)):
    os.makedirs(os.path.dirname(output))

polygons.colour(*sources, output.format("fill"))
polygons.colour(*sources, output.format("stroke - 1"), stroke=1)
polygons.colour(*sources, output.format("stroke - 5"), stroke=5)
polygons.colour(*sources, output.format("stroke - perimeter"),
                stroke="perimeter")
polygons.colour(*sources, output.format("stroke - pixels"), stroke="pixels")
polygons.colour(*sources, output.format("scale - 1.5"), scale=1.5)
polygons.colour(*sources, output.format("scale - 0.5"), scale=0.5)
polygons.colour(*sources, output.format("resized - 1.5"), scale=1.5,
                resize=True)
polygons.colour(*sources, output.format("resized - 0.5"), scale=0.5,
                resize=True)
