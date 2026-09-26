
# Exoplanet Transit Analysis

Analysis of TESS light curves for exoplanet transit detection.

## About Me

I am an Electrical Engineering graduate (M.Sc. in Telecommunications) with a strong interest in astronomy and astrophysics. I am building my skills in astronomical data analysis, with the goal of pursuing a PhD in this field.

## Project Overview

This project analyzes real data from NASA's TESS (Transiting Exoplanet Survey Satellite) mission. It includes:

- Downloading light curves with `lightkurve`
- Data cleaning (NaN removal, outlier rejection)
- Period analysis with Lomb-Scargle periodogram
- Phase-folding of light curves

## Target Star

- **TIC 261136679**
- Observed in TESS Sector 01
- ~18,000 data points

## Results

- **Best Period:** ~4.98 days
- Possible interpretations: stellar rotation, exoplanet transit, or pulsation

## Tools

- Python 3.12
- lightkurve 2.6.0
- astropy 8.0.1
- matplotlib

## Files

| File | Description |
|------|-------------|
| `tess_01_download.py` | Download TESS light curve |
| `tess_02_clean.py` | Clean data |
| `tess_03_periodogram.py` | Period analysis |
| `REPORT.md` | Full analysis report |
| `tess_lightcurve.png` | Raw light curve |
| `tess_lightcurve_clean.png` | Cleaned light curve |
| `tess_periodogram.png` | Periodogram |
| `tess_folded.png` | Folded light curve |

## Next Steps

- Analyze transits for exoplanet detection
- Compare with known exoplanet catalogs
- Extend analysis to multiple stars
