from flask import current_app
from mongoengine import *
import datetime

"""베이스 Document
Document에 필요한 베이스 클래스를 정의한것이다.
모든 Document에 공통적인 필드를 정의하였다.
"""
class _BaseDocument(Document):
    meta = {
        'abstract': True,

    }
    time_created = DateTimeField()
    time_modified = DateTimeField()

    base_field = ['time_created', 'time_modified']

    def _time_stamp(self, mode=False):
        if mode:
            self.time_created = datetime.datetime.now(tz=current_app.config['KST'])
        self.time_modified = datetime.datetime.now(tz=current_app.config['KST'])

    def _create(self):
        self._time_stamp(mode=True)
        self.save()
