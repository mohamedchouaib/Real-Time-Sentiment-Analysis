from time import sleep
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, when, udf,upper
from pyspark.sql.types import StructType, StructField, StringType, FloatType
from config.config import config
from textblob import TextBlob

# def sentiment_analysis(comment) -> str:
#     if comment:
#         analysis = TextBlob(comment)
#         if analysis.sentiment.polarity >= 0.19:
#             return "POSITIVE"
#         elif 0.001<=analysis.sentiment.polarity<0.19 :
#             return "NEUTRAL"
#         else:
#             return "NEGATIVE"
#     return "Empty"

def start_streaming(spark):
    topic = 'iot_pr'
    while True:
        try:
            stream_df = (spark.readStream.format("socket")
                         .option("host", "0.0.0.0")
                         .option("port", 9999)
                         .load()
                         )

            schema = StructType([
                StructField("DateTime", StringType()),
                StructField("Temp_C", FloatType()),
                StructField("Rel_Hum", FloatType()),
                StructField("Wind_Speed_kmh", FloatType()),
                StructField("Visibility_km", FloatType()),
                StructField("Press_kPa", FloatType()),
                StructField("Weather", StringType()),
                StructField("weather_key", StringType())
            ])
            stream_df = stream_df.select(from_json(col('value'),schema).alias("data")).select(("data.*"))                          
            # query= stream_df.writeStream.outputMode("append").format("console").options(truncate=False).start()## Output each batch for debugging
            # query.awaitTermination()
            kafka_df = stream_df.selectExpr("CAST(weather_key AS STRING) AS key", "to_json(struct(*)) AS value")
            query = (kafka_df.writeStream
                   .format("kafka")
                   .option("kafka.bootstrap.servers", config['kafka']['bootstrap.servers'])
                   .option("kafka.security.protocol", config['kafka']['security.protocol'])
                   .option('kafka.sasl.mechanism', config['kafka']['sasl.mechanisms'])
                   .option('kafka.sasl.jaas.config',
                           'org.apache.kafka.common.security.plain.PlainLoginModule required username="{username}" '
                           'password="{password}";'.format(
                               username=config['kafka']['sasl.username'],
                               password=config['kafka']['sasl.password']
                           ))
                   .option('checkpointLocation', '/tmp/checkpoint')
                   .option('topic', topic)
                   .start()
                   .awaitTermination()
                )

        except Exception as e:
            print(f'Exception encountered: {e}. Retrying in 10 seconds')
            sleep(10)
if __name__ == "__main__":
    spark_conn = SparkSession.builder.appName("SocketStreamConsumer").getOrCreate()

    start_streaming(spark_conn)