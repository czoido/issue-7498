from conans import ConanFile, CMake
import os
import random
import string

def _create_bigfile(name, size):
    with open(name, 'wb') as bigfile:
        for i in range(size):
            bigfile.write(os.urandom(1024))
        bigfile.close()

class LargePackageConan(ConanFile):
    name = "large_package"
    version = "1.4"
    settings = "os", "compiler", "build_type", "arch"
    options = {"file_size": "ANY"}
    default_options = {"file_size": "3"}
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        _create_bigfile("large_library.lib", int(self.options.file_size)*1024*1024)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["large_package"]
