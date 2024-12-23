#Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from homepage import HomePage


class TestDemo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demo(self):
    self.driver.get("https://tdd-detroid.onrender.com/")
    self.driver.set_window_size(970, 555)

    home_page = HomePage(self.driver)
    home_page.wait_page_home()

    home_page.add_student("jose")
    assert (
      "INFO Added student id: 1, Name: jose"
      in self.driver.find_element(By.CSS_SELECTOR, ".py-p").text
      )

    home_page.add_materia_temp(course="automacao")
    assert (
            "INFO Added student id: 1, Name: jose"
            in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(2)").text
    )

    home_page.add_student_course()
    assert (
      "INFO Added student id: 1, Name: jose"
      in self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(3)").text
    )

    home_page.add_discipline_course()
    assert (
            "FAIL Necessários 3 cursos para se criar a primeira matéria"
            in self.get_first_log()
    )

    home_page.add_materia_temp(course="nuvem")
    home_page.add_materia_temp(course="qualidade")

    self.driver.find_element(
      By.CSS_SELECTOR, ".form-group:nth-child(5) > #course-btn").click()
    assert (
            "INFO Added discipline id: 1, Name: automacao, Course: 1"
            in self.get_first_log()
     )

    home_page.add_discipline_temp(discipline="api")
    home_page.add_discipline_temp(discipline="mobile")
    home_page.subscribe_student_discipline(1,1)
    assert (
            "WARN Aluno deve se inscrever em 3 materias no minimo"
            in self.get_first_log()
    )
    home_page.subscribe_student_discipline("1","2")
    home_page.subscribe_student_discipline("1","3")
    home_page.add_discipline_temp(discipline="web")
    home_page.subscribe_student_discipline("1", "4")


  def get_first_log(self):
    return self.driver.find_element(By.CSS_SELECTOR, ".py-p:nth-child(1)").text
  




