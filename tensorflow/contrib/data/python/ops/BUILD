package(default_visibility = ["//visibility:public"])

licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

py_library(
    name = "dataset_ops",
    srcs = ["dataset_ops.py"],
    srcs_version = "PY2AND3",
    deps = [
        "//tensorflow/contrib/data/python/framework:function",
        "//tensorflow/contrib/util:util_py",
        "//tensorflow/python:dataset_ops_gen",
        "//tensorflow/python:framework",
        "//tensorflow/python:parsing_ops",
        "//tensorflow/python:util",
    ],
)

filegroup(
    name = "all_files",
    srcs = glob(
        ["**/*"],
        exclude = [
            "**/METADATA",
            "**/OWNERS",
        ],
    ),
    visibility = ["//visibility:public"],
)
