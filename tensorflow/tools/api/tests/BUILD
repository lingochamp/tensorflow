# TensorFlow API backwards compatibility tests.

package(
    default_visibility = ["//visibility:public"],
)

licenses(["notice"])  # Apache 2.0

exports_files([
    "README.txt",
    "API_UPDATE_WARNING.txt",
])

py_test(
    name = "api_compatibility_test",
    srcs = ["api_compatibility_test.py"],
    data = [
        "//tensorflow/tools/api/golden:api_golden",
        "//tensorflow/tools/api/tests:API_UPDATE_WARNING.txt",
        "//tensorflow/tools/api/tests:README.txt",
    ],
    srcs_version = "PY2AND3",
    deps = [
        "//tensorflow:tensorflow_py",
        "//tensorflow/python:platform",
        "//tensorflow/tools/api/lib:python_object_to_proto_visitor",
        "//tensorflow/tools/common:public_api",
        "//tensorflow/tools/common:traverse",
        "@com_github_google_protobuf//:protobuf_python",
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
