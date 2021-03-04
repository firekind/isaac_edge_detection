import argparse

from isaac import Application

from codelets import EdgeDetector


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--simulate",
        action="store_true",
        help="uses issac sim unity3d instead of a v4l2 camera.",
    )
    args = parser.parse_args()

    if args.simulate:
        app_file = "apps/isaac_edge_detection/graphs/edge_detection_unity3d.app.json"
    else:
        app_file = "apps/isaac_edge_detection/graphs/edge_detection.app.json"

    app = Application(app_filename=app_file)
    app.nodes["edge_detector"].add(EdgeDetector, "detector")
    app.run()


if __name__ == "__main__":
    main()
