import lightkurve as lk

# جستجوی ستاره TIC 261136679
search_result = lk.search_lightcurve("TIC 261136679", mission="TESS")

print("=== نتایج جستجو ===")
print(search_result)

# دانلود اولین نتیجه
lc = search_result[0].download()

print("\n=== منحنی نوری ===")
print(lc)
# رسم نمودار
lc.plot()
import matplotlib.pyplot as plt
plt.savefig("tess_lightcurve.png", dpi=150)
plt.show()