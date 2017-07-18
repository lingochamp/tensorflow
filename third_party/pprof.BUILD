package(
    default_visibility = ["//visibility:public"],
)

licenses(["notice"])  # MIT

load("@patched_com_github_google_protobuf//:protobuf.bzl", "py_proto_library")

exports_files(["pprof/LICENSE"])

py_proto_library(
    name = "pprof_proto_py",
    srcs = ["proto/profile.proto"],
    default_runtime = "@patched_com_github_google_protobuf//:protobuf_python",
    protoc = "@patched_com_github_google_protobuf//:protoc",
    srcs_version = "PY2AND3",
    deps = ["@patched_com_github_google_protobuf//:protobuf_python"],
)
