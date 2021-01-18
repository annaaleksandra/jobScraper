from selenium import webdriver
import csv

browser = webdriver.Chrome(executable_path=r'C:/python/chromedriver.exe')
#The website that you want to scrape from
browser.get('https://www.s1jobs.com/')

def fillForm(keyword, location):
    #Type in the job name
    what = browser.find_element_by_css_selector('#Keywords')
    what.send_keys(keyword)

    #Select and type out the location
    where = browser.find_element_by_css_selector('#location')
    where.send_keys(location)

    where.submit()


def createCSV():
    #Searches for title, location, salary based on their class name
    jobTitles = browser.find_elements_by_class_name('jobTitle')
    location = browser.find_elements_by_class_name('dottedLink')
    salary = browser.find_elements_by_class_name('salary')

    #Creates and csv file in the folder where this program exists and writes the important information
    with open('jobSearchDataAnalyst.csv', 'w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['jobTitle', 'location', 'salary']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(len(jobTitles)):
            writer.writerow({'jobTitle': jobTitles[i].text, 'location': location[i].text, 'salary': salary[i].text.replace('Salary: ', '')})


    browser.quit()


fillForm('Data Analyst', 'Scotland')
createCSV()
