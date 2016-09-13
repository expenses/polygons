import os
import polygons

stroke = False
args = polygons.setup_args()

svg, image = args.files

if args.output:
    output = args.output
elif args.override:
    output = svg
else:
    output = "- colourized".join(os.path.splitext(svg))

if args.stroke is None:
    stroke = True
elif args.stroke is not False:
    stroke = args.stroke

polygons.colour(svg, image, output, stroke=stroke)
