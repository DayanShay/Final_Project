import json

def get_data_for_test() -> json:
    """
    preparing data for the tests from json file.
    :return: json : data for tests.
    """
    try:
        with open('.tests/data.json') as file_root:
            file_json_data = json.load(file_root)
    except:
        with open('data.json') as file_root:
            file_json_data = json.load(file_root)
    finally:
        return file_json_data


def pytest_addoption(parser):
    data_for_test = get_data_for_test()
    parser.addoption("--url",action="store",default=data_for_test["url"])
    parser.addoption("--browse",action="store",default=data_for_test["browse"])
    parser.addoption("--path_driver",action="store",default=data_for_test["path_driver"])
    parser.addoption("--sys_use",action="store",default=data_for_test["sys_use"])


