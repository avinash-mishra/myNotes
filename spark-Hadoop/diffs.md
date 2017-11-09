Difference between spark and map-reduce ?

A. Spark can run on top of hadoop and can do the same work as of map-reduce.
-> MapReduce is batch oriented in nature. So, any frameworks on top of MR implementations like Hive and Pig are also batch oriented in nature. For iterative processing as in the case of Machine Learning and interactive analysis, Hadoop/MR doesn't meet the requirement.
In Hadoop 2 (aka YARN), MR and other models including spark can be run on sa single cluster.

-> Spark eliminates a lot of Hadoop's overheads, such as the reliance on I/O for EVERYTHING. Instead it keeps everything in-memory. Great if you have enough memory, not so great if you don't.

HDFS - Hadoop Distributed Filesystem
YARN - Yet Another Resource Negotiator (or Resource Manager)
MapReduce - The batch processing Framework of Hadoop


# Ambari installation
master node:
/etc/init.d/ambari-server
/etc/init.d/ambari-agent

slave nodes:
/etc/init.d/ambari-agent
