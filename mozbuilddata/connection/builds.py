# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import unicode_literals

from . import ConnectionBase


class BuildConnection(ConnectionBase):
    def insert_build(self, build_id, version, params):
        d = dict(params)
        d['id'] = build_id
        d['version_'] = version

        self._insert_dict(b'builds', d)

    def get_build(self, build_id):
        c = self.c.cursor()
        c.execute(b'SELECT * FROM builds WHERE id=:id', {'id': build_id})

        for row in self._cursor_to_dicts(c):
            return row

        return None
