# Description: SavedModel half plus two example.

package(
    default_visibility = ["//visibility:public"],
    features = [
        "-layering_check",
    ],
)

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
            "g3doc/sitemap.md",
        ],
    ),
    visibility = ["//visibility:public"],
)

py_binary(
    name = "saved_model_half_plus_two",
    srcs = [
        "saved_model_half_plus_two.py",
    ],
    srcs_version = "PY2AND3",
    deps = [
        "//tensorflow:tensorflow_py",
    ],
)
