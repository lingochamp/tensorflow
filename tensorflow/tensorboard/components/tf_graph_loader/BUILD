package(default_visibility = ["//visibility:public"])

load("//tensorflow/tensorboard:defs.bzl", "tensorboard_webcomponent_library")
load("//tensorflow/tensorboard:web.bzl", "ts_web_library")

licenses(["notice"])  # Apache 2.0

ts_web_library(
    name = "tf_graph_loader",
    srcs = ["tf-graph-loader.html"],
    path = "/tf-graph-loader",
    deps = [
        "//tensorflow/tensorboard/components/tf_graph_common",
        "//tensorflow/tensorboard/components/tf_imports:polymer",
    ],
)

tensorboard_webcomponent_library(
    name = "legacy",
    srcs = [":tf_graph_loader"],
    destdir = "tf-graph-loader",
    deps = [
        "//tensorflow/tensorboard/components/tf_graph_common:legacy",
        "//third_party/javascript/polymer/v1/polymer:lib",
    ],
)

filegroup(
    name = "all_files",
    srcs = glob(["**"]),
    tags = ["notsan"],
)
