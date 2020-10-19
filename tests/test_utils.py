from flask_mongo.utils import convert_to_gematria

def test_convert_to_gematria_under_ten():
    assert convert_to_gematria(9) == "ט"

def test_convert_to_gematria_with_fifteen():
    assert convert_to_gematria(15) == "טו"
    assert convert_to_gematria(115) == "קטו"

def test_convert_to_gematria_over_ten():
    assert convert_to_gematria(93) == "צג"
    assert convert_to_gematria(123) == "קכג"

def test_convert_to_gematria_with_zero():
    assert convert_to_gematria(103) == "קג"
