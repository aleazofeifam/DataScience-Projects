# Prepare training data
# ...
from flaml import AutoML
automl = AutoML()
automl.fit(X_train, y_train, task="regression", time_budget=60, **other_settings)
# Save the model
with open("automl.pkl", "wb") as f:
    pickle.dump(automl, f, pickle.HIGHEST_PROTOCOL)

# At prediction time
with open("automl.pkl", "rb") as f:
    automl = pickle.load(f)
pred = automl.predict(X_test)