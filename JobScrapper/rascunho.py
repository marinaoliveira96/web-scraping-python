import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f'https://br.indeed.com/empregos?q=python&limit={LIMIT}'
#URL= f"https://www.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"


def extract_indeed_pages():
    resul = requests.get(URL)

    soup = BeautifulSoup(resul.text, 'html.parser')

    pagination = soup.find('div', {'class': 'pagination'})

    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
      pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_job(html):
    title = html.find('h2', {'class': 'title'}).find('a')['title']
    #find só mostra o 1 que achar
    company = html.find('span', {'class': 'company'})
    company_anchor = company.find('a')

    if company_anchor is not None:
      company = company_anchor.string
    else:
      company = company.string
    location = html.find('span', {'class': 'location'}).string
    job_id = html['data-jk']

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': f'https://br.indeed.com/viewjob?jk={job_id}'
    }


def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"scrapping Indeed jobs : page {page+1}")
    result =requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text,"html.parser")
    results = soup.find_all("div",{"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)

  return jobs




 