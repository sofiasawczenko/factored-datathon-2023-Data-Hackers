# Factored Datathon 2023

This project leverages two primary data sources related to product reviews on Amazon, using Databricks for processing and analysis.

## 1. Batch-format Tables

These tables contain valuable insights and information about product reviews on Amazon. They are structured in batches, distributed in partitions, and stored as JSON files in an Azure Data Lake Storage instance. Specifically, the following two tables are used:

- **Amazon Product Reviews**: This dataset consists of 82.83 million unique product reviews contributed by approximately 20 million users.
- **Amazon Metadata**: This table contains crucial product descriptions and metadata for all products in the dataset.

## 2. Streaming Data - Amazon Product Reviews

In addition to the batch-format tables, real-time data updates are available through a streaming mode. This streaming topic continuously receives new data as it becomes available, keeping the dataset up-to-date with the latest developments.

```python
spark.conf.set("fs.azure.account.auth.type.{0}.dfs.core.windows.net".format("safactoreddatathon"), "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.{0}.dfs.core.windows.net".format("safactoreddatathon"), "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
```
### Installation of Required Libraries
To get started with the necessary packages, install the required libraries using the following commands:

```python
!pip install pyspark
!pip install azure-eventhub
```
### Spark Session and EventHub Consumer
Initialize the SparkSession and EventHub consumer client for handling real-time events.
```python
from azure.eventhub import EventHubConsumerClient
from pyspark.sql import SparkSession
```

# Define Event Hub Connection Parameters
eventhub_namespace = "factored-datathon"
eventhub_name = "factored_datathon_amazon_review_1"
listen_policy_key = "sJJnyi8GGTBAa55jY89kacoT6hXAzWx2B+AEhCPEKYE="
listen_policy_connection_string = "Endpoint=sb://factored-datathon.servicebus.windows.net/;SharedAccessKeyName=datathon_listener;SharedAccessKey=sJJnyi8GGTBAa55jY89kacoT6hXAzWx2B+AEhCPEKYE=;EntityPath=factored_datathon_amazon_review"

# Event processing function
def on_event(partition_context, event):
    print("Received event from partition: {}".format(partition_context.partition_id))
    print("Data: {}".format(event.body_as_str(encoding='UTF-8')))
    print("Properties: {}".format(event.properties))

# EventHub Consumer Client setup
connection_str = listen_policy_connection_string
consumer_client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group="$Default", eventhub_name=eventhub_name)

# Start receiving events
try:
    with consumer_client:
        consumer_client.receive(on_event=on_event, starting_position="-1")
except KeyboardInterrupt:
    print("Receiving has stopped.")
3. Accessing the Data
Use the following commands to access the batch-format data stored in Azure Data Lake:

```python
dbutils.fs.ls("abfss://source-files@safactoreddatathon.dfs.core.windows.net/amazon_reviews/")
This command lists the files within the amazon_reviews folder in the Azure Data Lake.
```
Example Output:
```python
[FileInfo(path='abfss://source-files@safactoreddatathon.dfs.core.windows.net/amazon_reviews/partition_1/', name='partition_1/', size=0, modificationTime=1689569806000),
 FileInfo(path='abfss://source-files@safactoreddatathon.dfs.core.windows.net/amazon_reviews/partition_10/', name='partition_10/', size=0, modificationTime=1689569900000),
 FileInfo(path='abfss://source-files@safactoreddatathon.dfs.core.windows.net/amazon_reviews/partition_100/', name='partition_100/', size=0, modificationTime=1689570860000),
 FileInfo(path='abfss://source-files@safactoreddatathon.dfs.core.windows.net/amazon_reviews/partition_1000/', name='partition_1000/', size=0, modificationTime=1689580431000),
 ...]
```
This allows you to access the different partitions of product reviews, enabling further processing and analysis.

## Conclusion
The Factored Datathon 2023 project integrates both batch and streaming data sources to analyze product reviews from Amazon. By using Spark, Databricks, and Azure Data Lake, it facilitates efficient processing of large datasets and real-time data streaming. The setup includes necessary libraries for PySpark and Azure EventHub to handle data processing and event-driven workflows.
