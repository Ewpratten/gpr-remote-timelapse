import sys
import os
import argparse
from datetime import datetime
from goprocam import GoProCamera, constants
import logging


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--camera-model",
                    help="GoPro camera model", default="HERO3")
    ap.add_argument("--output-dir", "-o", help="Output directory for the photo", required=True)
    args = ap.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Attach to the camera over the network
    logging.info("Connecting to camera")
    camera = GoProCamera.GoPro(camera=args.camera_model)

    # Take a photo
    logging.info("Taking photo")
    file_path = camera.take_photo(1)
    file_path = file_path.replace("10.5.5.9", "10.5.5.9:8080")
    logging.info("Photo taken and saved at: %s", file_path)

    # Move the photo locally
    logging.info("Downloading photo from camera")
    camera.downloadLastMedia(file_path, os.path.join(args.output_dir, "gpr_photo_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"))


    return 0


if __name__ == '__main__':
    sys.exit(main())
