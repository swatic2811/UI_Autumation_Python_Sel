from utils.ConfigReaderUtil import ConfigReaderUtil
from utils.logger import LOGGER
from datetime import datetime
import pytest
import os
import allure
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

today = datetime.today()
date = today.strftime("%d_%m_%Y")
timestamp = today.strftime("%d_%m_%Y_%H_%M_%S")


@pytest.fixture(scope="class")
def setup(request):
    browsername= ConfigReaderUtil.get_env_value('browserName')
    if browsername == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browsername == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print("Browser not supported")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()


@pytest.fixture
def test_data(request):
    data = get_test_data('test_data.json')
    request.cls.data = data


def get_test_data(filename):
    folder_path = os.path.abspath(os.path.dirname(__file__))
    folder = os.path.join(folder_path, 'testdata')
    jsonfile = os.path.join(folder, filename)
    with open(jsonfile) as file:
        data = json.load(file)
    return data

@pytest.fixture
def logger_init():
    folder_path = os.path.abspath(os.path.dirname(__file__))
    finalfolderPath = os.path.join(folder_path.replace("\\tests", ""), 'testresults')
    folderpath = "{folder}\\{date}".format(
        folder=finalfolderPath,
        date=date
    )
    path =folderpath
    try:
        if not os.path.exists(folderpath):
            os.mkdir(folderpath)
            path = "{folder}\\{date}".format(folder=finalfolderPath,date=date)
    except OSError:
        print("Creation of the directory %s failed" % path + ".txt")
    log_file_full_name = os.path.join(path, 'logfile_{}.log'.format(timestamp))
    create_file(file_path=log_file_full_name)
    LOGGER.set_logger(log_file=log_file_full_name)
    LOGGER.get_logger().info("..............Intialized Logger Instance...............")

def create_file(file_path,mode_parameter="w"):
    with open(file=file_path,mode=mode_parameter) as f:
        pass

@pytest.fixture
def test_loginUsers(request):
    params = request.param
    name = params["username"]
    pwd = params["pwd"]
    allure.attach(f"This is the parameter {params} passed by the test case")
    yield name, pwd


