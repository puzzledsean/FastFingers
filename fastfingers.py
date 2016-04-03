from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#open web driver to 10fastfingers.com
driver = webdriver.Firefox()
driver.get("http://10fastfingers.com/typing-test/english")

#get input text field and next word to enter
inputForm = driver.find_element_by_id("inputfield")
inputWord = driver.find_element_by_class_name("highlight")

#keep typing next word until there are no words left
while inputWord.text != None:
    inputForm.send_keys(inputWord.text + " ")
    try:
        inputWord = driver.find_element_by_class_name("highlight")
    except NoSuchElementException:
        print('Hit the end of the list. Stopping input.')
        break

print('Finished')