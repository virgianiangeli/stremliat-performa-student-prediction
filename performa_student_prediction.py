# -*- coding: utf-8 -*-
"""performa student prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JM6rnPe6fRToM0C7VF-2Nz6CzBSJ2pHO

# buatlah model untuk prediksi harga mobil dengan  3 alogaritma,beserta evaluasinya

##

## # Load library
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from google.colab import drive

"""## # 2. Load datasets"""

# Hubungkan ke Google Drive
drive.mount('/content/drive')

# Masukkan path dataset
data_path = '/content/drive/MyDrive/Colab_Notebooks/baru/data.csv'  # Ganti dengan path dataset Anda
df = pd.read_csv(data_path)

"""## # 3. Sneak peek data"""

print("5 Data Teratas:")
print(df.head())

print("\nInformasi Dataset:")
print(df.info())

print("\nStatistik Deskriptif:")
print(df.describe())

"""## # 4. Handling Missing Values"""

print("\nJumlah Missing Values per Kolom:")
print(df.isnull().sum())

# Isi missing values dengan rata-rata kolom
df.fillna(df.mean(), inplace=True)

"""## # 5. Exploratory Data Analysis (EDA)"""

# Korelasi antar fitur
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Korelasi Antar Fitur")
plt.show()

# Distribusi harga mobil ('price')
plt.figure(figsize=(8, 6))
sns.histplot(df['price'], kde=True, bins=30, color="blue")
plt.title("Distribusi Harga Mobil (price)")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Scatter plot horsepower vs price
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['horsepower'], y=df['price'], color='green', alpha=0.7)
plt.title("Horsepower vs Price")
plt.xlabel("Horsepower")
plt.ylabel("Price")
plt.show()

"""## # 6. Modeling"""

# Memisahkan fitur (X) dan target (y)
X = df.drop(columns='price')  # 'Price' adalah kolom target
y = df['price']

# Membagi dataset menjadi data latih dan uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model Gradient Boosting Regressor
gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
gb_model.fit(X_train, y_train)

# Prediksi pada data uji
y_pred = gb_model.predict(X_test)

"""## # 7. Evaluasi Model"""

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n=== Evaluasi Model Gradient Boosting Regressor ===")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R2 Score (Accuracy): {r2:.2%}")

"""## # 8. Visualisasi Prediksi"""

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.title("Hasil Prediksi vs Nilai Aktual")
plt.xlabel("Nilai Aktual")
plt.ylabel("Nilai Prediksi")
plt.show()

"""# Model 2 model  Support Vector Regressor (SVR),

## # Step 1: Load Library
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score
from google.colab import drive

"""## # Step 2: Load Dataset"""

# Hubungkan Google Drive
drive.mount('/content/drive')

# Pastikan file dataset ada di Google Drive Anda dan sesuaikan path-nya
file_path = '//content/drive/MyDrive/Colab_Notebooks/baru/data.csv'  # Sesuaikan path-nya
df = pd.read_csv(file_path)

"""## # Step 3: Sneak Peek Data"""

print(df.head())
print(df.info())
print(df.describe())

"""## # Step 4: Handling Missing Values"""

# Cek missing values
print("\nMissing Values:\n", df.isnull().sum())

# Menghapus baris dengan missing values pada kolom penting seperti 'horsepower' dan 'price'
df = df.dropna(subset=['horsepower', 'price'])

"""## # Step 5: Exploratory Data Analysis (EDA)"""

# Distribusi fitur 'price'
sns.histplot(df['price'], kde=True, bins=30)
plt.title('Distribusi Harga Mobil')
plt.show()

# Scatterplot harga vs horsepower
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['horsepower'], y=df['price'])
plt.title('Horsepower vs Price')
plt.xlabel('Horsepower')
plt.ylabel('Price')
plt.show()

# Korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

"""## # Step 6: Preprocessing dan Modelling"""

# Cek kolom yang tersedia dalam dataset
print("Kolom yang tersedia:", df.columns)

# Memisahkan fitur (X) dan target (y)
X = df[['horsepower']]  # Gunakan kolom yang tersedia
y = df['price']

# Split data menjadi train dan test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Shape X_train:", X_train.shape)
print("Shape X_test:", X_test.shape)
print("Shape y_train:", y_train.shape)
print("Shape y_test:", y_test.shape)

"""## # Step 7: Evaluasi Model"""

# Definisikan model SVR
model = SVR(kernel='linear')

# Latih model
model.fit(X_train, y_train)

# Prediksi
y_pred = model.predict(X_test)

# Evaluasi
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Plot hasil prediksi vs nilai aktual
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
plt.title('Hasil Prediksi vs Nilai Aktual')
plt.xlabel('Harga Aktual')
plt.ylabel('Harga Prediksi')
plt.show()

