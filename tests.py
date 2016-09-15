import os
import polygons

sources = ["testing/tuatara.svg", "testing/tuatara.jpg"]
output = "testing/output/{test}.svg"

if not os.path.isdir(os.path.dirname(output)):
    os.makedirs(os.path.dirname(output))

polygons.colour(*sources, output.format(test="fill"))
polygons.colour(*sources, output.format(test="stroke - 1"), stroke=1)
polygons.colour(*sources, output.format(test="stroke - 5"), stroke=5)
polygons.colour(*sources, output.format(test="stroke - perimeter"),
                stroke="perimeter")
polygons.colour(*sources, output.format(test="stroke - pixels"),
                stroke="pixels")
polygons.colour(*sources, output.format(test="scale - 1.5"), scale=1.5)
polygons.colour(*sources, output.format(test="scale - 0.5"), scale=-0.5)
polygons.colour(*sources, output.format(test="resized - 1.5"), scale=1.5,
                resize=True)
polygons.colour(*sources, output.format(test="resized - 0.5"), scale=-0.5,
                resize=True)
