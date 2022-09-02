from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium import webdriver
import time


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)
    
   
   
 #nasa_mars_data = {}
    
def scrape():
    browser = init_browser()
    
    nasa_mars_data ={}
   
    #executable_path = {'executable_path': ChromeDriverManager().install()}
    #browser = Browser('chrome', **executable_path, headless=False)
    #latest_news_title,latest_news_paragraph,Nasa_url = mars_news(browser)
    #featured_image_url,jpl_url = JPL_scrape(browser)
    #mars_table,mars_facts = mars_facts(browser)
    #hemisp_image_urls = mars_hemispheres(browser)
    #return browser
    
    
     
# Setting an empty dict for listings that we can save to Mongo    
    #nasa_mars_data ={"latest_news_title":latest_news_title,
                     #"latest_news_paragraph":latest_news_paragraph,
                     #"source":Nasa_url,
                    #"featured_image_url":featured_image_url,
                    #"source2":jpl_url,
                    #"html_table":mars_table,
                      #"source":mars_facts,
                    #"hemisp_image_urls":hemisp_image_urls} 
    
    #return nasa_mars_data
#def mars_news():
    #browser = init_browser()
    #browser = scrape()
    #time.sleep(1)
    Nasa_url = "https://redplanetscience.com/"
    browser.visit(Nasa_url)
    
    #creating my html object and parsing with bs
    html = browser.html

    soup = bs(html, "html.parser")
    
    #title text extration
    latest_news_title = soup.find("div", class_="content_title").text
    #print(f" news_title: {latest_news_title}")
    # paragraph extraction
    latest_news_paragraph = soup.find('div',class_='article_teaser_body').text
    nasa_mars_data["latest_news_paragraph"]=latest_news_paragraph
    nasa_mars_data["latest_news_title"]=latest_news_title
    #print(f"latest_news_paragraph: {latest_news_paragraph}")
    #nasa_mars_data ={"latest_news_title":latest_news_title,
                     #"latest_news_paragraph":latest_news_paragraph}
    
    
    #print(f" news_paragraph: {latest_news_paragraph}")
    
    #print(f" source:{Nasa_url}")
    
    #return latest_news_title,latest_news_paragraph,Nasa_url
    #return nasa_mars_data
    
    #time.sleep(1)
#def JPL_scrape():
    #browser = init_browser()
    #browser = scrape()
        
    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    response = browser.html
    soup = bs( response,"html.parser")
        
    image = soup.find("img", class_="fade-in")["src"]
    featured_image_url = jpl_url+image
    nasa_mars_data["featured_image_url"]=featured_image_url
    #nasa_mars_data.update({"featured_image_url":featured_image_url})
    #nasa_mars_data = {"featured_image_url":featured_image_url}
    #print(f" featured_image_url = {featured_image_url}")
        
    #return featured_image_url,jpl_url
    #return nasa_mars_data

    #time.sleep(1)
#def mars_facts():
    #browser = scrape()
    #browser = init_browser()
    
    #mars_facts_url = "https://space-facts.com/mars/"
    #browser.visit(mars_facts_url)

     #creating DataFrame to store the scraped data
    #facts_table = pd.read_html(mars_facts_url)

     #Create Dataframe to store table data
     #df = facts_table[0]
     #df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
     #html_table = df.to_html()
     #html_table
    #mars_data_df = facts_table[0]
    #mars_data_df.columns = ["label", "Mars"]
    #mars_data_df.set_index("label",inplace=True)
    #mars_data_df.index.name=None 
     #mars_data_df
     #using pandas to convert the table to a html
    #html_table = mars_data_df.to_html(classes="table table-striped table-hover")
    #nasa_mars_data["html_table"]=html_table
    #nasa_mars_data = {"html_table": html_table}

    nasa_url= "https://galaxyfacts-mars.com/"
    browser.visit(nasa_url)
    #creating DataFrame to store the scraped data
    marsfacts_df = pd.read_html(nasa_url)
    #marsfacts_df

    #Create Dataframe to store table data
    df = marsfacts_df[0]
    df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    html_table = df.to_html()
    nasa_mars_data["html_table"]=html_table
        
    #return nasa_mars_data
    
    #return mars_table,mars_facts
    #time.sleep(1)
#def mars_hemispheres():
    #browser = init_browser()
    #browser = scrape()
    Hemispheres_url = "https://marshemispheres.com/"
    browser.visit(Hemispheres_url)
    html = browser.html
    soup = bs(html, "html.parser")
    hem_link = soup.find_all("div", class_="item")

    #creating a list to collect the image_urls
    hemisp_image_urls = []

    # looping into the link to collect titles and image_url

    for x in hem_link:
    
        title = x.find("h3").text
        img_url = x.find("a")["href"]
        hemi_img_url = Hemispheres_url + img_url
    
        browser.visit(hemi_img_url)
        #time.sleep(5)
        html = browser.html
        hemi_soup = bs(html, "html.parser")
        #hemis_url = soup.find("img", class_= "wide-image")["src"]
    
    
        hemisph_img_url =  hemi_soup.find("img", class_= "wide-image")["src"]
        final_image_url =  Hemispheres_url+hemisph_img_url
    
        #print(final_image_url)
    
        #appending the titles and hemisphere_urls into the dict
        img_data=dict({'title':title, 'img_url':final_image_url})
        hemisp_image_urls.append(img_data)

        #browser.back()
        
    #nasa_mars_data["hemisp_image_urls"]=hemisp_image_urls

    nasa_mars_data["hemisp_image_urls"] = hemisp_image_urls
    
    
    browser.quit()
                    
    return nasa_mars_data
    
    

    
    
    
    
    
        
        
        
        
        
    
    
    
    
   
    
    
    
    
    
    
    
    
    

    

