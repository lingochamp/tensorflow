"""This script replaces any internal visibility with //visibility:public."""

from subprocess import call
import glob
import os
import os.path
import re

def _build_files(workspace_dir):
    """Return all BUILD files under the workspace dir.

    This excludes symbolic links.
    """
    build_files = []
    for file in glob.glob(workspace_dir + "/**/BUILD", recursive=True):
        # Glob will follow symbolic links, which creates a lot of trouble.
        # Exclude files that are not within the current workspace dir.
        if not file.startswith(workspace_dir):
            continue
        if file.startswith(os.path.join(workspace_dir, "bazel-")):
            continue
        build_files.append(file)
    return build_files

if __name__ == "__main__":
    workspace_dir = os.getcwd()
    while not os.path.exists(os.path.join(workspace_dir, "WORKSPACE")):
        workspace_dir = os.path.dirname(workspace_dir)
    if workspace_dir == "/":
        print("Script must be called within Bazel workspace.")
        exit(1)
    print("Workspace is ", os.path.join(workspace_dir, "WORKSPACE"))

    build_files = _build_files(workspace_dir)

    reg = re.compile("visibility = \[.*?\]", re.DOTALL)
    # Call buildifier on all BUILD files.
    # REQUIRES: /usr/local/bin/buildifier presents.
    for file in build_files:
        print("check", file)
        # Read in the file
        with open(file, "r") as f :
            data = f.read()
        # Replace the target string
        data = reg.sub("visibility = [\"//visibility:public\"]", data)
        # Write the file out again
        with open(file, "w") as f:
            f.write(data)
        call(["/usr/local/bin/buildifier", "-v", "--mode=fix", file])
