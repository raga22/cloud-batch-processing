from airflow import models
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowTemplatedJobStartOperator
from airflow.utils.dates import days_ago

import datetime
import pandas

bucket_path = models.Variable.get('bucket_path')
project_id = models.Variable.get('project_id')
gce_zone = models.Variable.get('gce_zone')

default_args = {
    'start_date':days_ago(1)
}

def _extract_data(ti):
    return 0

with DAG('search_history', schedule_interval=datetime.timedelta(days=1), default_args=default_args,
catchup=False) as dag:
    
    start_template_job = DataflowTemplatedJobStartOperator(
        task_id='dataflow_operator_transform_csv_to_bq',
        template='gs://dataflow-templates/latest/GCS_Text_to_BigQuery',
        parameters={
            'javascriptTextTransformFunctionName': 'transformCSVtoJSON',
            'JSONPath': bucket_path + '/jsonSchema.json',
            'javascriptTextTransformGcsPath': bucket_path + '/transformCSVtoJSON.js',
            'inputFilePattern': bucket_path + '/inputFile.txt',
            'outputTable': project_id + ':bs_wk2.keyword_search',
            'bigQueryLoadingTemporaryDirectory': bucket_path + '/tmp/',
        },
    )
