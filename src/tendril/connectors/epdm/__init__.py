#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2017 Chintalagiri Shashank
#
# This file is part of tendril-connector-tally.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
EPDM Primitives and API Engine
------------------------------
"""


try:
    from tendril.config import EPDM_HOST
    from tendril.config import EPDM_USERNAME
    from tendril.config import EPDM_PASSWORD
except ImportError:
    EPDM_HOST = 'localhost'
    EPDM_USERNAME = 'pdmwadmin'
    EPDM_PASSWORD = 'pdmwadmin'


from .cache import cachefs


class EPDMNotAvailable(ConnectionError):
    pass


class EPDMAPIEngine(object):
    """
    Very bare-bones architecture. Could do with more structure.  
    """
    def __init__(self):
        self._query = None
        self._response = None

    def execute(self, query, cachename=None):
        self.query = query
        try:
            pass
        except ConnectionError as e:
            print("Got Exception")
            print(e)
            raise EPDMNotAvailable
        if cachefs and cachename:
            with cachefs.open(cachename + '.xml', 'wb') as f:
                f.write(r.content)
        self._response = ''
        return self._response

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    @property
    def response(self):
        return self._response

    def print_query(self):
        s = StringIO()
        self.query.write(s)
        print(s.getvalue())
