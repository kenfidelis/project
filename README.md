# IoT Soil Moisture Sensor Testing Suite

This project provides a testing framework for IoT soil moisture sensors, including simulation capabilities and comprehensive test coverage.

## Features

- Soil moisture sensor simulation
- Moisture level validation
- Status classification (DRY/OPTIMAL/WET)
- Comprehensive test suite
- GitHub Actions CI/CD integration

## Project Structure

```
.
├── src/
│   └── soil_moisture_sensor.py
├── tests/
│   └── test_soil_moisture_sensor.py
├── .github/
│   └── workflows/
│       └── test.yml
├── requirements.txt
└── README.md
```

## Running Tests

To run the tests locally:

```bash
pip install -r requirements.txt
pytest tests/
```

To run tests with coverage:

```bash
pytest --cov=src tests/
```

## CI/CD

The project includes GitHub Actions workflow that:
- Runs on push to main and pull requests
- Sets up Python environment
- Installs dependencies
- Runs tests with coverage
- Uploads coverage reports to Codecov

## Sensor Status Classifications

- DRY: Moisture level < 20%
- OPTIMAL: Moisture level between 20% and 60%
- WET: Moisture level > 60%