# factored-datathon-2023-Data-Hackers

This project revolves around leveraging two primary data sources related to product reviews on Amazon:

1. Batch-format Tables: These tables contain valuable insights and information about product reviews on Amazon. They are structured in batches, distributed in partitions, and stored as JSON format files in an Azure Data Lake Storage instance. Specifically, we have two tables:

  - Amazon Product Reviews: This dataset comprises an extensive collection of product reviews sourced from Amazon. It contains an impressive 82.83 million unique reviews         contributed by approximately 20 million users.
  - Amazon Metadata: This table contains crucial descriptions and metadata for all products present in the dataset.

2. Streaming Data - Amazon Product Reviews: In addition to the batch-format tables, we have access to real-time data updates of Amazon Product Reviews through a streaming mode. This streaming topic continuously receives new data as it becomes available, ensuring we remain up-to-date with the latest developments.
