class homepage:
    def __init__(self, page):
        self.page = page
        self.home_page_image = page.locator("//div[@Id='LogoContent']/a/img")
        self.sign_in_link = page.locator("//a[text()='Sign In']")
        self.username = page.locator("//p[text()='Please enter your username and password.']")
        self.reptiles_link = page.locator("//img[@src='../images/sm_reptiles.gif']")
        self.reptiles_header = page.locator("//h2[text()='Reptiles']")
