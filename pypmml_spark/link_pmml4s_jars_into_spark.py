#!/usr/bin/env python

#
# Copyright (c) 2017-2019 AutoDeploy AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from __future__ import print_function
import os
import sys


def _find_spark_home():
    """Find the SPARK_HOME.
    This function is borrowed from PySpark distribution
    """
    # If the environment has SPARK_HOME set trust it.
    if "SPARK_HOME" in os.environ:
        return os.environ["SPARK_HOME"]

    def is_spark_home(path):
        """Takes a path and returns true if the provided path could be a reasonable SPARK_HOME"""
        return (os.path.isfile(os.path.join(path, "bin/spark-submit")) and
                (os.path.isdir(os.path.join(path, "jars")) or
                 os.path.isdir(os.path.join(path, "assembly"))))

    paths = ["../", os.path.dirname(os.path.realpath(__file__))]

    # Add the path of the PySpark module if it exists
    if sys.version < "3":
        import imp
        try:
            module_home = imp.find_module("pyspark")[1]
            paths.append(module_home)
            # If we are installed in edit mode also look two dirs up
            paths.append(os.path.join(module_home, "../../"))
        except ImportError:
            # Not pip installed no worries
            pass
    else:
        from importlib.util import find_spec
        try:
            module_home = os.path.dirname(find_spec("pyspark").origin)
            paths.append(module_home)
            # If we are installed in edit mode also look two dirs up
            paths.append(os.path.join(module_home, "../../"))
        except ImportError:
            # Not pip installed no worries
            pass

    # Normalize the paths
    paths = [os.path.abspath(p) for p in paths]

    try:
        return next(path for path in paths if is_spark_home(path))
    except StopIteration:
        print("Could not find valid SPARK_HOME while searching {0}".format(paths), file=sys.stderr)
        sys.exit(-1)


def _find_pypmml_spark_home():
    """Find the PyPMML-Spark home
    """
    module_home = None
    if sys.version < "3":
        import imp
        try:
            module_home = imp.find_module("pypmml_spark")[1]
        except ImportError:
            # Not pip installed no worries
            pass
    else:
        from importlib.util import find_spec
        try:
            module_home = os.path.dirname(find_spec("pypmml_spark").origin)
        except ImportError:
            # Not pip installed no worries
            pass

    if module_home is None:
        print("Could not find pypmml_spark, are you sure it installed?", file=sys.stderr)
        sys.exit(-1)

    return module_home


def _link_jars():
    spark_home = _find_spark_home()
    pypmml_spark_home = _find_pypmml_spark_home()

    pypmml_spark_home_jars = os.path.join(pypmml_spark_home, "jars")
    spark_home_jars = os.path.join(spark_home, "jars")

    if not os.path.exists(spark_home_jars):
        print("Could not find jars directory in SPARK_HOME.", file=sys.stderr)
        sys.exit(-1)

    # Check if there are old soft links of both jars: pmml4s and pmml4s-spark
    old_links = []
    for jar in os.listdir(spark_home_jars):
        if jar.startswith("pmml4s_") or jar.startswith("pmml4s-spark_"):
            if os.path.islink(os.path.join(spark_home_jars, jar)):
                old_links.append(jar)
                os.remove(os.path.join(spark_home_jars, jar))

    jars = []
    for jar in os.listdir(pypmml_spark_home_jars):
        if jar.endswith(".jar"):
            if not os.path.exists(os.path.join(spark_home_jars, jar)):
                os.symlink(os.path.join(pypmml_spark_home_jars, jar), os.path.join(spark_home_jars, jar))
            jars.append(jar)

    if old_links:
        print("Totally {0} jars are linked into Spark with {1} jar(s) unlinked successfully.".format(
            len(jars), len(old_links)))
    else:
        print("Totally {0} jars are linked into Spark successfully.".format(len(jars)))


if __name__ == "__main__":
    _link_jars()

