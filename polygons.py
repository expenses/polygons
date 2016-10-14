import os
import polygons

args = polygons.setup_args()

output = (args.output if args.output
          else args.svg if args.overwrite
          else " - colourized".join(os.path.splitext(args.svg)))

stroke = (True if args.stroke is None
          else args.stroke if args.stroke is not False
          else False)

polygons.colour(args.svg, args.image, output,
                stroke=stroke, scale=args.scale, resize=args.resize)
