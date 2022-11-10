from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(keyword):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    request = requests.get(url, headers={"User-Agent": "Kimchi"})

    if request.status_code != 200:
        print("Can't resquest site.")
    else:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all(
            "td", class_="company position company_and_position")
        for job in jobs:
            anchor = job.find_all("a")
            position = job.find("h2")
            link = anchor[0]["href"]
            locations = job.find("div", class_="location")
            company = job.find("h3")
            if locations is not None:
                location = str(locations.string)

                job_data = {
                    'company': company.string.strip(),
                    'location': location,
                    'position': position.string.strip(),
                    'link': f"https://remoteok.com/{link}"
                }
                results.append(job_data)
        return results
