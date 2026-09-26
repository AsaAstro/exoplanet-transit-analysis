import lightkurve as lk
import matplotlib.pyplot as plt

# جستجو و دانلود
search_result = lk.search_lightcurve("TIC 261136679", mission="TESS")
lc = search_result[0].download()

print("=== قبل از پاکسازی ===")
print("تعداد نقاط:", len(lc))

# === پاکسازی ۱: حذف NaN ===
lc_clean = lc.remove_nans()
print("\n=== بعد از حذف NaN ===")
print("تعداد نقاط:", len(lc_clean))

# === پاکسازی ۲: حذف نقاط پرت ===
lc_clean = lc_clean.remove_outliers(sigma=3)
print("\n=== بعد از حذف Outliers ===")
print("تعداد نقاط:", len(lc_clean))

# === رسم نمودار تمیز ===
lc_clean.plot()
plt.savefig("tess_lightcurve_clean.png", dpi=150)
plt.show()

print("\nنمودار تمیز ذخیره شد!")