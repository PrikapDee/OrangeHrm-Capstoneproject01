# OrangeHrm_locator python file to keep all xpath at one location"

class Locators:
    username = "username"
    password = "password"
    login = "//button[@type='submit']"
    pim = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name' and text()='PIM']"
    add_employee_icon = "//a[text()='Add Employee']"
    first_name = "//div//input[@name='firstName']"
    last_name = "//div//input[@name='lastName']"
    save_button = "//div//button[@type='submit']"
    success_msg = "//div//P[2][text()='Successfully Saved']"
    edit_icon = "//div//button[1]//i[@class='oxd-icon bi-pencil-fill']"
    fullname = "//input[@class='oxd-input oxd-input--active orangehrm-firstname' and @name='firstName']"
    save_update = "//form//div[4]//button[@type='submit']"
    update_msg = "//div//P[2][text()='Successfully Updated']"
    employee_list_icon = "//a[text()='Employee List']"
    delete_icon = "//div//button[2]//i[@class='oxd-icon bi-trash']"
    del_button_icon = ("//div[@class='oxd-sheet oxd-sheet--rounded oxd-sheet--white oxd-dialog-sheet "
                       "oxd-dialog-sheet--shadow oxd-dialog-sheet--gutters orangehrm-dialog-popup']//div[3]//button["
                       "2][text()=' Yes, Delete ']")
    del_msg = "//div//P[2][text()='Successfully Deleted']"
    invalid_msg = "//div[@class='oxd-alert-content oxd-alert-content--error']//P[text()='Invalid credentials']"
    Employee_id = ("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input "
                   "oxd-input--active']")
    radio_button = ("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//div//label//input["
                    "@type='radio' and @value='2']")


