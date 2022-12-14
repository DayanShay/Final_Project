from functions_and_fixtures.fixtures import *
from functions_and_fixtures.fixture_data import *
from functions_and_fixtures.functions import *


@pytest.mark.order(0)
class Test_login_and_register_features:
    @pytest.mark.parametrize("test_input,expected", [(USER_no_email_and_no_pass, Invalid_msg),
                                                     (USER_invalid_email_and_no_pass,
                                                      [Invalid_email_msg, Invalid_password_msg,
                                                       No_password_filled_msg]),
                                                     (USER_invalid_email_with_pass, [Invalid_email_msg]),
                                                     (USER_noemail_Generic_pass,
                                                      [Invalid_email_msg, No_email_filled_msg]),
                                                     (USER_noemail_invalid_low_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_noemail_invalid_high_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_withemail_invalid_low_password, [Invalid_password_msg]),
                                                     (USER_withemail_invalid_high_password, [Invalid_password_msg])
                                                     ])
    def test_register_on_Api_with_Invalid_data(self, get_base_url, get_api_UnAutho, get_to_main_page, test_input: dict,
                                               expected):
        api = get_api_UnAutho
        invalid_register_user = make_register_account(test_input)
        res_register_invalid = api.account.post_account(data=invalid_register_user)
        assert res_register_invalid["code"] == 400
        for msg in expected:
            assert msg in res_register_invalid["msg"]
        invalid_login_user = make_login_account(invalid_register_user)
        res_login_invalid = api.account.post_login(data=invalid_login_user)
        for msg in expected:
            assert msg in res_login_invalid["msg"]
        page = get_to_main_page
        page.click_log_in()
        store_page = page.make_login(invalid_login_user)
        assert store_page.get_page_url() == get_base_url

    @pytest.mark.parametrize("test_input,expected", [(USER_no_email_and_no_pass, Invalid_msg),
                                                     (USER_invalid_email_and_no_pass,
                                                      [Invalid_email_msg, Invalid_password_msg,
                                                       No_password_filled_msg]),
                                                     (USER_invalid_email_with_pass, [Invalid_email_msg]),
                                                     (USER_noemail_Generic_pass,
                                                      [Invalid_email_msg, No_email_filled_msg]),
                                                     (USER_noemail_invalid_low_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_noemail_invalid_high_password,
                                                      [Invalid_email_msg, No_email_filled_msg, Invalid_password_msg]),
                                                     (USER_withemail_invalid_low_password, [Invalid_password_msg]),
                                                     (USER_withemail_invalid_high_password, [Invalid_password_msg])
                                                     ])
    def test_register_on_Website_with_Invalid_data(self, get_base_url, get_to_main_page, get_api_UnAutho, expected,
                                                   test_input: dict):
        page = get_to_main_page
        page.click_log_in()
        register_user = make_register_account(test_input)
        login_user = make_login_account(register_user)
        page.make_register(register_user)
        assert page.get_page_url() == f"{get_base_url}register"
        page.click_back_to_login()
        page.make_login(login_user)
        assert page.get_page_url() == f"{get_base_url}"
        api = get_api_UnAutho
        invalid_login_user = make_login_account(register_user)
        res_login_invalid = api.account.post_login(data=invalid_login_user)
        for msg in expected:
            assert msg in res_login_invalid["msg"]

    @pytest.mark.parametrize("test_input", [USER_Admin])
    def test_register_on_Website_with_Adminuser(self, get_base_url, get_to_main_page, get_api_UnAutho,
                                                test_input: dict):
        page = get_to_main_page
        page.click_log_in()
        register_user = make_register_account(test_input)
        login_user = make_login_account(register_user)
        page.make_register(register_user)
        assert page.get_page_url() == f"{get_base_url}register"
        page.click_back_to_login()
        store_page = page.make_login(login_user)
        api = get_api_UnAutho
        login_user = make_login_account(register_user)
        res_login = api.account.post_login(data=login_user)
        assert store_page.get_page_url() == f"{get_base_url}store"
        assert res_login.token is not None

    @pytest.mark.parametrize("test_input", [USER_testuser])
    def test_register_on_Website_with_Testuser(self, get_base_url, get_to_main_page, get_api_UnAutho, test_input: dict):
        page = get_to_main_page
        page.click_log_in()
        register_user = make_register_account(test_input)
        login_user = make_login_account(register_user)
        page.make_register(register_user)
        assert page.get_page_url() == f"{get_base_url}register"
        page.click_back_to_login()
        store_page = page.make_login(login_user)
        api = get_api_UnAutho
        login_user = make_login_account(register_user)
        res_login = api.account.post_login(data=login_user)
        assert store_page.get_page_url() == f"{get_base_url}store"
        assert res_login.token is not None

    @pytest.mark.parametrize("test_input", [USER_Admin])
    def test_register_on_API_with_valid_Adminuser(self, get_base_url, get_api_UnAutho, get_to_main_page,
                                                  test_input: dict):
        api = get_api_UnAutho
        register_user = make_register_account(test_input)
        res_register1 = api.account.post_account(data=register_user)
        assert res_register1 == 'OK'
        login_user = make_login_account(register_user)
        res_login = api.account.post_login(data=login_user)
        assert res_login.token is not None
        page = get_to_main_page
        page.click_log_in()
        store_page = page.make_login(login_user)
        assert store_page.get_page_url() == f"{get_base_url}store"

    @pytest.mark.parametrize("test_input", [USER_testuser])
    def test_register_on_API_with_Testuser(self, get_base_url, get_api_UnAutho, get_to_main_page,
                                                     test_input: dict):
        api = get_api_UnAutho
        register_user = make_register_account(test_input)
        res_register1 = api.account.post_account(data=register_user)
        assert res_register1 == 'OK'
        login_user = make_login_account(register_user)
        res_login = api.account.post_login(data=login_user)
        assert res_login.token is not None
        page = get_to_main_page
        page.make_register(register_user)
        page.click_log_in()
        store_page = page.make_login(login_user)
        assert store_page.get_page_url() == f"{get_base_url}store"

    @pytest.mark.parametrize("test_input", [USER_testuser, USER_Admin])
    def test_register_Dup_accounts_on_API(self, get_base_url, get_api_UnAutho, get_to_main_page, test_input: dict):
        api = get_api_UnAutho
        register_user = make_register_account(test_input)
        res_register1 = api.account.post_account(data=register_user)
        dup_msg = make_dup_user_msg(register_user.email)
        assert res_register1["msg"] == dup_msg
        login_user = make_login_account(register_user)
        res_login = api.account.post_login(data=login_user)
        assert res_login.token is not None
        page = get_to_main_page
        page.click_log_in()
        store_page = page.make_login(login_user)
        assert store_page.get_page_url() == f"{get_base_url}store"

