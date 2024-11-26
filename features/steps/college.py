from homepage import HomePage
from selenium import webdriver

@given(u'the student does not exist')
def step_impl(context):
    driver = webdriver.Chrome()
    vars = {}
    hp = HomePage(driver)
    driver.get("https://tdd-detroid.onrender.com/")
    driver.set_window_size(970, 555)
    hp.wait_page_load()
    context.homepage = hp

@when(u'I create a student')
def step_impl(context):
    hp = context.homepage
    hp.add_student("jose")


@then(u'the student is created')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the student is created')

#######

@given(u'the course "automacao" exists')
def step_impl(context):
    driver = webdriver.Chrome()
    hp = HomePage(driver)
    driver.get("https://tdd-detroid.onrender.com/")
    driver.set_window_size(970, 555)
    hp.wait_page_load()
    hp.add_materia_temp(course="automacao")
    context.homepage = hp

@when(u'I add a discipline "api" to the course')
def step_impl(context):
    hp = context.homepage
    hp.add_discipline_temp(discipline="api")

@then(u'the discipline "api" should be added to the course')
def step_impl(context):
    hp = context.homepage
    assert "INFO Added discipline id: 1, Name: api" in context.homepage.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(3)").text
