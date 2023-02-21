import requests
from bs4 import BeautifulSoup
import os
import cloudscraper
from urllib.parse import urljoin


class Scraper:
    def __init__(self):
        # specify the URL of the website to scrape
        self.home_url = "https://www.classcentral.com/"

        # create CloudScraper instance to bypass cloudflare
        self.scraper = cloudscraper.create_scraper(delay=10, browser='chrome') 

        # create a directory to save the HTML files
        if not os.path.exists("html_files"):
            os.makedirs("html_files")
            os.makedirs("text_files")

    def get_files(self):
        url = self.home_url
        # send a GET request to the website to retrieve its HTML conten
        # create a BeautifulSoup object from the HTML content
        info = self.scraper.get(url).text
        soup = BeautifulSoup(info, "html.parser")
        self.soup = soup

        # get the JavaScript files
        script_files = []
        self.script_files = script_files
        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                # if the tag has the attribute 'src'
                script_url = urljoin(url, script.attrs.get("src"))
                script_files.append(script_url)

        # get the CSS files
        css_files = []
        self.css_files = css_files
        for css in soup.find_all("link"):
            if css.attrs.get("href"):
                # if the link tag has the 'href' attribute
                css_url = urljoin(url, css.attrs.get("href"))
                css_files.append(css_url) 
    
    # generate the files and save locally
    def write_files(self):
        text = self.soup.get_text()
        with open('html_files/home.html', "w", encoding="utf-8") as file:
            file.write(str(self.soup.prettify()))

        with open('text_files/home.txt', "w", encoding="utf-8") as file:
            file.write(text)

        print("Total script files in the page:", len(self.script_files))
        print("Total CSS files in the page:", len(self.css_files))

        # write file links into files
        with open("javascript_files.txt", "w") as f:
            for js_file in self.script_files:
                print(js_file, file=f)

        with open("css_files.txt", "w") as f:
            for css_file in self.css_files:
                print(css_file, file=f)

    def download_files(self, file_url):
        #r = requests.get(file_url, stream = True)
        r = self.scraper.get(file_url, stream = True)
        file_name = file_url.split("/")[-1]
        with open(file_name,"wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                # writing one chunk at a time to f file
                if chunk:
                    f.write(chunk)

    def save_files(self):
        # iterate over the links and save the HTML content in a separate file
        links = []
        with open('links.txt', "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                links.append(line)

        #for i, link in enumerate(links):
        link = 'https://www.classcentral.com/institution/salesforce'
        info = self.scraper.get('https://www.classcentral.com/institution/salesforce').text
        
        soup = BeautifulSoup(info, "html.parser")
        text = soup.get_text()
        file_name = link.split("/")[-1]
        
        with open(f'html_files/{file_name}.html', "w", encoding="utf-8") as file:
            file.write(str(self.soup.prettify()))

        with open('text_files/home.txt', "w", encoding="utf-8") as file:
            file.write(text)

    def extract_links(self):
        # extract all the links available in one level
        '''links = []
        for link in self.soup.find_all("a"):
            href = link.get("href")
            if href is not None and not href.startswith("#") and not href.startswith("javascript:"):
                # check if the link is within the same domain
                if href.startswith(self.home_url):
                    links.append(href)
                # check if the link is relative
                elif href.startswith("/"):
                    links.append(self.home_url + href)'''


        # iterate over the links and save the HTML content in a separate file
        links = []
        with open('links.txt', "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                links.append(line)

        for i, link in enumerate(links):
            info = self.scraper.get(link).text
            soup = BeautifulSoup(info, "html.parser")
            text = soup.get_text()
            with open('links.txt', "a+", encoding="utf-8") as file:
                file.write(f'{link}\n')

            '''
            filename = f"html_files/page_{i+1}.html"
            text_file = f"text_files/page_{i+1}.txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(str(soup.prettify()))

            print(f"HTML content saved to {filename}")
            with open(text_file, "w", encoding="utf-8") as file:
                file.write(text)

            print(f"Text content saved to {filename}")'''

    def run(self):
        self.get_files()
        self.write_files()
        #self.extract_links()
        self.save_files()

if __name__ == "__main__":
    scraper = Scraper()
    scraper.run()
