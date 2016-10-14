import argparse


def setup_args():
    parser = argparse.ArgumentParser(
        description="A cli tool for colouring svg meshes")

    parser.add_argument("svg", help="The svg mesh to colourize.")

    parser.add_argument("image", help="The image file to read.")

    parser.add_argument("-s", "--stroke", dest="stroke", type=str, nargs="?",
                        default=False,
                        help="Stroke the polygons instead of colouring them. \
                        Takes either a width, 'perimeter' or 'pixels'. \
                        Default is 1.")

    parser.add_argument("-f", "--scale-factor", dest="scale", type=float,
                        default=1,
                        help="A scale factor for the polygon scan area. \
                        Values > 1 will scan a larger area, values < 1 will \
                        scan a smaller area. Default is 1.")

    parser.add_argument("-r", "--resize", dest="resize", action="store_const",
                        const=True, default=False, help="Resize the output \
                        polygons to match the scan area.")

    parser.add_argument("-o", "--output", dest="output", type=str,
                        help="Specify an output file. The default is the \
                        input file + '- colourized'.")

    parser.add_argument("-O", "--overwrite", dest="overwrite",
                        action="store_const", const=True, default=False,
                        help="Overwrite the input svg.")

    args = parser.parse_args()

    if args.output and args.override:
        parser.error(
            "Cannot specify an output file and override the original."
        )

    if args.resize and args.scale == 1:
        parser.error(
            "Resizing the polygons will have no effect if they are not scaled."
        )

    if args.scale < 0:
        parser.error("Scale cannot be less than 0.")

    return parser.parse_args()
