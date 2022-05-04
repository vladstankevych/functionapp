"""Tests utilities for spark."""
from pyspark.sql import functions as sf
from pyspark.sql import Row
from cpfr.utils.extras.spark import get_spark_session


data = [
    Row(column1="A", column2=1, column3=True, column4=1.1),
    Row(column1="B", column2=2, column3=False, column4=2.2),
    Row(column1="C", column2=3, column3=None, column4=3.3),
    Row(column1="D", column2=4, column3=True, column4=4.4),
]

#spark.conf.set("spark.unsafe.sorter.spill.read.ahead.enabled", False)
#spark = SparkSession.builder.getOrCreate()

#def test_tracking_change_in_two_row():
#    """Tests when a single row has changed."""
#    df = spark.createDataFrame(data)
#
#    type(df)
#    assert "column1" in df.schema.fieldNames()

def test_just_spark():
    """Tests when a single row has changed."""
    #df = spark.range(100).withColumn("example_data1", sf.rand(seed=42) * 3)
    spark = get_spark_session()
    df = spark.createDataFrame(data)

    type(df)
    assert "column1" in df.schema.fieldNames()

def test_tracking_change_in_three_row():
    """Tests when a single row has changed."""
    spark = get_spark_session()
    df = spark.range(10000000).withColumn("example_data", sf.rand(seed=42) * 3)
    df.write.mode("overwrite").format("delta").saveAsTable("example_table")

    new_df = spark.table("example_table1")
    assert "example_data1" in new_df.schema.fieldNames()

#def test_tracking_change_in_four_row(spark_session):
#    """Tests when a single row has changed."""
#    
#    df = spark_session.range(100).withColumn("example_data2", sf.rand(seed=42) * 3)
#
#    df.write.mode("overwrite").format("delta").saveAsTable("example_table2")
#
#    new_df = spark_session.table("example_table2")
#    assert "example_data2" in new_df.schema.fieldNames()

def test_tracking_change_in_five_row():
    """Tests when a single row has changed."""
    spark = get_spark_session()
    df = spark.range(10000000).withColumn("example_data3", sf.rand(seed=42) * 3)

    df.write.mode("overwrite").format("delta").saveAsTable("example_table3")

    new_df = spark.table("example_table3")
    assert "example_data3" in new_df.schema.fieldNames()