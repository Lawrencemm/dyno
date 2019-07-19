#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile


class DynoConan(ConanFile):
    name = "dyno"
    version = "0.1"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["include/*"]
    no_copy_source = True
    requires = (
        'boost_callable_traits/1.69.0@bincrafters/stable',
        'boost_hana/1.69.0@bincrafters/stable',
    )

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses")
        self.copy(pattern="*", dst="include", src="include", keep_path=True)

    def package_id(self):
        self.info.header_only()
