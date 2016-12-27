from setuptools import setup, Extension


vulkbaremodule = Extension(
    'vulkbare', sources=['vulkbaremodule.c'],
    include_dirs=['includes']
)


setup(
    name="vulkbare",
    version='1.0.0',
    packages=[],
    author="realitix",
    author_email="realitix@gmail.com",
    description="Vulk 3D Engine C utils functions",
    long_description="Vulk 3D Engine C utils functions",
    install_requires=[],
    setup_requires=[],
    tests_require=[],
    include_package_data=True,
    url="http://github.com/realitix/vulk-bare",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="Apache2",
    ext_modules=[vulkbaremodule]
)
