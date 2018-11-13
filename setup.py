from setuptools import setup, find_packages

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Topic :: Software Development",
    "Topic :: Scientific/Engineering",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Unix",
    "Operating System :: MacOS",
    "Topic :: Scientific/Engineering :: Mathematics",
    "Topic :: Software Development :: Libraries :: Python Modules"]

MAJOR = "1"
MINOR = "0"
PATCH = "0"
VERSION = "{0}.{1}.{2}".format(MAJOR, MINOR, PATCH)

def write_version_py(filename='cromosim/version.py'):
    a = open(filename, 'w')
    try:
        a.write("version = '{}'".format(VERSION))
    finally:
        a.close()

README = open("README.rst").readlines()

write_version_py()

setup(
    name           = "cromosim",
    version        = VERSION,
    description    = README[0],
    long_description = "".join(README[1:]),
    author         = "Sylvain Faure, Bertrand Maury",
    author_email   = "sylvain.faure@math.u-psud.fr, bertrand.maury@math.u-psud.fr",
    url            = "http://www.cromosim.fr",
    license        = "GPL",
    keywords       = "Crowd Motion Simulator",
    classifiers    = CLASSIFIERS,
    #packages       = find_packages(exclude=['demo', 'doc', 'tests*']),
    packages       = ["cromosim"],
    include_package_data=True,
    install_requires=[
                      'scipy>=0.19.1',
                      'Pillow>=1.1.7',
                      'scikit-fmm>=0.0.9',
                      'matplotlib>=2.1.1',
                      'numpydoc>=0.7.0',
                      'sphinx>=1.6.3'
                      ],
    #dependency_links=[
    #    "hg+https://bitbucket.org/pauloh/pyevtk"
    #],
    #extras_require={'pythran': ["pythran>=0.7.1"],
    #                'numba': ["numba>=0.19.1"]
    #                },
)