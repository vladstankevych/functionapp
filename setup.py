"""Install this Python package."""

import os.path
import re
from pathlib import Path
from urllib.parse import urlparse

from setuptools import find_namespace_packages, setup


class Setup:
    """Convenience wrapper (for C.I. purposes) of the `setup()` call form `setuptools`.

    It automatically fills some of the most obnoxious variables that normally need to be repeated
    multiple times in several places (for instance, the `README.md` and the `MANIFEST.in`).
    """

    def __init__(self, **kw):
        """Initialize attributes for packaging."""
        self.conf = kw
        self.work_dir = os.path.abspath(os.path.dirname(__file__))

        # Automatically fill `package_data` from `MANIFEST.in`. No need to repeat lists twice
        assert "package_data" not in self.conf
        assert "include_package_data" not in self.conf
        package_data = {}
        try:
            with open(os.path.join(self.work_dir, "MANIFEST.in")) as fp:
                for line in fp.readlines():
                    line = line.strip()
                    m = re.search(r"include\s+(.+)/([^/]+)", line)
                    assert m
                    module = m.group(1).replace("/", ".")
                    file_name = m.group(2)
                    if module not in package_data:
                        package_data[module] = []
                    package_data[module].append(file_name)
        except FileNotFoundError:
            pass
        if package_data:
            self.conf["include_package_data"] = True
            self.conf["package_data"] = package_data

        # Automatically fill the long description from `README.md`. Filter out lines that look like
        # "badges". See https://dustingram.com/articles/2018/03/16/markdown-descriptions-on-pypi
        assert "long_description" not in self.conf
        assert "long_description_content_type" not in self.conf
        try:
            with open(os.path.join(self.work_dir, "README.md")) as fp:
                ld = "\n".join([line for line in fp if not line.startswith("[![")])
            self.conf["long_description"] = ld
            self.conf["long_description_content_type"] = "text/markdown"
        except FileNotFoundError:
            pass

        # Automatically fill the dependency list through the various requirements files
        self.load_deps()
        for p in Path.cwd().glob("requirements-*.txt"):
            self.load_deps(p.name[13:-4])

        # Automatically register entry points to CPFR plugin system!
        self.conf["entry_points"] = {
            "cpfr.version": ["utils = cpfr.utils.version:__version__"],
            "cpfr.job": ["utils = cpfr.utils.job.all"],
            "cpfr.model": ["utils = cpfr.utils.model.all"],
            "cpfr.cli": ["utils = cpfr.utils.cli_app"],
        }

        # Everything under src should be looked for
        self.conf["package_dir"] = {"": "src"}
        self.conf["packages"] = find_namespace_packages(where="src")

    def load_deps(self, req=None):
        """Load dependencies from files formatted like `requirements.txt`.

        If `req` is omitted, load `requirements.txt` as list of standard dependencies. If `req` is
        provided, load from `requirements-<req>.txt` and make it possible for those extra deps to be
        installed when doing `pip install '<package>[<req>]'`.
        """
        suffix = f"-{req}" if req else ""
        with open(f"requirements{suffix}.txt") as fp:
            deps = [y for y in (x.strip() for x in fp) if y]
        # Detect if we have Git URLs in the list and change them accordingly
        for idx, dep in enumerate(deps):
            udep = urlparse(dep)
            if udep.scheme.startswith("git+") and udep.fragment.startswith("egg="):
                egg = udep.fragment.split("=", 1)[1]
                deps[idx] = f"{egg} @ {dep}"
        if req:
            if "extras_require" not in self.conf:
                self.conf["extras_require"] = {}
            self.conf["extras_require"][req] = deps
        else:
            self.conf["install_requires"] = deps

    def __str__(self):
        """Return a stringified version of the current configuration."""
        return str(self.conf)

    def __call__(self):
        """Run the setup when calling the class instance as if it were a function."""
        setup(**self.conf)


SETUP = Setup(
    name="pg-ds-cf-cpfr-utils",
    use_scm_version=True,
    description="Library of reusable models and utilities for CPFR projects",
    url="https://github.com/procter-gamble/ds-cf-cpfr-utils",
    author="Anatoly Makarevich",
    author_email="makarevich.as@pg.com",
    license="Proprietary",
    classifiers=[
        # See https://pypi.org/classifiers/
        f"Programming Language :: Python :: 3.8",
        f"Programming Language :: Python :: 3.9",
    ],
    keywords="P&G Procter&Gamble D&A Data&Analytics CPFR Utils DS DE AIE",
    python_requires=">=3.8.*",
    setup_requires=[
        "setuptools_scm>=3.3.1",
    ],
)

if __name__ == "__main__":
    SETUP()
