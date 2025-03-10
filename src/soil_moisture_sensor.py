class SoilMoistureSensor:
    def __init__(self, sensor_id: str):
        self.sensor_id = sensor_id
        self._moisture_level = 0
        
    def read_moisture(self) -> float:
        """
        Simulates reading moisture level from a sensor
        Returns value between 0 (completely dry) and 100 (saturated)
        """
        return self._moisture_level
    
    def set_moisture(self, value: float) -> None:
        """
        For simulation/testing purposes - sets the moisture level
        """
        if not 0 <= value <= 100:
            raise ValueError("Moisture level must be between 0 and 100")
        self._moisture_level = value
        
    def get_moisture_status(self) -> str:
        """
        Returns the soil moisture status based on the reading
        """
        if self._moisture_level < 20:
            return "DRY"
        elif self._moisture_level < 60:
            return "OPTIMAL"
        else:
            return "WET"