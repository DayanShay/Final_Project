import json
import pytest
import allure

def get_data_for_test() -> json:
    """
    preparing data for the tests from json file.
    :return: json : data for tests.
    """
    try:
        with open('.tests/test_configuration.json') as file_root:
            file_json_data = json.load(file_root)
    except FileNotFoundError:
        with open('test_configuration.json') as file_root:
            file_json_data = json.load(file_root)
    finally:
        return file_json_data


def pytest_addoption(parser):
    data_for_test = get_data_for_test()
    parser.addoption("--url",action="store",default=data_for_test["url"])
    parser.addoption("--browse",action="store",default=data_for_test["browse"])
    parser.addoption("--path_driver",action="store",default=data_for_test["path_driver"])
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

def screenshot_if_faild(driver, request) -> None:
    """
    screenshot_if_faild takes a screenshot if a test faild
    """

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore