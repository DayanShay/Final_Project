import allure
def screenshot_if_faild(driver, request,sys_use) -> None:
    """
    screenshot_if_faild takes a screenshot if a test faild
    """
    if sys_use == "selenium":
        if request.node.rep_call.failed:
            # Make the screen-shot if test failed:
            try:
                driver.execute_script("document.body.bgColor = 'white';")

                allure.attach(driver.get_screenshot_as_png(),
                              name=request.function.__name__,
                              attachment_type=allure.attachment_type.PNG)
            except:
                pass  # just ignore
    elif sys_use == "playwright":
        if request.node.rep_call.failed:
            # Make the screen-shot if test failed:
            try:
                driver.evaluate("document.body.bgColor = 'white';")

                allure.attach(driver.screenshot(path="screenshot.png"),
                              name=request.function.__name__,
                              attachment_type=allure.attachment_type.PNG)
            except:
                pass  # just ignore