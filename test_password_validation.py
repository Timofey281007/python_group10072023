import pytest

import password_validation

test_cases_true = ['My_pwd23',
                   'dC2+km2ekmmmmdk',
                   '2=dldvvfvfve267248468',
                   'Cho2o_________']

test_cases_false = ['',
                    'Mm2+',
                    'Mn2+ pe2kepk',
                    'ббггггG=2221',
                    'ffffff2==',
                    'FSFSFSFSDS2=-']


@pytest.mark.parametrize('value', test_cases_true)
def test_validate_password(value):
    assert password_validation.validate_password(value)


@pytest.mark.parametrize('value', test_cases_false)
def test_validate_password1(value):
    assert not password_validation.validate_password(value)
