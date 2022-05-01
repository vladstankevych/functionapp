"""Tests utilities for spark."""

import tempfile
import logging
import uuid
from typing import List
from datetime import datetime

from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable

from pandas._typing import FilePath
from pyspark.sql import DataFrame, SparkSession, Row
from pyspark.sql import functions as sf
from pyspark.sql.types import BooleanType, TimestampType

def get_spark_session() -> SparkSession:
    """Gets the :class:`SparkSession` instance. If it doesn't exist it builds a new one."""
    existing = SparkSession.getActiveSession()  # on Databricks a session is always already running
    if existing:
        return existing
    else:
        # outside of Databricks the session needs to be created on first invocation
        logging.warning("Could not find an existing Spark session. Creating a new one...")
        builder = (
            SparkSession.builder.appName("CPFR-Spark-Session")
            .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            #.config("spark.jars.packages", "io.delta:delta-core_2.12:0.8.0")
            .config(
                "spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"
            )
        )
        new_session = configure_spark_with_delta_pip(builder).getOrCreate()
        return new_session

data = [
    Row(column1="A", column2=1, column3=True, column4=1.1),
    Row(column1="B", column2=2, column3=False, column4=2.2),
    Row(column1="C", column2=3, column3=None, column4=3.3),
    Row(column1="D", column2=4, column3=True, column4=4.4),
]
primary_key_columns = ["column1", "column2"]

def test_tracking_change_in_two_row():
    """Tests when a single row has changed."""
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame(data)

    type(df)
    
    #df = spark.range(10000000).withColumn("example_data", sf.rand(seed=42) * 3)
    #df.write.mode("overwrite").format("delta").saveAsTable("example_table")
    #new_df = spark.table("example_table")
    assert "A" in df.schema.fieldNames()

#def test_tracking_change_in_three_row():
#    """Tests when a single row has changed."""
#    spark = get_spark_session()
#    
#    df = spark.range(10000000).withColumn("example_data1", sf.rand(seed=42) * 3)
#
#    df.write.mode("overwrite").format("delta").saveAsTable("example_table1")
#
#    new_df = spark.table("example_table1")
#    assert "example_data1" in new_df.schema.fieldNames()

#def test_tracking_change_in_four_row():
#    """Tests when a single row has changed."""
#    spark = get_spark_session()
#    
#    df = spark.range(10000000).withColumn("example_data2", sf.rand(seed=42) * 3)
#
#    df.write.mode("overwrite").format("delta").saveAsTable("example_table2")
#
#    new_df = spark.table("example_table2")
#    assert "example_data2" in new_df.schema.fieldNames()
#
#def test_tracking_change_in_five_row():
#    """Tests when a single row has changed."""
#    spark = get_spark_session()
#    
#    df = spark.range(10000000).withColumn("example_data3", sf.rand(seed=42) * 3)
#
#    df.write.mode("overwrite").format("delta").saveAsTable("example_table3")
#
#    new_df = spark.table("example_table3")
#    assert "example_data3" in new_df.schema.fieldNames()