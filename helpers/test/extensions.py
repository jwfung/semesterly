# Copyright (C) 2017 Semester.ly Technologies, LLC
#
# Semester.ly is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Semester.ly is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

from django.test import TestCase
from elasticsearch import Elasticsearch
from rest_framework.test import APITestCase

from searches.elastic import GlobSearchDocument


class TestCaseWithElastic(TestCase):
    @classmethod
    def setUpClass(cls):
        """On inherited classes, run our `setUp` method."""
        if cls is TestCaseWithElastic or cls.setUp is TestCaseWithElastic.setUp:
            return
        orig_setUp = cls.setUp
        def setUpOverride(self, *args, **kwargs):
            TestCaseWithElastic.setUp(self)
            return orig_setUp(self, *args, **kwargs)
        cls.setUp = setUpOverride


    @classmethod
    def tearDownClass(cls):
        """On inherited classes, run our `tearDown` method."""
        if cls is TestCaseWithElastic or cls.tearDown is TestCaseWithElastic.tearDown:
            return
        orig_tearDown = cls.tearDown
        def tearDownOverride(self, *args, **kwargs):
            TestCaseWithElastic.tearDown(self)
            return orig_tearDown(self, *args, **kwargs)
        cls.tearDown = tearDownOverride


    def setUp(self):
        GlobSearchDocument._doc_type.index = 'test-search-index'


    def tearDown(self):
        Elasticsearch().indices.delete(index=GlobSearchDocument._doc_type.index,
                                       ignore=[400, 404])
