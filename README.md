# What to use when

Summary of the concepts: 
NOTE: Below content is useful but is not a replacement for the Video made by Sandeep Sir. Please watch the full video first and then use the below summary.

Cache
Options: Redis, Memcache
Use: Redis (Redis is an modern version of Memcache). Redis understands data structures like list etc, so performing list append fast in Redis wrt Memcache which sees all values as a blob.

File storage
Why? To store images, videos, files etc. These are blob storages. DBMS is used when we have to query on the data. But file is something we just serve.
Options: S3

Text search engine
Why?
Netflix: search for a movie
Amazon: search for a product
Uber: search for a location
Options: Elastic Search, Solar (build over lucene)
Important: They are search engines, not databases. They give availability and redundancy but no guarantee on data, so data may be lost. Store critical data somewhere else.

Fuzzy text search
Why? User may type wrong spelling. For eg, instead of Airport, may type Ariport.
Options: Elasticsearch, Solar

Timeseries database
Why? For metrics
Options: InfluxDB, OpenTSDB 
Note: These are kind of RDBMS with some customization. In it, user will write always in append-only mode and wont edit old data. Also, queries will be bulk queries on a time range. So, optimized for that.

Data Warehouse/ Big Data
Why? Want to store huge data for analytics. Eg for Amazon, which country giving more revenue, which geography has more transactions, which product sold where most etc.
Options: Hadoop
Note: This is more for offline processing.

RDBMS
Why? When information is structured. And when we need ACID guarantees. For eg, in banking, amount debited but not credited, different account balance for different queries etc
Options: MySQL, PostgreSQL, Oracle

NoSQL (Document DB)
Why? For Amazon, building catalogue. Catalogue can have different type of items with different attributes. Eg, T-shirt, Washing machine, Refrigerator, Milk, Medicine etc. This can be stored as json in RDBMS but NoSQL DBs are designed to handle such kind of queries in a more optimized manner.
Options: MongoDB, CouchBase

NoSQL (Columnar DB)
Why? When data is ever increasing. Eg, Uber drivers keep sending their location data every few minutes. And if drivers keep increasing, data will keep growing exponentially. But queries will be low only on this huge data, like what locations for a given driver id.
Options: Cassandra, Hbase

1> Write Heavy vs Read Heavy systems is also an important point to consider for database selection. We cannot write scale RDBMS (as generally in RDBMS the write is on the single primary instance). For DocumentDB, we need sharding to write scale it which can be done but are not so natural as it is in ColumnarDB like Cassandra where we need to mandatorily choose the partition key during the data modelling itself. So for write heavy systems I prefer to go with Cassandra if I don't need ACID. For write heavy systems that need ACID we should choose RDBMS with multi master configuration and for that application needs to take care of bifurcating the data to the appropriate master based on the decided key. 

2>  Graph database for mapping social network type of data.



1. Twitter
2. Facebook / Instagram
3. Tinder
4. IRCTC / Redbus
5. Whatsapp / Messenger / Slack
6. Netflix / Youtube
7. Uber / Ola
8. Airbnb / Oyo
9. Zoom
10. Amazon / Flipkart
11. Bookmyshow
12. Google Drive / Dropbox
13. Zerodha / Upstox
14. Swiggy / Zomato
15. Make My Trip
16. Gmail
17. Google Map
18. Google Docs
19. Rate limiter
20. TinyURL / Pastebin 