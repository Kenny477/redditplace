import pandas as pd
import time

results = pd.DataFrame(columns=['format', 'load', 'save'])

print("Loading CSV")
print("===========")
# Load CSV
csv_load_start = time.perf_counter()
df = pd.read_csv('place_tiles.csv')
csv_load_end = time.perf_counter()
print("Loaded CSV in {} seconds\n".format(csv_load_end - csv_load_start))

print("Saving CSV")
print("==========")
# Save CSV
csv_save_start = time.perf_counter()
df.to_csv('place_tiles_new.csv')
csv_save_end = time.perf_counter()
print("Saved CSV in {} seconds\n".format(csv_save_end - csv_save_start))

results = results.append({'format': 'csv', 'load': csv_load_end - csv_load_start, 'save': csv_save_end - csv_save_start}, ignore_index=True)

print("Saving Pickle")
print("=============")
# Save pickle
pickle_save_start = time.perf_counter()
df.to_pickle('place2017.pkl')
pickle_save_end = time.perf_counter()
print("Saved Pickle in {} seconds\n".format(pickle_save_end - pickle_save_start))

print("Loading Pickle")
print("=============")
# Load pickle
pickle_load_start = time.perf_counter()
df = pd.read_pickle('place2017.pkl')
pickle_load_end = time.perf_counter()
print("Loaded Pickle in {} seconds\n".format(pickle_load_end - pickle_load_start))

results = results.append({'format': 'pickle', 'load': pickle_load_end - pickle_load_start, 'save': pickle_save_end - pickle_save_start}, ignore_index=True)

print("Saving HDF5")
print("============")
# Save HDF5
hdf5_save_start = time.perf_counter()
df.to_hdf('place2017.h5', 'place2017')
hdf5_save_end = time.perf_counter()
print("Saved HDF5 in {} seconds\n".format(hdf5_save_end - hdf5_save_start))

print("Loading HDF5")
print("============")
# Load HDF5
hdf5_load_start = time.perf_counter()
df = pd.read_hdf('place2017.h5', 'place2017')
hdf5_load_end = time.perf_counter()
print("Loaded HDF5 in {} seconds\n".format(hdf5_load_end - hdf5_load_start))

results = results.append({'format': 'hdf5', 'load': hdf5_load_end - hdf5_load_start, 'save': hdf5_save_end - hdf5_save_start}, ignore_index=True)

print("Saving Feather")
print("==============")
# Save feather
feather_save_start = time.perf_counter()
df.to_feather('place2017.feather')
feather_save_end = time.perf_counter()
print("Saved Feather in {} seconds\n".format(feather_save_end - feather_save_start))

print("Loading Feather")
print("==============")
# Load feather
feather_load_start = time.perf_counter()
df = pd.read_feather('place2017.feather')
feather_load_end = time.perf_counter()
print("Loaded Feather in {} seconds\n".format(feather_load_end - feather_load_start))

results = results.append({'format': 'feather', 'load': feather_load_end - feather_load_start, 'save': feather_save_end - feather_save_start}, ignore_index=True)

print("Saving Parquet")
print("===============")
# Save parquet
parquet_save_start = time.perf_counter()
df.to_parquet('place2017.parquet')
parquet_save_end = time.perf_counter()
print("Saved Parquet in {} seconds\n".format(parquet_save_end - parquet_save_start))

print("Loading Parquet")
print("===============")
# Load parquet
parquet_load_start = time.perf_counter()
df = pd.read_parquet('place2017.parquet')
parquet_load_end = time.perf_counter()
print("Loaded Parquet in {} seconds\n".format(parquet_load_end - parquet_load_start))

results = results.append({'format': 'parquet', 'load': parquet_load_end - parquet_load_start, 'save': parquet_save_end - parquet_save_start}, ignore_index=True)

print(results)

results.to_csv('place2017_results.csv')
