# TESS Light Curve Analysis Report

## Target
- **Star:** TIC 261136679
- **Mission:** TESS (Transiting Exoplanet Survey Satellite)
- **Sector:** 01
- **Observation period:** ~28 days

## Data
- **Total data points:** 18,264
- **After cleaning:** 18,037
- **Outliers removed:** 227

## Method
1. Downloaded light curve with `lightkurve`
2. Removed NaNs and outliers (sigma = 3)
3. Computed Lomb-Scargle periodogram
4. Found best period
5. Folded light curve

## Results
- **Best Period:** ~4.98 days

## Interpretation
The star shows a periodic signal of about 4.98 days. This could be due to:
- Stellar rotation with starspots
- A transiting exoplanet
- Stellar pulsation

## Tools Used
- Python 3.12
- lightkurve 2.6.0
- astropy 8.0.1
- matplotlib

## Files
- `tess_01_download.py` — Download data
- `tess_02_clean.py` — Clean data
- `tess_03_periodogram.py` — Period analysis
- `tess_lightcurve.png` — Raw light curve
- `tess_lightcurve_clean.png` — Cleaned light curve
- `tess_periodogram.png` — Periodogram
- `tess_folded.png` — Folded light curve