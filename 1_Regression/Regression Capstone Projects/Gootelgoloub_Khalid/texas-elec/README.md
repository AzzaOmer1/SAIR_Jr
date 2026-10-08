# Texas Monthly Electricity Consumption

## Project overview
This project estimates monthly electricity consumption in Texas using the observed average temperature and calendar information for that month.

This is an estimate made when the month's observed average temperature is available; it is not a forecast made before the month begins.

## Dataset
- 306 monthly observations
- Period: January 2001 to June 2026
- Target: `consumption`
- Main predictors: average temperature, squared average temperature, year, and month
### Data sources
- Electricity consumption: [U.S. Energy Information Administration (EIA) — Electricity Data](https://www.eia.gov/electricity/data.php )
- Texas monthly average temperature: [NOAA Climate at a Glance — Texas, Monthly Average Temperature (2001–2026)](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/41/tavg/1/0/2001-2026 )
- [NOAA Climate at a Glance — Statewide Time Series](https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series )


## Evaluation
The data was split chronologically into training, validation, and test sets.
Models were compared using the validation period. The selected model was Linear Regression.

Final test metrics:
- R²: 0.4168
- MAE: 3707.6046
- RMSE: 4250.8981

The test period was also inspected during earlier exploratory modeling, so these final metrics should be interpreted transparently.

## Project files
- `notebooks/`: data preparation, EDA, and modeling notebooks
- `data/`: raw and processed data
- `models/`: saved model, complete preprocessing pipeline, and model card
- `experiments/mlruns/`: MLflow experiment tracking
- `app.py`: Streamlit prediction app

## Setup
From the project folder, install the project dependencies:

```bash
uv sync
```

## Run the Streamlit app

```bash
uv run streamlit run app.py
```

## Run the MLflow UI

On Windows Command Prompt:

```cmd
set MLFLOW_ALLOW_FILE_STORE=true
uv run mlflow ui --backend-store-uri experiments/mlruns --port 5000
```

Then open `http://127.0.0.1:5000` in a browser.

## Important limitation
The app requires the observed average temperature for the month being estimated. It should not be interpreted as a forecast made before that month's weather is known.
