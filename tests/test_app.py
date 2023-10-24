from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")


"""
Get home
Returns page with title
"""
def test_request_returns_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    
    strong_tag = page.locator("h2")

    expect(strong_tag).to_have_text("Welcome to MakersB&B")

"""
Homepage has user sign up UI
"""
def test_request_homepage_has_correct_ui(page, test_web_address):
    page.goto(f"http://{test_web_address}/")

    email_input = page.locator('input[name="email"]')
    assert email_input.is_visible()

    password_input = page.locator('input[name="password"]')
    assert password_input.is_visible()

    password_confirmation_input = page.locator('input[name="password_confirmation"]')
    assert password_confirmation_input.is_visible()

    submit_button = page.locator('input[type="submit"]')
    assert submit_button.is_visible()

"""
Log-in page has user log-in UI
"""
def test_request_login_page_has_correct_ui(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    # page.get_by_role("link", name="login").click()
    # expect (page.goto(f"http://{test_web_address}/login"))

    email_input = page.locator('input[name="email"]')
    assert email_input.is_visible()

    password_input = page.locator('input[name="password"]')
    assert password_input.is_visible()

    submit_button = page.locator('input[type="submit"]')
    assert submit_button.is_visible()