import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier

with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    mlflow.sklearn.log_model(model, "modelo_fraude")
    mlflow.log_metric("accuracy", accuracy_score(y_test, model.predict(X_test)))

# drift_report.py
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=ref_df, current_data=curr_df)
report.save_html("monitoring/report.html")
