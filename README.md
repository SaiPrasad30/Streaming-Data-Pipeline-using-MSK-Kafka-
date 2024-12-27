# Streaming-Data-Pipeline-using-MSK-Kafka

## Overview
This Project aims to represents a modern data streaming and processing pipeline built on AWS. The solution involves integrating external applications with a highly scalable, event-driven architecture. It leverages Amazon MSK (Managed Streaming for Apache Kafka) for real-time data processing, Kinesis Firehose for data ingestion, and S3 for storage and Athena for analytics. 

The design ensures data integrity, scalability, and efficient data consumption for downstream applications, enabling robust analytics and real-time processing.

---

## Project Goals
1. **Enable Real-Time Data Ingestion and Processing**: Stream data from external applications efficiently into an analytics platform.
2. **Decouple Producers and Consumers**: Use AWS SQS and MSK for reliable and asynchronous communication.
3. **Support Scalable Data Storage and Analytics**: Store processed data in S3 for querying and long-term retention.
4. **Enhance Data Governance and Accessibility**: Catalog data using AWS Glue and query using Athena for business insights.
5. **Build Fault-Tolerant Architecture**: Ensure system resilience with Lambda-based error handling and message processing.
6. **Optimize for Cost and Performance**: Use serverless and managed services to reduce operational overhead.

---

## Services Used
### Core Services
1. **Amazon API Gateway**:
   - Acts as an entry point for external applications to push data into the pipeline.
   
2. **Amazon SQS**:
   - Ensures reliable message delivery between producers and downstream processing components.

3. **AWS Lambda**:
   - Powers serverless compute for producing/consuming Kafka messages and transforming data.
   - Includes a Kafka layer to simplify interaction with the MSK cluster.

4. **Amazon MSK (Managed Streaming for Apache Kafka)**:
   - Provides a managed Kafka service for real-time event streaming and message brokering.

5. **Amazon Kinesis Data Firehose**:
   - Streams processed data into Amazon S3 for long-term storage.

6. **Amazon S3**:
   - Stores raw and processed data for analytics and archival.

### Data Processing and Analytics
1. **AWS Glue Data Catalog and Crawlers**:
   - Enables automated schema discovery and metadata management.

2. **Amazon Athena**:
   - Provides serverless querying capabilities over data stored in S3.

---

## Workflow Summary
1. **Ingestion**:
   - External applications send data through API Gateway into SQS.
   - Lambda retrieves messages from SQS and publishes them to MSK.

2. **Processing**:
   - MSK brokers handle event streaming. Kafka consumers process events via Lambda.
   - Processed data is sent to Kinesis Firehose for ingestion into S3.

3. **Analytics**:
   - Data stored in S3 is cataloged using AWS Glue.
   - Athena provides serverless querying.

4. **Integration**:
   - Downstream systems retrieve insights through Athena queries.

---

## Networking Details
1. **VPC Configuration**:
   - The architecture is deployed within a single VPC.
   - The VPC contains 2 public subnets and 2 private subnets.

2. **Amazon MSK**:
   - The MSK cluster is deployed in private subnets for enhanced security.

3. **Linux Machines**:
   - A Linux machine is deployed in a public subnet to act as a bastion host for accessing resources in private subnets.
   - Another Linux machine is deployed in a private subnet to interact with the MSK cluster.

4. **Connectivity**:
   - The bastion host in the public subnet facilitates secure SSH access to the Linux machine in the private subnet.
   - Both machines are configured to ensure seamless interaction with the MSK cluster in private subnets.

5. **Security**:
   - Security groups and network ACLs are configured to allow only required traffic between the components.
   - Private subnets have restricted internet access, using NAT gateways in public subnets for outbound connections where necessary.
