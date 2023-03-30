# stock_price_comparision
## Today's at the moment stock data analysis
This notebook looks at today's at the moment stock data, to find the top five largest stocks by 3 month average volume for a particular time. Use yfinance to get information about each of those stocks, and use data visualization to see how each of those stocks is performing for the past year. The goal is to check to see when the stock had it's highest and lowest price. Looking at one of those five stocks for a period of one year, this notebook shows the closing and opening price from the last
time the data was scrapped, and goes back daily for one year. 

**Dates and times are subject to the stock trading calendar.**

### Important Note: 
Each time the code is run, new stocks could be present because the code webscrapes from the website using .read_html. During trading hours, most active, gainers and losers change over time. As a result, some of the queries might not be displaying any results. 

### To view the project
Option 1:
        Clone the Github repository to your local machine and follow the packages listed below or the requirements.txt
        Click on moment_stock_data.ipynb

Option 2:
        Click on the link: https://colab.research.google.com/github/pdizdar/stock_price_comparision/blob/master/colab_moment_stock_data.ipynb
        or in GitHub stock_price_comparision repository select colab_moment_stock_data.ipynb, once inside click on Open in colab link. Click the runtime tab, then click run all tab. This will run the entire project. 

### Packages that need to be installed to run this project
Download the latest version of python from https://www.python.org/downloads/ and follow the recommended steps.
   
##### Follow the steps below to install the Jupyter Notebook package on macOS using pip:
Step 1: Install the latest Python3 in MacOS

Step 2: Check if pip3 and python3 are correctly installed.
        python3 --version
        pip3 --version

Step 3: Upgrade your pip to avoid errors during installation.
        pip3 install --upgrade pip

Step 4: Enter the following command to install Jupyter Notebook using pip3.
        pip3 install jupyter
        
Step 5: Enter the command jupyter notebook in your terminal to start up Jupyter Notebook.

##### Other libraries
pip3 install pandas
pip3 install matplotlib
pip3 install yfinance
pip3 install plotly
pip3 install -U pytest
pip3 install pigar

#### To install Jupyter  notebook, pandas and matplotlib using pip on windows, we need to first check if pip is updated in our system. Use the following command to update pip:
python -m pip install --upgrade pip
python -m pip install jupyter
pip install pandas
pip install matplotlib
pip install yfinance
pip install plotly
pip install -U pytest 
pip install pigar

##### To run pytest
pip install -U pytest
There are four functions to test on test_convert_scale.py file.
To run this test successfully type pytest in the terminal and press enter.

##### To generate requirements.txt file for only this file
pip install pigar
On terminal enter pigar generate and enter, it will create requirements.txt file for you.

### 5+ features I have included from the project requirements list.
Feature 1. Read in 3 datasets from https://finance.yahoo.com/ using Pandas read_html functions.

Feature 2. Concatenated the datasets to create one dataframe, used a custom function to make conversions, find and deleted duplicate rows.

Feature 2.1 Analysed data to answer 7 questions.

Feature 3. Visualized data through interactive plotly graphs.

Feature 4. Created four unit tests

Feature 5. Added Markdowns on JupyterNotebook and description of the graphs.

### Note:
Google Colab uses UTC timezone, which is 5 hours ahead of Eastern Time Zone. 
Time difference is 4 hours during Daylight Savings Time.

