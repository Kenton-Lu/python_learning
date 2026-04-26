from google.cloud import bigquery
from sklearn.ensemble import IsolationForest
import pandas as pd

client = bigquery.Client(project="aiops-sre-assistant")

query = """
SELECT
  timestamp,
  cpu_usage,
  memory_usage,
  disk_usage
FROM `aiops-sre-assistant.aiops_metrics.vm_metrics`
ORDER BY timestamp
LIMIT 1000
"""

df = client.query(query).to_dataframe()

features = df[["cpu_usage", "memory_usage", "disk_usage"]]

model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df["anomaly"] = model.fit_predict(features)

print(df[df["anomaly"] == -1])

