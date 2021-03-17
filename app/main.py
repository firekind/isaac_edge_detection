import argparse

from isaac import Application

from codelets import EdgeDetector
from utils import configure_websight_root, patch_capnp_paths


def main():
    patch_capnp_paths()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="uses issac sim unity3d instead of a v4l2 camera.",
    )
    args = parser.parse_args()

    if args.simulate:
        app_file = "app/graphs/edge_detection_unity3d.app.json"
    else:
        app_file = "app/graphs/edge_detection.app.json"

    # creating app
    app = Application(app_filename=app_file)

    # adding EdgeDetector codelet to the detector component of the edge_detector node
    app.nodes["edge_detector"].add(EdgeDetector, "detector")
    configure_websight_root(app)

    # running the application
    app.run()


if __name__ == "__main__":
    main()
