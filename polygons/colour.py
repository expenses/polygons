import tqdm
import xml.etree.ElementTree as ET
from skimage.draw import polygon
from skimage.io import imread
from .tools import avg, perimeter


def colour(svg_path, image_path, output_path, stroke=False, scale=1):
    svg = ET.parse(svg_path)
    # Load the image as a 2d numpy array with rgb in a list
    image = imread(image_path)
    # Create a list of polygons based off element tags (<polygon .. />)
    polygons = [el for el in svg.getroot() if el.tag.endswith("polygon")]

    # Loop through polygons with the tqdm progress bar
    for poly in tqdm.tqdm(polygons, mininterval=0.01):
        # Get out points attribute (points="..")
        points = poly.attrib["points"]
        channels = [0, 0, 0]
        # Set up a list of y and x coordinates
        coords = [[], []]

        # Add the x and y coordinates for each point
        for point in points.split():
            for dimension, value in enumerate(point.split(",")):
                coords[dimension].append(float(value))

        if scale != 1:
            for dimension in coords:
                for i, point in enumerate(dimension):
                    # Change the point by the distance to the center x scale
                    dimension[i] -= (avg(dimension) - point) * (scale - 1)

        # Create a list of pixels from the image using the coords and shape
        pixels = image[polygon(coords[1], coords[0], image.shape)]

        # If the list isn't empty (some polys cover less than 1 pixel)
        if len(pixels):
            # Loop through pixels and add colour values to channel totals
            for rgb in pixels:
                for i in range(3):
                    channels[i] += rgb[i]

            # And get the average
            channels = [int(channel/len(pixels)) for channel in channels]
        else:
            # Find the values of the average (center) pixel of the poly
            channels = image[int(avg(coords[1])), int(avg(coords[0]))]

        # Set the polygon attributes
        poly.attrib = {
            "points": points,
            # Use a tuple version of the channels to format the string
            "stroke" if stroke else "fill": "rgb(%s, %s, %s)" % tuple(channels)
        }

        if stroke:
            poly.attrib.update({
                "fill": "none",
                "stroke-linejoin": "bevel",
                "stroke-width": str(
                    # Use the perimeter of the poly / 10
                    perimeter(coords[0], coords[1])/10 if stroke == "perimeter"
                    # Use the sqrt of len(pixels) (or 1) / 2
                    else (len(pixels) or 1) ** 0.5 / 2 if stroke == "pixels"
                    # Use the entered stroke value (num expected)
                    else stroke
                )})

    # Write out the svg
    svg.write(output_path)
