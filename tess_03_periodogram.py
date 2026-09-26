import lightkurve as lk
import matplotlib.pyplot as plt

# جستجو و دانلود
search_result = lk.search_lightcurve("TIC 261136679", mission="TESS")
lc = search_result[0].download()

# پاکسازی
lc_clean = lc.remove_nans().remove_outliers(sigma=3)

# === محاسبه Periodogram ===
pg = lc_clean.to_periodogram(method="lombscargle")

# پیدا کردن دوره با بیشترین قدرت
best_period = pg.period_at_max_power
print("=== دوره تناوب پیدا شده ===")
print("Best Period:", best_period)

# === رسم Periodogram ===
pg.plot()
plt.savefig("tess_periodogram.png", dpi=150)
plt.show()

# === رسم منحنی نوری فولد شده ===
lc_clean.fold(period=best_period).plot()
plt.savefig("tess_folded.png", dpi=150)
plt.show()

print("\nنمودارها ذخیره شدن!")