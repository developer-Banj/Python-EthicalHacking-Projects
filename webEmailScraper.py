### Run with root privileges(sudo)


import re
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

def start_scrape(page):
    print("\n\nWebpage is currently being scrapped... please wait...")

    scrape = BeautifulSoup(page, 'html.parser')
    scrape = scrape.get_text()

    phone_numbers = set(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", scrape))
    emails = set(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape))

    nodupnumber = len(list(phone_numbers))
    nodupemail = len(list(emails))

    dupnumber = len(list(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})", scrape)))
    dupemail = len(list(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}", scrape)))

    number_of_dup_number = int(dupnumber) - int(nodupnumber)
    number_of_dup_email = int(dupemail) - int(nodupemail)

    if len(phone_numbers) == 0:
        print("No phone number(s) found.")
        print("-----------------------------\n")
    else:
        count = 1
        for item in phone_numbers:
            print("Phone number #" + str(count) + ': ' + item)
            count += 1

    print("-----------------------------\n")

    if len(emails) == 0:
        print("No email address(es) found.")
        print("-----------------------------\n")
    else:
        count = 1
        for item in emails:
            print('Email address #' + str(count) + ': ' + item)
            count += 1

    print("\nDuplicates have been removed from the list.")
    print("Total phone numbers: ", nodupnumber)
    print("Total email addresses: ", nodupemail)
    print("There were " + str(number_of_dup_number) + " duplicate phone numbers.")
    print("There were " + str(number_of_dup_email) + " duplicate email addresses.")


def main():
    webpage = input("Paste the webpage you would like to scrape (include http/https): ")

    try:
        page = urlopen(webpage)
        start_scrape(page)
    except:
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = Request(webpage, headers=hdr)
        page = urlopen(req)
        start_scrape(page)


if __name__ == "__main__":
    main()