"""# MODEL 3 XGBoost Regressor

# langkah Load Library
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from xgboost import XGBRegressor
from google.colab import drive

# Hubungkan ke Google Drive
drive.mount('/content/drive')

"""## # **2. Load Datasets**"""

file_path = '//content/drive/MyDrive/Colab_Notebooks/baru/data.csv'  # Sesuaikan dengan path di Google Drive Anda
df = pd.read_csv(file_path)

"""## **3. Sneak Peek Data**"""

print(df.head())
print("\nInformasi Dataset:")
print(df.info())
print("\nStatistik Deskriptif:")
print(df.describe())

"""## **4. Handling Missing Values**"""

# Debugging: Periksa nama kolom
print("Kolom dalam DataFrame:", df.columns)

# Debugging: Cek missing values per kolom
print("Jumlah Missing Values:")
print(df.isnull().sum())

# Pastikan nama kolom di subset sesuai dengan yang ada dalam DataFrame
subset_columns = ['horsepower', 'price']  # Hapus 'curb-weight' jika tidak ada
if 'curb-weight' in df.columns:
    subset_columns.append('curb-weight')  # Indentasi diperbaiki di sini

# Menghapus baris dengan missing values pada kolom yang valid
df = df.dropna(subset=subset_columns)

# Debugging: Periksa kembali setelah dropna
print("DataFrame setelah dropna:")
print(df.head())

"""## # **5. Exploratory Data Analysis (EDA)**"""

# Distribusi target
sns.histplot(df['price'], kde=True, bins=30)
plt.title("Distribusi Harga Mobil")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# Korelasi antar fitur
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

"""##  Modelling**"""

# Periksa nama kolom yang ada dalam DataFrame
print("Nama Kolom dalam DataFrame:", df.columns)

# Pastikan kolom yang digunakan ada dalam DataFrame
selected_columns = ['horsepower', 'curb-weight', 'engine-size']

# Cek jika kolom ada di dalam DataFrame
missing_columns = [col for col in selected_columns if col not in df.columns]
if missing_columns:
    print(f"Kolom berikut tidak ditemukan: {missing_columns}")
else:
    # Memisahkan fitur (X) dan target (y) jika semua kolom ada
    X = df[['horsepower', 'curb-weight', 'engine-size']]
    y = df['price']
    print("Fitur dan target berhasil dipisahkan.")

"""## **7. Evaluasi**"""

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mse)
print("R² Score:", r2)

# Visualisasi Prediksi vs Realita
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--')
plt.title("Real vs Predicted Prices")
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.show()

"""# Buatlah tambahan  3 alogaritma untuk prediksi  gaji beserta evaluasinya

## # Langkah 1: Hubungkan dengan Google Drive

## model 1 linier regresion
"""

from google.colab import drive
drive.mount('/content/drive')

"""## # Langkah 2: Load Library"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""## # Langkah 3: Load Dataset"""

# Buat dataset atau pastikan ada file di Google Drive, misal 'gaji_data.csv'
try:
    file_path = '/content/drive/My Drive/gaji_data.csv'  # Ubah ke path file Anda
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    # Jika tidak ada dataset, buat dummy dataset
    data = {'Tahun_bekerja': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'Gaji': [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500]}
    df = pd.DataFrame(data)
    df.to_csv('/content/drive/My Drive/gaji_data.csv', index=False)
    print("Dummy dataset created and saved to Google Drive!")

"""## # Langkah 4: Sneak Peek Dataset"""

print("First few rows of the dataset:")
print(df.head())

"""## Langkah 5: Exploratory Data Analysis (EDA)"""

plt.scatter(df['Tahun_bekerja'], df['Gaji'], color='blue')
plt.title('Hubungan Lama Kerja dengan Gaji')
plt.xlabel('Tahun Bekerja')
plt.ylabel('Gaji')
plt.show()

"""## Langkah 6: Pisahkan Data (Feature dan Target)"""

X = df[['Tahun_bekerja']]  # Feature
y = df['Gaji']             # Target

# Split data menjadi train dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""## Langkah 7: Modeling (Regresi Linier)"""

model = LinearRegression()
model.fit(X_train, y_train)

"""## Langkah 8: Evaluasi Model"""

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2 Score): {r2}")

# Visualisasi hasil prediksi
plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.plot(X_test, y_pred, color='red', label='Predicted Line')
plt.title('Actual vs Predicted Gaji')
plt.xlabel('Tahun Bekerja')
plt.ylabel('Gaji')
plt.legend()
plt.show()

"""## Langkah 9: Simpan Model atau Dataset (Opsional)"""

import joblib
model_path = '/content/drive/My Drive/linear_model_gaji.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")

"""# model Polynomial Regression

## # Langkah 1: Hubungkan dengan Google Drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""## # Langkah 2: Load Library"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

"""## # Langkah 3: Load Dataset

