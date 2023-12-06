from statsmodels.tsa.api import VAR
import pandas as pd


def predict_next_30_days(df):
    print("Start predict_next_30_days")
    pred_df = pd.DataFrame()
    try:
        # df = make_data_stationary(df)
        model = VAR(df)
        fitted_model = model.fit()
        lag_order = fitted_model.k_ar
        pred_values = fitted_model.forecast(df.values[-lag_order:], steps=30)
        # Create a DataFrame with predicted values and maintain the date index
        date_rng = pd.date_range(
            start=df.index[-1] + pd.DateOffset(1), periods=30, freq="D"
        )
        pred_df = pd.DataFrame(pred_values, index=date_rng, columns=df.columns)
    except Exception as e:
        print(f"Error while predicting next 30 days: {e}")
    finally:
        print("End predict_next_30_days")
        return pred_df


def make_data_stationary(df):
    df_differenced = df.diff().dropna()
    return df_differenced
