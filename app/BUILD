load("@com_nvidia_isaac_sdk//bzl:py.bzl", "isaac_py_app")

filegroup(
    name = "codelets",
    srcs = glob(["codelets/*"]),
)

filegroup(
    name = "utils",
    srcs = glob(["utils/*"]),
)

filegroup(
    name = "graphs",
    srcs = glob(["graphs/*"]),
)

isaac_py_app(
    name = "edge_detection",
    srcs = [
        "main.py",
        ":codelets",
        ":utils",
    ],
    data = [
        ":graphs",
        "@com_nvidia_isaac_sdk//packages/navsim/apps:navsim_navigation_subgraph",
    ],
    main = "main.py",
    modules = [
        "@com_nvidia_isaac_sdk//packages/sight",
        "@com_nvidia_isaac_sdk//packages/viewers",
        "@com_nvidia_isaac_sdk//packages/sensors:v4l2_camera",
    ],
    deps = ["@com_nvidia_isaac_sdk//packages/pyalice"],
)
