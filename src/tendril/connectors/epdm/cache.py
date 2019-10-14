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
Resources for EPDM Response Caching
-------------------------------
"""

from fs.rpcfs import RPCFS
from fs.opener import fsopendir
from fs.errors import RemoteConnectionError

try:
    from tendril.config import EPDM_CACHE
except ImportError:
    EPDM_CACHE = None


def _cache_init():
    if not EPDM_CACHE:
        return
    if EPDM_CACHE.startswith('rpc://'):
        try:
            l_cache_fs = RPCFS('http://' + EPDM_CACHE[len('rpc://'):])
        except RemoteConnectionError:
            return None
    else:
        l_cache_fs = fsopendir(EPDM_CACHE, create_dir=True)
    return l_cache_fs


cachefs = _cache_init()
