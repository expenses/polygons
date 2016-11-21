from tqdm import tqdm
import xml.etree.ElementTree as ET
from skimage import draw, io
from numpy import average
from math import hypot


def intavg(array, dimension=-1):
    return average(array, dimension).astype(int)


def perimeter(xords, yords):
    perimeter = 0
    for i in range(len(xords)):
        perimeter += hypot(xords[i] - xords[i-1], yords[i] - yords[i-1])
    return perimeter


def colour(svg_path, image_path, output_path, stroke=False, scale=1,
           resize=False):
    svg = ET.parse(svg_path)
    image = io.imread(image_path)

    # Verify that the image has 3 channels
    if image.shape[2] != 3:
        print("Invalid image. Requires RGB.")
        exit()

    # Create a list of polygons based off element tags (<polygon .. />)
    polygons = [el for el in svg.getroot() if el.tag.endswith("polygon")]

    # Loop through polygons with the tqdm progress bar
    for poly in tqdm(polygons, mininterval=0.01):
        # Get out points attribute (points="..")
        points = poly.attrib["points"]
        # Set up a list of y and x coordinates
        coords = [[], []]

        # Add the x and y coordinates for each point
        for point in points.split():
            for dimension, value in enumerate(point.split(",")):
                coords[dimension].append(float(value))

        if scale != 1:
            for i, dimension in enumerate(coords):
                coords[i] -= (average(dimension) - dimension) * (scale - 1)

        # Create a list of pixels from the image using the coords and shape
        pixels = image[draw.polygon(coords[1], coords[0], image.shape)]
        # And get out the image channels as a rbg tuple
        channels = tuple(
            intavg(pixels, 0) if len(pixels) else
            # Get the center pixel instead of average (if poly is too small)
            image[intavg(coords[1]), intavg(coords[0])]
        )

        if resize:
            points = ""
            for point in range(len(coords[0])):
                points += "%s,%s " % (coords[0][point], coords[1][point])

        # Set the polygon attributes
        poly.attrib = {
            "points": points,
            "stroke" if stroke else "fill": "rgb(%s, %s, %s)" % channels
        }

        if stroke:
            poly.attrib.update({
                "fill": "none",
                "stroke-linejoin": "bevel",
                "stroke-width": str(
                    # Use the perimeter of the poly / 10
                    perimeter(*coords) / 10 if stroke == "perimeter"
                    # Use the sqrt of len(pixels) (or 1) / 2
                    else (len(pixels) or 1) ** 0.5 / 2 if stroke == "pixels"
                    # Use the entered stroke value (num expected)
                    else stroke
                )})

    # Write out the svg
    svg.write(output_path)
