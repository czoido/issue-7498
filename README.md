## Trying to reproduce [large packages download issue with Artifactory](https://github.com/conan-io/conan/issues/7498)

This python script will create a package with a big library and upload and download from Artifactory
several times. Although it is using Conan for the whole process this issue is known not happen also
[when downloading packages directly with
curl](https://github.com/conan-io/conan/issues/7498#issuecomment-679306767).

The number of times that the create, upload and download cycle is repeated is configurable via the
`--repetitions` parameter (will do 10 repetitions if not specified). Also, the size in gigabytes
(aproximately) of the library can be configured with the `--size` parameter (3 gigabytes by default).
The   `--conan_remote` argument is required.

```bash
python3 run.py --size=<size-in-gigabytes> --conan_remote=<conan-remote> --repetitions=<number-or-repetitions>
```

```bash
usage: run.py [-h] [--size SIZE] --conan_remote CONAN_REMOTE
              [--repetitions REPETITIONS]

optional arguments:
  -h, --help            show this help message and exit
  --size SIZE           package size in gigabytes
  --conan_remote CONAN_REMOTE
                        name for the conan remote
  --repetitions REPETITIONS
```