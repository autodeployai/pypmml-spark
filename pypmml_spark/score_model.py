#
# Copyright (c) 2017-2022 AutoDeploy AI
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

from pyspark.ml.wrapper import JavaTransformer
from pyspark.ml.util import _jvm
from pyspark.ml.param import *


class ScoreModel(JavaTransformer):
    """
    Model restored from PMML.
    """
    predictionCol = Param(Params._dummy(), "predictionCol", "prediction column name.",
                          typeConverter=TypeConverters.toString)
    prependInputs = Param(Params._dummy(), "prependInputs", "whether to prepend the input cols to the output data.",
                          typeConverter=TypeConverters.toBoolean)
    supplementOutput = Param(Params._dummy(), "supplementOutput",
                             "whether to return those predefined output fields not exist in the Output element explicitly.",
                             typeConverter=TypeConverters.toBoolean)

    def __init__(self, java_model=None):
        """
        Initialize this instance with a Java model object.
        """
        super(ScoreModel, self).__init__(java_model)
        if java_model is not None:
            self._resetUid(java_model.uid())

    def setPredictionCol(self, value):
        """
        Sets the value of :py:attr:`predictionCol`.
        """
        return self._set(predictionCol=value)

    def getPredictionCol(self):
        """
        Gets the value of predictionCol or its default value.
        """
        return self.getOrDefault(self.predictionCol)

    def setPrependInputs(self, value):
        """
        Sets the value of :py:attr:`prependInputs`.
        """
        return self._set(prependInputs=value)

    def getPrependInputs(self):
        """
        Gets the value of prependInputs or its default value.
        """
        return self.getOrDefault(self.prependInputs)

    def setSupplementOutput(self, value):
        """
        Sets the value of :py:attr:`supplementOutput`.
        """
        return self._set(supplementOutput=value)

    def getSupplementOutput(self):
        """
        Gets the value of supplementOutput or its default value.
        """
        return self.getOrDefault(self.supplementOutput)

    @classmethod
    def fromFile(cls, name):
        """
        Constructs a score model from PMML file with given pathname.
        """
        java_model = _jvm().org.pmml4s.spark.ScoreModel.fromFile(name)
        return cls(java_model)

    @classmethod
    def fromString(cls, s):
        """
        Constructs a score model from PMML in a String.
        """
        java_model = _jvm().org.pmml4s.spark.ScoreModel.fromString(s)
        return cls(java_model)

    @classmethod
    def fromBytes(cls, bytes_array):
        """
        Constructs a score model from PMML in an array of bytes.
        """
        java_model = _jvm().org.pmml4s.spark.ScoreModel.fromBytes(bytes_array)
        return cls(java_model)
