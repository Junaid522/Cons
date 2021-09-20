import json
from celery_progress.backend import ProgressRecorder
from time_consultants.celery import app as celery_app
from ..helper.import_scholarships_data import ScholarshipExcelToJsonParser, get_or_create_complete_scholarship
from ..utils import DataframeUtil
from .base import BaseTask


class ImportScholarshipFromExcelTask(BaseTask):
    name = "ImportScholarshipFromExcelTask"

    def run(self, filepath, *args, **kwargs):
        result = []
        progress_recorder = ProgressRecorder(self)
        dataframe = DataframeUtil.get_validated_dataframe(filepath)
        total_record = dataframe.shape[0] + 1
        parser = ScholarshipExcelToJsonParser(dataframe)
        status, errors = parser.get_header()
        if not status:
            result = errors

        else:
            rows_data = parser.data
            row = 2
            for data in rows_data:
                progress_recorder.set_progress(current=row, total=total_record,
                                               description="Inserting row into table")
                status, errors = get_or_create_complete_scholarship(data, row)
                if not status:
                    result = errors
                    break
                if row < total_record:
                    row = row + 1
            if total_record == row:
                success_message = 'successfully completed. total records ' + str(total_record)
                result = [{'key': 'success', 'error': success_message}]
        return json.dumps(result)


@celery_app.task(bind=True, base=ImportScholarshipFromExcelTask)
def import_scholarship_task(self, *args, **kwargs):
    return super(type(self), self).run(*args, **kwargs)
