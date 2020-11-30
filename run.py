import argparse
import tempfile
import os
import platform
import shutil
import json
import textwrap


def run(cmd, ignore_errors=False):
    retcode = os.system(cmd)
    if retcode != 0 and not ignore_errors:
        raise Exception("Command failed: %s" % cmd)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', help='package size in gigabytes', default="3")
    parser.add_argument('--conan_remote', help='name for the conan remote', required=True)
    parser.add_argument('--repetitions', help='number of times to repeat the process', default="2", type=int)
    args = parser.parse_args()
    for x in range(args.repetitions):
        create_package = "conan create . -o file_size={}".format(args.size)
        upload_package = "conan upload large_package -r={} --all --confirm".format(args.conan_remote)
        remove_package = "conan remove large_package -f"
        download_package = "conan install large_package/1.4@ -r={}".format(args.conan_remote)
        run(create_package)
        run(upload_package)
        run(remove_package)
        run(download_package)
        run(remove_package)
