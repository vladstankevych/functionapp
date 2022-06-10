"""Tests utilities for spark."""
import pytest
from pyspark.sql import functions as sf
from pyspark.sql import Row, SparkSession
from cpfr.utils.extras.spark import get_spark_session
import importlib_metadata 


data = [
    Row(column1="A", column2=1, column3=True, column4=1.1),
    Row(column1="B", column2=2, column3=False, column4=2.2),
    Row(column1="C", column2=3, column3=None, column4=3.3),
    Row(column1="D", column2=4, column3=True, column4=4.4),
]

def test_weird():
    """Tests when a single row has changed."""
    spark = SparkSession.builder.getOrCreate()
    df = spark.crveateDataFrame(data)

    type(df)
    assert "column1" in df.schema.fieldNames()

def test_weird_2():
    """Tests when a single row has changed."""
    spark = SparkSession.builder.getOrCreate()
    df = spark.crveateDataFrame(data)

    type(df)
    assert "column1" in df.schema.fieldNames()

#def test_just_spark():
#    """Tests when a single row has changed."""
#    #df = spark.range(100).withColumn("example_data1", sf.rand(seed=42) * 3)
#    df = spark.createDataFrame(data)
#
#    type(df)
#    assert "column1" in df.schema.fieldNames()

@pytest.mark.xdist_group(name="delta")
def test_tracking_change_in_three_row():
    """Tests when a single row has changed."""
    spark = get_spark_session()
    df = spark.range(100).withColumn("example_data", sf.rand(seed=42) * 3)
    df.write.mode("overwrite").format("delta").saveAsTable("example_table")

    new_df = spark.table("example_table")
    assert "example_data" in new_df.schema.fieldNames()

@pytest.mark.xdist_group(name="delta")
def test_tracking_change_in_four_row():
    """Tests when a single row has changed."""
    spark = get_spark_session()
    df = spark.range(100).withColumn("example_data2", sf.rand(seed=42) * 3)
    df.write.mode("overwrite").format("delta").saveAsTable("example_table2")

    new_df = spark.table("example_table2")
    assert "example_data2" in new_df.schema.fieldNames()

@pytest.mark.xdist_group(name="delta")
def test_tracking_change_in_five_row():
    """Tests when a single row has changed."""
    spark = get_spark_session()
    df = spark.range(100).withColumn("example_data3", sf.rand(seed=42) * 3)
    df.write.mode("overwrite").format("delta").saveAsTable("example_table3")

    new_df = spark.table("example_table3")
    assert "example_data3" in new_df.schema.fieldNames()

@pytest.mark.xdist_group(name="delta")
def test_init():
    """Tests when a single row has changed."""
    spark = get_spark_session()
    df = spark.range(100).withColumn("example_data1", sf.rand(seed=42) * 3)
    df.write.mode("overwrite").format("delta").saveAsTable("example_table1")
    new_df = spark.table("example_table1")
    assert "example_data1" in new_df.schema.fieldNames()
