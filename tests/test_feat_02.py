"""Generated tests for FEAT-02: Feedback Review."""

import pytest

import feat_02


@pytest.fixture(autouse=True)
def _reset():
    feat_02.reset()


def test_ac_02_01_01():
    """AC-02.01.01: Given the system, when exercised, then: Support staff shall """
    record = {
        'name': 'Dev',
        'email': 'dev1@test.local',
        'category': 'bug',
        'message': 'Synthetic record 1 for STORY-02.01',
    }
    stored = feat_02.story_02_01(record)
    assert stored["story_id"] == "STORY-02.01"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_02_01_02():
    """AC-02.01.02: Negative/boundary behavior for BR-04 is handled without data"""
    with pytest.raises(feat_02.ServiceError):
        feat_02.story_02_01({})
    with pytest.raises(feat_02.ServiceError):
        feat_02.story_02_01("not-a-dict")


def test_ac_02_02_01():
    """AC-02.02.01: Given the system, when exercised, then: The review dashboard"""
    record = {
        'name': 'Hiro',
        'email': 'hiro1@sample.org',
        'category': 'question',
        'message': 'Synthetic record 1 for STORY-02.02',
    }
    stored = feat_02.story_02_02(record)
    assert stored["story_id"] == "STORY-02.02"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_02_02_02():
    """AC-02.02.02: Negative/boundary behavior for BR-05 is handled without data"""
    with pytest.raises(feat_02.ServiceError):
        feat_02.story_02_02({})
    with pytest.raises(feat_02.ServiceError):
        feat_02.story_02_02("not-a-dict")


def test_ac_02_03_01():
    """AC-02.03.01: Given the system, when exercised, then: Closed feedback must"""
    record = {
        'name': 'Farid',
        'email': 'farid1@test.local',
        'category': 'question',
        'message': 'Synthetic record 1 for STORY-02.03',
    }
    stored = feat_02.story_02_03(record)
    assert stored["story_id"] == "STORY-02.03"
    assert stored["record_id"] == 1
    assert stored["email"] == record["email"]


def test_ac_02_03_02():
    """AC-02.03.02: Negative/boundary behavior for BR-06 is handled without data"""
    with pytest.raises(feat_02.ServiceError):
        feat_02.story_02_03({})
    with pytest.raises(feat_02.ServiceError):
        feat_02.story_02_03("not-a-dict")
