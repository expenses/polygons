import os
import polygons

args = polygons.setup_args()

svg, image = args.files

output = (args.output if args.output
          else svg if args.override
          else "- colourized".join(os.path.splitext(svg)))

stroke = (True if args.stroke is None
          else args.stroke if args.stroke is not False
          else False)

polygons.colour(svg, image, output, stroke=stroke)
