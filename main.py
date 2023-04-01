from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    unheard_skill = input("enter a skill your are unfamiliar with->")
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find("span", class_="sim-posted").text
        published_date = job.find("span", class_="sim-posted").text
        if not 'few' in published_date:
            continue
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(" ","")
        skills=job.find("span",class_='srp-skills').text.replace(" ","")
        more_info=job.header.h2.a['href']
        if unheard_skill not in skills:
            with open(f"job_posts/{index}.txt","w") as f:
                print('written in file {index}')
                f.write(f"Company name:{company_name.strip()} \n")
                f.write(f"skills:{skills.strip()} \n \n")
                f.write(f'{more_info} \n')



if __name__ =="__main__":
    while(True):
        print('hi')
        find_jobs()
        time.sleep(6)
