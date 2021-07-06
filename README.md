# cloud-batch-processing
### Tech Stack
 1. Google Cloud Storage
 2. Google Composer (Airflow)
 3. Google Dataflow
 4. Google BigQuery

### Steps
1. Create Google Cloud Storage
2. Upload Dataset(.csv) ke dalam GCS
3. Create Composer dengan spesifikasi

- Location :  us-central1
- Zone : us-central1
- Node count : 3
- Disk size (GB) : 20
- Machine type : n1-standard-1
- Cloud SQL machine type : db-n1-standard-2 (2 vCPU, 7.5 GB memory)
- Web server machine type : composer-n1-webserver-2 (2 vCPU, 1.6 GB memory)

4. Create Dataset di BigQuery
5. Lalu create table dengan schema

- user_id INTEGER
- search_keyword STRING
- search_result_count INTEGER
- created_at DATETIME

7. Create Dataflow

- Create Job From Template
- di dataflow template, pilih yang process data in bulk -> text file on cloud storage to BigQuery
- di Required Parameter di isi value file dan lokasi file Javascript untuk UDF dan json untuk schema bigquery

8. deploy dag airflow, di storage composer -> folder dags
9. run airflow melalui composer -> airflow webserver
