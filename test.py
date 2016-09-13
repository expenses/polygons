import os
import polygons

svg = "testing/tuatara.svg"
image = "testing/tuatara.jpg"
output = "testing/output/{test}.svg"

if not os.path.isdir(os.path.dirname(output)):
    os.makedirs(os.path.dirname(output))

polygons.colour(svg, image, output.format(test="fill"))
polygons.colour(svg, image, output.format(test="stroke - 1"), stroke=1)
polygons.colour(svg, image, output.format(test="stroke - 5"), stroke=5)
polygons.colour(svg, image, output.format(test="stroke - perimeter"),
                stroke="perimeter")
polygons.colour(svg, image, output.format(test="stroke - pixels"),
                stroke="pixels")
