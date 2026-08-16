from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.homepage import DashboardPage
from pages.profile_page import ProfilePage


def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("sneha", "password123")

    dashboard_page = DashboardPage(page)
    expect(dashboard_page.welcome_message).to_be_visible()
    expect(dashboard_page.welcome_message).to_have_text("Welcome, Sneha!")


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("ABC", "XYZ")

    expect(login_page.login_message).to_be_visible()
    expect(login_page.login_message).to_have_text("Invalid username or password.")


def test_dashboard_after_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("sneha", "password123")

    dashboard_page = DashboardPage(page)
    expect(dashboard_page.welcome_message).to_be_visible()
    dashboard_page.go_to_profile()

    profile_page = ProfilePage(page)
    expect(profile_page.profile_heading).to_be_visible()
    expect(profile_page.profile_heading).to_have_text("Sneha's Profile")


def test_logout(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("sneha", "password123")

    dashboard_page = DashboardPage(page)
    expect(dashboard_page.welcome_message).to_be_visible()
    dashboard_page.logout()

    expect(page).to_have_url("file:///I:/sneha/Development/PlaywrightFramework/login.html")


def test_go_to_profile(page):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    profile_page = ProfilePage(page)

    login_page.open()
    login_page.login("Sneha", "Password123")
    dashboard_page.go_to_profile()

    expect(profile_page.profile_heading).to_have_text("Sneha's Profile")
    expect(page).to_have_url("file:///I:/sneha/Development/PlaywrightFramework/profile.html")
