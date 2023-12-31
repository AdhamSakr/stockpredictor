import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
import warnings

warnings.filterwarnings("ignore")


def predict_next_30_days(df):
    print("Start predict_next_30_days")
    predictions_df = pd.DataFrame()
    feature_columns = df.columns.difference(["close"])
    target_column = "close"
    try:
        # Split dataframe into features (X) and target (y)
        X = df[feature_columns]
        y = df[target_column]

        # Scale features
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)

        # Train model
        svr_model = SVR(kernel="poly")
        svr_model.fit(X_scaled, y)

        future_dates = pd.date_range(start=df.index.max(), periods=30, freq="D")

        # Predict the target values for the next 30 days
        predicted_values = []

        for date in future_dates:
            future_features = get_features_for_date(df, date, feature_columns)
            future_scaled = scaler.transform([future_features])
            predicted_value = svr_model.predict(future_scaled)
            predicted_values.append(predicted_value[0])

        predictions_df = pd.DataFrame(
            index=future_dates, data={"Predictions": predicted_values}
        )
    except Exception as e:
        print(f"Error while predicting next 30 days: {e}")
    finally:
        print("End predict_next_30_days")
        return predictions_df


def get_features_for_date(df, date, feature_columns, window_size=30):
    # Calculate rolling averages for each feature
    relevant_data = df[df.index >= (date - pd.DateOffset(days=window_size))]
    rolling_averages = relevant_data[feature_columns].mean()
    return rolling_averages.values
