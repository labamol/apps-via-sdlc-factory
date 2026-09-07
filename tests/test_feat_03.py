"""Generated tests for FEAT-03: Reporting."""

import pytest

import feat_03


@pytest.fixture(autouse=True)
def _reset():
    feat_03.reset()


def test_ac_03_01_01():
    """AC-03.01.01: Given the system, when exercised, then: Managers must receiv"""
    record = {
        'name': 'Hiro',
        'email': 'hiro1@test.local',
        'category': 'bug',
        'message': 'Synthetic record 1 for STORY-03.01',
    }
    stored = feat_03.story_03_01(record)
    assert stored["story_id"] == "STORY-03.01"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_03_01_02():
    """AC-03.01.02: Negative/boundary behavior for BR-07 is handled without data"""
    with pytest.raises(feat_03.ServiceError):
        feat_03.story_03_01({})
    with pytest.raises(feat_03.ServiceError):
        feat_03.story_03_01("not-a-dict")


def test_ac_03_02_01():
    """AC-03.02.01: Given the system, when exercised, then: The report delivery """
    record = {
        'name': 'Grace',
        'email': 'grace1@example.com',
        'category': 'idea',
        'message': 'Synthetic record 1 for STORY-03.02',
    }
    stored = feat_03.story_03_02(record)
    assert stored["story_id"] == "STORY-03.02"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_03_02_02():
    """AC-03.02.02: Negative/boundary behavior for BR-08 is handled without data"""
    with pytest.raises(feat_03.ServiceError):
        feat_03.story_03_02({})
    with pytest.raises(feat_03.ServiceError):
        feat_03.story_03_02("not-a-dict")
