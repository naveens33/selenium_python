class BasePage:
    driver=""
    def __init__(self,d):
        self.driver=d

    def click(self,locator):
        #Why * is given, since, find_element needs two parameter then we have to pass the locator as *args
        element=self.driver.find_element(*locator)
        self.highlight(element)
        element.click()

    def type(self,locator,text):
        self.driver.find_element(*locator).send_keys(text)

    def get_element_by_text(self,locator,text):
        elements=self.driver.find_elements(*locator)
        for element in elements:
            if element.text==text:
                self.highlight(element)
                return element

    def highlight(self,element):
        #highlight the element through execute_script fucntion
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                    element,
                                    "border: 2px solid red;")
