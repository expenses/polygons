import argparse


def setup_args():
    parser = argparse.ArgumentParser(
        description="A cli tool for colouring svg meshes")

    parser.add_argument("files", nargs="*",
                        help="The input svg and image files.")

    parser.add_argument("-s", "--stroke", dest="stroke", type=str, nargs="?",
                        default=False,
                        help="The width of the strokes. Default is 1.")

    parser.add_argument("-o", "--output", dest="output", type=str,
                        help="Specify an output file.")

    parser.add_argument("-O", "--override", dest="override",
                        action="store_const", const=True, default=False,
                        help="Override the input svg.")

    args = parser.parse_args()

    if args.output and args.override:
        parser.error(
            "Cannot specify an output file and override the original."
        )

    if len(args.files) > 2 or len(args.files) == 1:
        parser.error("Must input 2 or 0 (for testing) files.")

    return parser.parse_args()
