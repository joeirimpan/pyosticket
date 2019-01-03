#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pyosticket` package."""
import sys
import os

testpath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, testpath + '/../')

import vcr  # noqa
import pytest  # noqa

from pyosticket import OSTicketAPI # noqa


osticket_vcr = vcr.VCR(
    filter_headers=[
        'X-API-Key',
    ]
)

@pytest.fixture
def osticket():
    return OSTicketAPI(
        url="https://osticket-test.company.com",
        api_key="API-KEY",
    )


@osticket_vcr.use_cassette(
    'tests/fixtures/tickets.yml'
)
def test_all_tickets(osticket):
    response, code = osticket.ticket.all("nibba@nibba.com")
    assert code == 200
    assert response[0]["number"] == "XXXXXXXXXXXXXX"
    assert response[0]["status"] == "closed"
