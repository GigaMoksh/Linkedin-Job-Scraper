import requests
import geocoder
from bs4 import BeautifulSoup
import csv

header = ["Id", "Job", "Company", "Details", "Location", "Upload Date", "Link"]
filename = "linkedin-job-scraper.csv"
links_to_apply = []

url = "https://www.linkedin.com/jobs/search?"
location = "location="
profile = "&keywords="
position = "&f_E="
jobtype = "&f_JT="
sort = "&sortBy="
search_type = input(
    "Enter : \n\t<1> For Direct Search\n\t<2> For Custom Search (Recommended)\n>> "
)

if search_type == "1":
    loc = geocoder.ipinfo("me")
    state_input = str(loc.state)
    state_input = state_input.replace(" ", "%20").lower()
    location += str(state_input)
    url += location

elif search_type == "2":
    city_input = input("Please Enter Your City : \n>> ")
    city_input = city_input.replace(" ", "").lower()
    location += str(city_input)
    url += location
    job_input = input("Please Enter Your Job Profile : \n>> ")
    job_input = job_input.replace(" ", "").lower()
    profile += str(job_input)
    url += profile
    types_input = ""
    bool_pre_position = False
    bool_pre_type = False

    while types_input != "0":
        print("Enter : ")
        if not bool_pre_position:
            print("\t<1> For : Job Position")
        if not bool_pre_type:
            print("\t<2> For : Job Type")
        types_input = input("\t<0> To esc\n>> ")
        if types_input == "1":
            bool_pre_position = True
            bool_positional = False
            while not bool_positional:
                position_input = input(
                    "Enter : \n\t<1> For : Internship\n\t<2> For : Entry Level\n\t<3> For : Associate\n\t<4> For : Mid Senior Level\n\t<5> For : Director\n\t<6> For : Executive\n >> "
                )
                if position_input == "1":
                    bool_positional = True
                    position += str("1")
                elif position_input == "2":
                    bool_positional = True
                    position += str("2")
                elif position_input == "3":
                    bool_positional = True
                    position += str("3")
                elif position_input == "4":
                    bool_positional = True
                    position += str("4")
                elif position_input == "5":
                    bool_positional = True
                    position += str("5")
                else:
                    continue
            url += position

        elif types_input == "2":
            bool_pre_type = True
            bool_jobtype = False
            while not bool_jobtype:
                jobtype_input = input(
                    "Enter : \n\t<1> For : Full Time Job\n\t<2> For : Part Time Job\n>> "
                )
                if jobtype_input == "1":
                    bool_jobtype = True
                    jobtype += str("F")
                elif jobtype_input == "2":
                    bool_jobtype = True
                    jobtype += str("P")
                else:
                    continue
            url += jobtype

        if bool_pre_position and bool_pre_type:
            break
else:
    print("Wrong Input")
    quit()

try:
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    body = soup.find("body")

    with open("linkedin-job-scraper.csv", "a", newline="") as f:
        writer = csv.writer(f)
        i = 0

        for link in body.findAll("a", {"class": "base-card base-card--link base-search-card base-search-card--link job-search-card"}):
            apply_link = link.get("href")
            apply_link = " ".join(apply_link.split())
            links_to_apply.append(apply_link)

        for content in body.findAll("div", {"class": "base-search-card__info"}):
            try:
                Title = str(
                    content.find(
                        "h3", {"class": "base-search-card__title"}).get_text()
                )
                Title = " ".join(Title.split())
                Company = str(
                    content.find(
                        "h4", {"class": "base-search-card__subtitle"}).get_text()
                )
                Company = " ".join(Company.split())
                Location = str(
                    content.find(
                        "span", {"class": "job-search-card__location"}
                    ).get_text()
                )
                Location = " ".join(Location.split())
                # Details = str(
                #     content.find("p", {"class": "job-search-card__snippet"}).get_text()
                # )
                # Details = " ".join(Details.split())
                # Time = str(
                #     content.find(
                #         "time", {"class": "job-search-card__listdate"}
                #     ).get_text()
                # )
                # Time = " ".join(Time.split())
                print(f'Title : {Title}')
                print(f'Company : {Company}')
                # print(f'Details : {Details}')
                print(f'Location : {Location}')
                # print(f'Time : {Time}')
                print(f'Link : {links_to_apply[i]}')
                print("\n")
                i += 1
                writer.writerow(
                    [i, Title, Company, "", Location, "", links_to_apply[i]])

            except:
                pass

except requests.HTTPError as _:
    print("Unable to Scrap!")
