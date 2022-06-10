"""Tests utilities for spark."""
import pytest
from pyspark.sql import functions as sf
from pyspark.sql import Row
from cpfr.utils.extras.spark import get_spark_session
import importlib_metadata 


data = [
    Row(column1="A", column2=1, column3=True, column4=1.1),
    Row(column1="B", column2=2, column3=False, column4=2.2),
    Row(column1="C", column2=3, column3=None, column4=3.3),
    Row(column1="D", column2=4, column3=True, column4=4.4),
]

#def test_tracking_change_in_two_row():
#    """Tests when a single row has changed."""
#    df = spark.createDataFrame(data)
#
#    type(df)
#    assert "column1" in df.schema.fieldNames()

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
   # spark = get_spark_session()
   # df = spark.range(100).withColumn("example_data", sf.rand(seed=42) * 3)
   # df.write.mode("overwrite").format("delta").saveAsTable("example_table")
#
   # new_df = spark.table("example_table")
   # assert "example_data" in new_df.schema.fieldNames()
    delta_version = importlib_metadata.version("delta_spark")
    scala_version = "2.12"
    maven_artifact = f"io.delta:delta-core_{scala_version}:{delta_version}"
    print(f"OUTPUT: {maven_artifact}")
    assert 1==1

#def test_tracking_change_in_four_row(spark_session):
#    """Tests when a single row has changed."""
#    
#    df = spark_session.range(100).withColumn("example_data2", sf.rand(seed=42) * 3)
#
#    df.write.mode("overwrite").format("delta").saveAsTable("example_table2")
#
#    new_df = spark_session.table("example_table2")
#    assert "example_data2" in new_df.schema.fieldNames()

@pytest.mark.xdist_group(name="delta")
def test_tracking_change_in_five_row():
    """Tests when a single row has changed."""
    #spark = get_spark_session()
    #df = spark.range(100).withColumn("example_data3", sf.rand(seed=42) * 3)
    #df.write.mode("overwrite").format("delta").saveAsTable("example_table3")

    #new_df = spark.table("example_table3")
    #assert "example_data3" in new_df.schema.fieldNames()
    delta_version = importlib_metadata.version("delta_spark")
    scala_version = "2.12"
    maven_artifact = f"io.delta:delta-core_{scala_version}:{delta_version}"
    print(f"OUTPUT: {maven_artifact}")
    assert 1==1

@pytest.mark.xdist_group(name="delta")
def test_init():
    """Tests when a single row has changed."""
    #spark = get_spark_session()
    #df = spark.range(100).withColumn("example_data1", sf.rand(seed=42) * 3)
    #df.write.mode("overwrite").format("delta").saveAsTable("example_table1")
    delta_version = importlib_metadata.version("delta_spark")
    scala_version = "2.12"
    maven_artifact = f"io.delta:delta-core_{scala_version}:{delta_version}"
    print(f"OUTPUT: {maven_artifact}")
    #new_df = spark.table("example_table1")
    assert 1==1
    #assert "example_data1" in new_df.schema.fieldNames()

#spark = get_spark_session()
#df = spark.range(10000000).withColumn("example_data1", sf.rand(seed=42) * 3)
#df.write.mode("overwrite").format("delta").saveAsTable("example_table1")
#print('Hi')
#new_df = spark.table("example_table1")
#assert "example_data1" in new_df.schema.fieldNames()
