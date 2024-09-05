# PyPMML-Spark

_PyPMML-Spark_ is a Python PMML scoring library for PySpark as SparkML Transformer, it really is the Python API for [PMML4S-Spark](https://github.com/autodeployai/pmml4s-spark).

## Prerequisites
 - Java >= 1.8
 - Python 2.7 or >= 3.5

## Dependencies
Module                    | PySpark
------------------------- | ----------------------
[pypmml-spark](https://github.com/autodeployai/pypmml-spark/tree/master)              | PySpark >= 3.0.0
[pypmml-spark2](https://github.com/autodeployai/pypmml-spark/tree/spark-2.x)          | PySpark >= 2.4.0, < 3.0.0
  
## Installation

```bash
pip install pypmml-spark
```

Or install the latest version from github:

```bash
pip install --upgrade git+https://github.com/autodeployai/pypmml-spark.git
```

After that, you need to do more to use it in Spark that must know those jars in the package `pypmml_spark.jars`. There are several ways to do that:

1. The easiest way is to run the script `link_pmml4s_jars_into_spark.py` that is delivered with `pypmml-spark`:

    ```bash
    link_pmml4s_jars_into_spark.py
    ```
    
2. Use those config options to specify dependent jars properly. e.g. `--jars`, or `spark.executor.extraClassPath` and `spark.executor.extraClassPath`. See [Spark](http://spark.apache.org/docs/latest/configuration.html) for details about those parameters.

## Usage

1. Load model from various sources, e.g. filename, string, or array of bytes.

    ```python
    from pypmml_spark import ScoreModel
    
    # The model is from http://dmg.org/pmml/pmml_examples/KNIME_PMML_4.1_Examples/single_iris_dectree.xml
    model = ScoreModel.fromFile('single_iris_dectree.xml')
    ```

2. Call `transform(dataset)` to run a batch score against an input dataset.

    ```python
    # The data is from http://dmg.org/pmml/pmml_examples/Iris.csv
    df = spark.read.csv('Iris.csv', header='true')
    score_df = model.transform(df)
    ```

## Use PMML in Scala or Java
See the [PMML4S](https://github.com/autodeployai/pmml4s) project. _PMML4S_ is a PMML scoring library for Scala. It provides both Scala and Java Evaluator API for PMML.

## Use PMML in Python
See the [PyPMML](https://github.com/autodeployai/pypmml) project. _PyPMML_ is a Python PMML scoring library, it really is the Python API for PMML4S.

## Use PMML in Spark
See the [PMML4S-Spark](https://github.com/autodeployai/pmml4s-spark) project. _PMML4S-Spark_ is a PMML scoring library for Spark as SparkML Transformer.

## Deploy PMML as REST API
See the [AI-Serving](https://github.com/autodeployai/ai-serving) project. _AI-Serving_ is serving AI/ML models in the open standard formats PMML and ONNX with both HTTP (REST API) and gRPC endpoints.

## Deploy and Manage AI/ML models at scale
See the [DaaS](https://www.autodeployai.com/) system that deploys AI/ML models in production at scale on Kubernetes.

## Support
If you have any questions about the _PyPMML-Spark_ library, please open issues on this repository.

Feedback and contributions to the project, no matter what kind, are always very welcome. 

## License
_PyPMML-Spark_ is licensed under [APL 2.0](http://www.apache.org/licenses/LICENSE-2.0).
