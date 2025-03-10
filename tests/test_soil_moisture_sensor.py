import pytest
from src.soil_moisture_sensor import SoilMoistureSensor

def test_sensor_initialization():
    sensor = SoilMoistureSensor("SENSOR_001")
    assert sensor.sensor_id == "SENSOR_001"
    assert sensor.read_moisture() == 0

def test_set_valid_moisture():
    sensor = SoilMoistureSensor("SENSOR_001")
    sensor.set_moisture(50.0)
    assert sensor.read_moisture() == 50.0

def test_set_invalid_moisture():
    sensor = SoilMoistureSensor("SENSOR_001")
    with pytest.raises(ValueError):
        sensor.set_moisture(101)
    with pytest.raises(ValueError):
        sensor.set_moisture(-1)

@pytest.mark.parametrize("moisture,expected_status", [
    (0, "DRY"),
    (15, "DRY"),
    (30, "OPTIMAL"),
    (55, "OPTIMAL"),
    (70, "WET"),
    (100, "WET"),
])
def test_moisture_status(moisture, expected_status):
    sensor = SoilMoistureSensor("SENSOR_001")
    sensor.set_moisture(moisture)
    assert sensor.get_moisture_status() == expected_status