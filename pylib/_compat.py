# -*- coding: utf-8 -*-
# flake8: noqa

import sys


PY2 = sys.version_info[0] == 2
WIN = sys.platform.startswith('win')

_identity = lambda x: x

if PY2:
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)

    range_type = xrange
else:
    text_type = str
    string_types = (str, )
    integer_types = (int, )

    range_type = range
