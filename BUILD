load("//bzl:py.bzl", "isaac_py_app")

isaac_py_app(
    name = "edge_detection",
    srcs = glob(["codelets/*"]) + ["main.py"],
    data = [
        "graphs/edge_detection.app.json",
        "graphs/edge_detection_unity3d.app.json",
        "//packages/navsim/apps:navsim_navigation_subgraph",
    ],
    main = "main.py",
    modules = [
        "sight",
        "viewers",
        "sensors:v4l2_camera",
    ],
    deps = ["//packages/pyalice"],
)
