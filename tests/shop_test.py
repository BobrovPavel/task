import pytest


@pytest.fixture(scope="class")
def class_setup(app):
    app.driver.get("https://shop.by/")
    app.base.wait_banner()


@pytest.mark.usefixtures("class_setup", "take_screenshot_when_failure")
class TestShopBy:

    def test_shop_by(self, app):
        app.base.open_notebook_page()
        app.catalog.apply_filters()
        app.catalog.show_result()
        compare = app.catalog.compare_product_list_size()
        app.catalog.sort_by_price_up()
        cheap_book = app.catalog.get_first_book_name_on_page()
        app.catalog.sort_by_price_down()
        last_book = app.catalog.get_last_book_name_on_page()
        assert cheap_book in last_book and compare, \
            "Notebook names do not match: \n " \
            "Expect name: %s \n " \
            "Actual name: %s\n " \
            "Products number is equal: %s" \
            % (cheap_book, last_book, compare)
