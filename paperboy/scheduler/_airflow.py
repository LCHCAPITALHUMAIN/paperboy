import logging
from airflow.models import BaseOperator
# from airflow.operators.sensors import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

from .base import BaseScheduler


class AirflowScheduler(BaseScheduler):
    pass


class JobOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(JobOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        logging.info("job")


class JobCleanupOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(JobCleanupOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        logging.info("job-cleanup")


class ReportOperator(BaseOperator):
    @apply_defaults
    def __init__(self, *args, **kwargs):
        super(ReportOperator, self).__init__(*args, **kwargs)

    def execute(self, context):
        logging.info("report")