# -*- coding: utf-8 -*-

from pylib.security import gen_salt


def test_gen_salt():
    assert len(gen_salt(6)) == 6
