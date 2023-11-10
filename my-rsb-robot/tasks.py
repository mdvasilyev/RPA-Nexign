from robocorp.tasks import task
from robocorp import browser
from RPA.Windows import Windows

library = Windows()

@task
def test_do_some_calculations():
    library.windows_run("calc.exe")
    try:
        library.control_window("name:Калькулятор")
        library.click("id:clearButton")
        library.send_keys(keys="96+4=")
        result = library.get_attribute("id:CalculatorResults", "Name")
        print(result)
    finally:
        library.close_current_window()

@task
def access_mail():
    browser.configure(
        slowmo=100,
    )
    browser.goto("https://mail.ru/")