from selene import browser, be, have


def test_positive_search(url_browser,browser_conf):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[data-test-id="result-title"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_negative_search(url_browser,browser_conf):
    browser.element('[data-test-id="search-form-reset"]').press_enter()
    browser.element('[name="q"]').should(be.blank).type('тестопка').press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(have.text('Unfortunately we didn’t find any results for “тестопка”'))