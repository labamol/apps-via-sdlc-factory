"""Generated tests for FEAT-01: Feedback Submission."""

import pytest

import feat_01


@pytest.fixture(autouse=True)
def _reset():
    feat_01.reset()


def test_ac_01_01_01():
    """AC-01.01.01: Given the system, when exercised, then: Customers must be ab"""
    record = {
        'name': 'Chloe',
        'email': 'chloe1@sample.org',
        'category': 'praise',
        'message': 'Synthetic record 1 for STORY-01.01',
    }
    stored = feat_01.story_01_01(record)
    assert stored["story_id"] == "STORY-01.01"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_01_01_02():
    """AC-01.01.02: Negative/boundary behavior for BR-01 is handled without data"""
    with pytest.raises(feat_01.ServiceError):
        feat_01.story_01_01({})
    with pytest.raises(feat_01.ServiceError):
        feat_01.story_01_01("not-a-dict")


def test_ac_01_02_01():
    """AC-01.02.01: Given the system, when exercised, then: The system shall ack"""
    record = {
        'name': 'Ava',
        'email': 'ava1@test.local',
        'category': 'praise',
        'message': 'Synthetic record 1 for STORY-01.02',
    }
    stored = feat_01.story_01_02(record)
    assert stored["story_id"] == "STORY-01.02"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_01_02_02():
    """AC-01.02.02: Negative/boundary behavior for BR-02 is handled without data"""
    with pytest.raises(feat_01.ServiceError):
        feat_01.story_01_02({})
    with pytest.raises(feat_01.ServiceError):
        feat_01.story_01_02("not-a-dict")


def test_ac_01_03_01():
    """AC-01.03.01: Given the system, when exercised, then: Submissions must be """
    record = {
        'name': 'Ben',
        'email': 'ben1@sample.org',
        'category': 'question',
        'message': 'Synthetic record 1 for STORY-01.03',
    }
    stored = feat_01.story_01_03(record)
    assert stored["story_id"] == "STORY-01.03"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_01_03_02():
    """AC-01.03.02: Negative/boundary behavior for BR-03 is handled without data"""
    with pytest.raises(feat_01.ServiceError):
        feat_01.story_01_03({})
    with pytest.raises(feat_01.ServiceError):
        feat_01.story_01_03("not-a-dict")
