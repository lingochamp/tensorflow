licenses(["notice"])  # Apache 2.0

exports_files(["LICENSE"])

package(default_visibility = ["//visibility:public"])

py_library(
    name = "tfprof",
    srcs = [
        "__init__.py",
    ],
    srcs_version = "PY2AND3",
    visibility = ["//visibility:public"],
    deps = [
        "//tensorflow/contrib/tfprof/python/tools/tfprof:model_analyzer",
        "//tensorflow/contrib/tfprof/python/tools/tfprof:tfprof_logger",
        "//tensorflow/python:util",
    ],
)
