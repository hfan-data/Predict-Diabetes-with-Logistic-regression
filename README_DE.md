# Vorhersage von Diabetes mit logistischer Regression

Wenden Sie die im Unterricht erlernte logistische Regression auf einen neuen Datensatz aus der Praxis an. Das Ziel ist es, basierend auf diagnostischen Messwerten vorherzusagen, ob ein Patient an Diabetes leidet.

## Datenvorbereitung
Für diese Aufgabe müssen Sie den `diabetes.csv`-Datensatz herunterladen (er ist z. B. auf Kaggle oder im UCI Machine Learning Repository verfügbar) oder ihn direkt über eine URL mit `pandas` laden.

Der Datensatz enthält die folgenden medizinischen Variablen:
* Schwangerschaften (Pregnancies)
* Glukose (Glucose)
* Blutdruck (BloodPressure)
* Hautfaltendicke (SkinThickness)
* Insulin (Insulin)
* Body-Mass-Index (BMI)
* Diabetes-Stammbaumfunktion (DiabetesPedigreeFunction)
* Alter (Age)

### Aufgaben
* **Aufgabe 1**: Schreiben Sie ein Python-Skript, das die Daten in einen `pandas DataFrame` lädt.
* **Aufgabe 2**: Trennen Sie den Datensatz in Ihre Features (X) und die Zielvariable (y).
* **Aufgabe 3**: Teilen Sie den Datensatz in einen Trainingssatz (75%) und einen Testsatz (25%) auf. Verwenden Sie dabei einen `random_state` Ihrer Wahl.

## Modellerstellung und Auswertung
Verwenden Sie `scikit-learn`, um den im Unterricht gezeigten Modellierungsprozess nachzubilden.

* **Aufgabe 4**: Initialisieren Sie ein logistisches Regressionsmodell. Falls eine Warnung bezüglich der Konvergenz erscheint, müssen Sie den Parameter `max_iter` erhöhen.
* **Aufgabe 5**: Trainieren Sie das Modell mit Ihren Trainingsdaten.
* **Aufgabe 6**: Verwenden Sie das trainierte Modell, um Vorhersagen für Ihren Testdatensatz zu erstellen.
* **Aufgabe 7**: Berechnen und geben Sie sowohl den Accuracy Score als auch die Konfusionsmatrix (Confusion Matrix) aus.

## Kurze Reflexion
Nachdem Ihr Programm erfolgreich ausgeführt wurde, beantworten Sie die folgenden Fragen basierend auf Ihren Ergebnissen. Fügen Sie diese Antworten als Kommentar zu Ihrer Abgabe hinzu.

### Frage 1
Betrachten Sie Ihre Konfusionsmatrix. Wie viele **False Negatives** (Patienten, die tatsächlich Diabetes haben, die das Modell aber als gesund eingestuft hat) hat Ihr Modell erzeugt?

### Frage 2
Im Zusammenhang mit dem Brustkrebs-Datensatz ist ein False Negative extrem gefährlich (einem Patienten wird mitgeteilt, er sei krebsfrei, obwohl er tatsächlich Krebs hat). Welche realen Konsequenzen hat im Zusammenhang mit diesem Diabetes-Datensatz ein False Negative im Vergleich zu einem False Positive?
