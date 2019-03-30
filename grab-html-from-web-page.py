from urllib.request import urlopen
my_address = "http://www.staff.city.ac.uk/~ddimak/python/practice/Profile_Aphrodite.htm"
html_page = urlopen(my_address)
html_text = html_page.read().decode('windows-1252')
print(html_text)