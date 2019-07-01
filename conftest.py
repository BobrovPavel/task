import os
import pytest
import time
from reports import logger
from application import Application

logger = logger.get_logger()
fixture = None


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    fixture = Application(browser=browser)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def take_screenshot_when_failure(request):
    def tear_down():
        path = os.path.dirname(__file__)
        abspath = path.split("task", 1)[0]
        testname = request.node.name
        if request.node.rep_call.failed:
            logger.info("Make screenshot when failure")
            '''
            Где 'task' - корневая директория проекта. 
            Сделано это для того, что бы сохранение логов и скринов работало одинаково
            при запуске из различных мест проекта.
            Например из: $../task и $../task/tests или же при помощи ide
            '''
            fixture.driver.save_screenshot("%s/task/reports/screenshots/%sscreenshot_%s.png" % (abspath, time.time(), testname))

    request.addfinalizer(tear_down)
    yield
