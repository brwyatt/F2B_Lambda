import pytest
from uuid import UUID

from cloud_f2b.filters.auth.sshd_ddos import Sshd_Ddos


@pytest.mark.parametrize("test_data,result", [
    ('', False),
    ('This line should never match', False),
    ('Oct 28 12:42:33 stratus sshd[17548]: fatal: Unable to negotiate with 116.'
     '31.116.38 port 51122: no matching key exchange method found. Their offer:'
     ' diffie-hellman-group14-sha1,diffie-hellman-group-exchange-sha1,'
     'diffie-hellman-group1-sha1 [preauth]', {'host': '116.31.116.38'}),
])
def test_sshd_ddos_filters(test_data, result):
    sshd_ddos = Sshd_Ddos()

    assert sshd_ddos.test_line(test_data) == result


def test_sshd_ddos_filter_uuid():
    assert Sshd_Ddos().uuid == UUID('564327d2-50dd-5f51-af5c-6c41b8f2fcbf')