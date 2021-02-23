Saifs-MacBook-Pro:Python_random saifmustafa$ ls
03_classification.ipynb
AAPL Historical Data_SEPT_OCT_2020.csv
Books_small.json
Books_small_10000.json
COVID_using_pandas.py
Decorators_example.py
Dict_to_JSON.py
ECiP_1.py
ECiP_10.py
ECiP_9.py
FLASK
Fibonacci_GoldenRatio.py
HANDSONML_1.py
HANDSONML_2.py
HANDSONML_4.py
Lumberjack.Log
MUNISHA_1.py
MUNISHA_2.py
Permutations.py
RANDOM.py
RANDOM.textClipping
RANDOMDATA.txt
RANDOM_Langtons_Ant.py
RANDOM_MAP_FILTER_REDUCE_examples.py
RANDOM_arrays.py
RANDOM_bubblesort.py
RANDOM_complex_boolean.py
RANDOM_datetime_examples.py
RANDOM_dictionaries.py
RANDOM_functions_example.py
RANDOM_if_stringlength_example.py
RANDOM_if_then_integer_example.py
RANDOM_if_then_trianglesides_example.py
RANDOM_lambda_scifi_auth_quadratic.py
RANDOM_listcomprehension.py
RANDOM_logging.py
RANDOM_map_lambda_examples.py
RANDOM_pandas.py
RANDOM_plotting_linear_bar.py
RANDOM_withopen_ocean_example.py
Reviews_Machinelearning.py
STOCKPRICE_prediction_APPLE.py
Selenium
Sigmoid.py
StandardModel_python
Suhail_drone_challenge.py
Tello_DRONE
TensorFlow_2.py
TensorFlow_Convolution_NeuralNetwork.py
TensorFlow_fashion_Sequential_NeuralNetwork.py
TensorFlow_titanic1.py
WORKSPACE
__pycache__
circles.py
circles.pyc
classes_example.py
data
datasets
matrix.txt
my graph.pdf
my graph.png
neural-nets-master
neural-nets-master.zip
oceans.txt
person.json
pokemon_data.csv
randomwalk_MonteCarlo.py
requirements.txt
simplependulum.py
sine_cosine_tangent_plot.py
tech_with_tim_2
tensorflow
test_circles.py
test_circles.pyc
theta_1_function.py
theta_1_function_coefficients.py
unixdict.txt
Saifs-MacBook-Pro:Python_random saifmustafa$ vi COVID_using_pandas.py 

import urllib.request


url = "https://covid19.who.int/WHO-COVID-19-global-data.csv"
file_path = os.path.join("data", "covid")

os.makedirs(file_path, exist_ok=True)
csv_path = os.path.join(file_path, "WHO-COVID-19-global-data.csv")
urllib.request.urlretrieve(url, csv_path)
df = pd.read_csv(csv_path)

#1

Date_reported1 = df.loc[(df.New_deaths > 1000) & (df.Country_code == 'GB')][ "Date_reported"]

Cumulative_deaths = df.loc[(df.New_deaths > 1000) & (df.Country_code == 'GB')][ "Cumulative_deaths"]

#print(Date_reported1, Cumulative_deaths)

#plt.plot(Date_reported1, Cumulative_deaths)

#2

Date_reported2 = df.loc[(df.Country_code == 'GB')]['Date_reported']

New_deaths = df.loc[(df.Country_code == 'GB')]['New_deaths']

print(Date_reported2)
print(New_deaths)

plt.title('COVID-19 New Deaths reported per day in The United Kingdom')
plt.xlabel('Days since start of pandemic in The United Kingdom')
plt.ylabel('Number of reported Deaths')


plt.plot(Date_reported2, New_deaths, label='Latest data from The WHO')
plt.legend()
plt.show()

