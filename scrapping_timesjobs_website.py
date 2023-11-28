from bs4 import BeautifulSoup

#scrapping websites using requests library
#request library just requests information for the website

import requests as rq
import time

html_text= rq.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup= BeautifulSoup(html_text,'lxml')
jobs= soup.find_all('li', class_='clearfix job-bx wht-shd-bx')


#printing all jobs present on the current page
for job in jobs:
    #o/p is giving unnecessary spaces for replacing ' ' with ''
    company_name= job.find('h3', class_='joblist-comp-name').text.replace(' ', '')

    skills= job.find('span', class_='srp-skills').text.replace(' ','')

    #as published date is inside 2 span tags
    published_date= job.find('span', class_='sim-posted').span.text

    print(f'''
    Company Name : {company_name}
    Required skills= {skills}
    ''')
    print('')
#----------------------------------------------------------------------------------

#filtering on the bases of skills we are not familiar with
print("Enter skill you are not familiar with")
unfamilar_skill=input('>')
print(f'Filtering out {unfamilar_skill}')


def find_jobs():
    #to extract jobs that are posted recently
    for index,job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text

        #pinting all jobs that are posted few days ago
        #'few' word should be present in published_date data
        if 'few' in published_date:
            company_name= job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills= job.find('span', class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href'] #gettinf the href value i.e. link

            if unfamilar_skill not in skills:
                with open(f'job_posts/{index}.txt', 'w') as f:
                    f.write(f'Company name : {company_name.strip()}\n')
                    f.write(f'Skills : {skills.strip()}\n')
                    f.write(f'More info : {more_info}')

                print(f'file saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait*60} seconds')
        time.sleep(time_wait*60) #wait 600sec and then re-run the prog