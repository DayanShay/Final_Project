
import allure

def screenshot_if_faild(driver, request) -> None:
    """
    screenshot_if_faild takes a screenshot if a test faild
    """
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            allure.attach(driver.get_screen_shoot(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass  # just ignore