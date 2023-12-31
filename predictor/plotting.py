import matplotlib.pyplot as plt


def plot_prediction(hist_df, pred_df):
    print("Start plot_prediction")
    try:
        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(hist_df.index, hist_df["close"], label="Historical", color="blue")
        plt.plot(pred_df.index, pred_df["Predictions"], label="Prediction", color="red")

        # Connect last point of historical data with first point of prediction
        plt.plot(
            [hist_df.index[-1], pred_df.index[0]],
            [hist_df["close"].iloc[-1], pred_df["Predictions"].iloc[0]],
            color="red",
        )

        # Customize the plot
        plt.title("Plotting historical and predicted data")
        plt.xlabel("Date")
        plt.ylabel("Close")
        plt.legend()

        # Show the plot
        plt.show()
    except Exception as e:
        print(f"Error while plotting prediction: {e}")
    finally:
        print("End plot_prediction")
