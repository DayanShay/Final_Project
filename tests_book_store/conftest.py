import json
import pytest
import os

def get_data_for_test() -> json:
    """
    preparing data for the tests2 from json file.
    :return: json : data for tests2.
    """
    file_location = os.path.abspath("test_configuration.json").replace("tests_book_store\\","")
    with open(file_location) as file_root:
        file_json_data = json.load(file_root)
    return file_json_data



def pytest_addoption(parser):
    data_for_test = get_data_for_test()
    parser.addoption("--url",action="store",default=data_for_test["url"])
    parser.addoption("--browse",action="store",default=data_for_test["browse"])
    parser.addoption("--sys_use",action="store",default=data_for_test["sys_use"])
    parser.addoption("--remote",action="store",default=data_for_test["remote"])
    parser.addoption("--remote_url",action="store",default=data_for_test["remote_url"])
    parser.addoption("--api_url",action="store",default=data_for_test["api_url"])



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

