import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Aufgabe 1: Laden der Daten
# Falls keine lokale Datei vorhanden ist, hier eine Beispiel-URL:
url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
df = pd.read_csv(url)

# Aufgabe 2: Trennung in Features (X) und Zielvariable (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Aufgabe 3: Split in Trainings- und Testdaten (75% / 25%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Aufgabe 4: Initialisierung des Modells
# Erhöhung von max_iter, um Konvergenzwarnungen zu vermeiden
model = LogisticRegression(max_iter=1000)

# Aufgabe 5: Training des Modells
model.fit(X_train, y_train)

# Aufgabe 6: Vorhersagen treffen
y_pred = model.predict(X_test)

# Aufgabe 7: Auswertung
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy Score: {accuracy:.4f}")
print("Confusion Matrix:")
print(conf_matrix)