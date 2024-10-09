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

import unittest
from unittest import TestCase
import os

from pyspark.sql import SparkSession, SQLContext
from pypmml_spark import ScoreModel


class ModelTestCase(TestCase):

    jars_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../jars')
    jars = []
    for x in os.listdir(jars_path):
        jars.append(os.path.join(jars_path, x))
    spark = SparkSession.builder.config('spark.jars', ','.join(jars)).getOrCreate()
    sc = spark.sparkContext

    def test_from_string(self):
        df = SQLContext(self.sc).read.csv('./resources/data/Iris.csv', header='true', inferSchema='true')
        df.show()

        with open('./resources/models/single_iris_dectree.xml', 'r') as f:
            s = f.read()
        model = ScoreModel.fromString(s)
        out_df = model.transform(df)
        out_df.show()
        self.assertTrue(len(out_df.schema) == 11)
        self.assertTrue(out_df.schema['predicted_class'])

    def test_from_file(self):
        df = SQLContext(self.sc).read.csv('./resources/data/Iris.csv', header='true', inferSchema='true')
        df.show()

        model = ScoreModel.fromFile('./resources/models/single_iris_dectree.xml').setPredictionCol('prediction')
        out_df = model.transform(df)
        out_df.show()
        self.assertTrue(len(out_df.schema) == 11)
        self.assertTrue(out_df.schema['prediction'])

    def test_from_bytes_array(self):
        df = SQLContext(self.sc).read.csv('./resources/data/Iris.csv', header='true', inferSchema='true')
        df.show()

        with open('./resources/models/single_iris_dectree.xml', 'rb') as f:
            byte_array = f.read()

        model = ScoreModel.fromBytes(byte_array).setPrependInputs(False)
        out_df = model.transform(df)
        out_df.show()
        self.assertTrue(len(out_df.schema) == 6)
        self.assertTrue(out_df.schema['predicted_class'])


if __name__ == "__main__":
    unittest.main()