"""

try:
    # Ganti path ini sesuai dengan file di Google Drive Anda
    file_path = '/content/drive/My Drive/gaji_data.csv'
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    # Jika tidak ada dataset, buat dataset dummy
    data = {
        'Tahun_bekerja': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Gaji': [3000, 3500, 4000, 4500, 5000, 6000, 6500, 7200, 8000, 9000]
    }
    df = pd.DataFrame(data)
    df.to_csv('/content/drive/My Drive/gaji_data.csv', index=False)
    print("Dummy dataset created and saved to Google Drive!")

"""## # Langkah 4: Sneak Peek Dataset"""

print("\nFirst few rows of the dataset:")
print(df.head())

"""## # Langkah 5: Exploratory Data Analysis (EDA)"""

plt.scatter(df['Tahun_bekerja'], df['Gaji'], color='blue')
plt.title('Hubungan Lama Kerja dengan Gaji')
plt.xlabel('Tahun Bekerja')
plt.ylabel('Gaji')
plt.show()

"""## # Langkah 6: Pisahkan Data (Feature dan Target)"""

X = df[['Tahun_bekerja']]  # Feature
y = df['Gaji']             # Target

# Split data menjadi train dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""## # Langkah 7: Transformasi Polynomial Features"""

degree = 2  # Derajat polinomial
poly = PolynomialFeatures(degree=degree)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

"""## # Langkah 8: Modeling (Polynomial Regression)"""

model = LinearRegression()
model.fit(X_train_poly, y_train)

"""## # Langkah 9: Evaluasi Model"""

y_pred = model.predict(X_test_poly)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Degree of Polynomial: {degree}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2 Score): {r2}")

"""## # Langkah 10: Visualisasi Hasil"""

plt.scatter(X, y, color='blue', label='Actual Data')
X_range = np.linspace(X['Tahun_bekerja'].min(), X['Tahun_bekerja'].max(), 100).reshape(-1, 1)
y_range_pred = model.predict(poly.transform(X_range))
plt.plot(X_range, y_range_pred, color='red', label='Polynomial Fit')
plt.title('Actual vs Predicted Gaji (Polynomial Regression)')
plt.xlabel('Tahun Bekerja')
plt.ylabel('Gaji')
plt.legend()
plt.show()  # Pastikan tanda kurung lengkap

"""## # Langkah 11: Simpan Model ke Google Drive"""

import joblib
model_path = '/content/drive/My Drive/polynomial_model_gaji.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")

"""## model 3 Decision Tree Regressor

## # Langkah 1: Hubungkan dengan Google Drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""## # Langkah 2: Load Library"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

"""## # Langkah 3: Load Dataset"""

try:
    # Ganti path ini sesuai dengan file di Google Drive Anda
    file_path = '/content/drive/My Drive/gaji_data.csv'
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    # Jika tidak ada dataset, buat dataset dummy
    data = {
        'Tahun_bekerja': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Gaji': [3000, 3500, 4000, 4500, 5000, 6000, 6500, 7200, 8000, 9000]
    }
    df = pd.DataFrame(data)
    df.to_csv('/content/drive/My Drive/gaji_data.csv', index=False)
    print("Dummy dataset created and saved to Google Drive!")

"""## # Langkah 4: Sneak Peek Dataset"""

print("\nFirst few rows of the dataset:")
print(df.head())  # Perbaikan di sini: pastikan kurung penutup ditambahkan

"""## # Langkah 5: Exploratory Data Analysis (EDA)"""

plt.scatter(df['Tahun_bekerja'], df['Gaji'], color='blue')
plt.title('Hubungan Lama Kerja dengan Gaji')
plt.xlabel('Tahun Bekerja')
plt.ylabel('Gaji')
plt.show()

"""## # Langkah 6: Pisahkan Data (Feature dan Target)"""

X = df[['Tahun_bekerja']]  # Feature
y = df['Gaji']             # Target

# Split data menjadi train dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""## # Langkah 7: Modeling (Decision Tree Regressor)"""

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

"""## # Langkah 8: Evaluasi Model"""

y_pred = model.predict(X_test)

# Evaluasi menggunakan MSE dan R2 Score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error (MSE): {mse}")
print(f"R-squared (R2 Score): {r2}")

"""## # Langkah 9: Visualisasi Hasil Prediksi"""

plt.scatter(X_test, y_test, color='blue', label='Actual Data')
plt.scatter(X_test, y_pred, color='red', label='Predicted Data')
plt.title('Actual vs Predicted Gaji (Decision Tree)')
plt.xlabel('Tahun Bekerja')
plt.ylabel('Gaji')
plt.legend()
plt.show()

"""## # Langkah 10: Simpan Model ke Google Drive (Opsional)"""

model_path = '/content/drive/My Drive/decision_tree_model_gaji.pkl'
joblib.dump(model, model_path)
print(f"Model saved to {model_path}")