# stockpredictor
Master's degree graduation project

To run ETL Airflow Automation:
1- Make sure Docker Desktop is installed and running
2- Navigate to "airflow" folder
3- In the terminal run: docker compose up
4- In a web browser, navigate to "http://localhost:8080/" (username: airflow, password: airflow) (may take a minute to be working)
5- To stop the docker image, in a new terminal run: docker compose down
6- Another way is to install Docker extension for VS Code, and right click on the docker-compose.yaml file to start or stop.

To run the predictor:
1- Navigate to "predictor" folder
2- In the terminal run: python main.py