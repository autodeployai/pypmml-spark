from setuptools import setup
import os

VERSION_PATH = os.path.join("pypmml_spark", "version.py")
exec(open(VERSION_PATH).read())

VERSION = __version__ # noqa

with open("README.md", "r") as fh:
    long_description = fh.read()

scripts = ["pypmml_spark/link_pmml4s_jars_into_spark.py"]

setup(
    name="pypmml-spark",
    version=VERSION,
    description="Python PMML scoring library for PySpark as SparkML Transformer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["pypmml_spark", "pypmml_spark.jars"],
    package_data={
        "pypmml_spark.jars": ["*.jar"]
    },
    # include_package_data=True,
    install_requires=["pyspark>=3.0.0"],
    scripts=scripts,
    url="https://github.com/autodeployai/pypmml-spark",
    download_url="https://github.com/autodeployai/pypmml-spark/archive/v" + VERSION + ".tar.gz",
    author="AutoDeployAI",
    author_email="autodeploy.ai@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
