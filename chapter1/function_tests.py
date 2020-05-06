from selenium import webdriver


browser = webdriver.Firefox()


# Edith heard about the cool to-do app and
# goes tocheckout its homepage
browser.get('http://localhost:8000')

# she notices page title and header mention to-do lists
assert 'To-Do' in browser.title, "Browser title was "+ browser.title


# she is invited to enter a to-do item straight away


# she types 'Buy peacock feathers' into a text box

# she hits enters the page updates and now the page lists
# "1. Buy Peacock feathers" as a item in a to-do list


# There is still a text box inviting her to add another item.
# she enters "Use peacock feathers to make a fly"


# The page updates and now show both items on her lists

# Edith wonders wether the site remembers her lists.
# she sees the site has generated a unique url for her -- 

# she visits the url-- her todo list is still there

# Satisfied, she goes to sleep

browser.quit()

