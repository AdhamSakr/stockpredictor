import pandas as pd
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler
from copy import deepcopy

num_lags = 30


def predict_next_30_days(df):
    print("Start predict_next_30_days")
    future_predictions_df = pd.DataFrame()
    try:
        df = create_lagged_features(df)

        df = df.fillna(df.mean())

        # Split dataframe into features (X) and target (y)
        X, y = split_dataframe(df)

        # Scale features
        X_scaled = scale_features(X)

        # Train model
        svr = SVR(kernel="poly")
        svr.fit(X_scaled, y)

        extended_df = extend_dataframe_by_30_business_days(df)

        # Fill future feature values using interpolation
        extended_df = interpolate_future_features(extended_df)

        # Select the future part from the dataframe now that the features have been filled
        future_df = extended_df.query("isFuture").copy()

        # Make prediction
        future_predictions_df = predict_future_target(svr, future_df)
    except Exception as e:
        print(f"Error while predicting next 30 days: {e}")
    finally:
        print("End predict_next_30_days")
        return future_predictions_df


def create_lagged_features(df):
    print("Start create_lagged_features")
    lagged_columns = []
    df_shifting = deepcopy(df)
    for column in df.columns:
        for i in range(1, num_lags + 1):
            df_temp = pd.DataFrame({f"{column}_lag_{i}": df_shifting[column].shift(i)})
            lagged_columns.append(df_temp)
    lagged_df = pd.concat(lagged_columns, axis=1)
    df = pd.concat([df, lagged_df], axis=1)
    print("End create_lagged_features")
    return df


def split_dataframe(df):
    print("Start split_dataframe")
    X = df.drop("close", axis=1)
    y = df["close"]
    print("End split_dataframe")
    return X, y


def scale_features(df):
    print("Start scale_features")
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df)
    print("End scale_features")
    return df_scaled


def extend_dataframe_by_30_business_days(df):
    print("Start extend_dataframe_by_30_business_days")
    future_idx = pd.date_range(
        start=df.index[-1] + pd.Timedelta(days=1), periods=num_lags, freq="B"
    )
    future_df = pd.DataFrame(index=future_idx)
    future_df["isFuture"] = True
    df["isFuture"] = False
    df_and_future = pd.concat([df, future_df])
    print("End extend_dataframe_by_30_business_days")
    return df_and_future


def interpolate_future_features(df):
    print("Start interpolate_future_features")
    columns_to_interpolate = df.columns.difference(["close", "isFuture"])
    df[columns_to_interpolate] = df[columns_to_interpolate].interpolate(
        method="spline", order=2
    )
    print("End interpolate_future_features")
    return df


def predict_future_target(model, df):
    print("Start predict_future_target")
    FEATURES = df.columns.difference(["close", "isFuture"])
    df_scaled = scale_features(df[FEATURES])
    future_predictions = model.predict(df_scaled)
    future_predictions_df = pd.DataFrame(
        index=df.index, data={"close_pred": future_predictions}
    )
    print("End predict_future_target")
    return future_predictions_df
