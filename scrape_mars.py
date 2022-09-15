from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium import webdriver


chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation']);

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)
    
   
    
def scrape():
    browser = init_browser()
    
    nasa_mars_data ={}
   

    Nasa_url = "https://redplanetscience.com/"
    browser.visit(Nasa_url)
    #creating my html object and parsing with bs
    html = browser.html
    soup = bs(html, "html.parser")
    #title text extration
    latest_news_title = soup.find("div", class_="content_title").text
    nasa_mars_data["latest_news_title"]=latest_news_title
    # paragraph extraction
    latest_news_paragraph = soup.find('div',class_='article_teaser_body').text
    nasa_mars_data["latest_news_paragraph"]=latest_news_paragraph
    
    
   
    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    response = browser.html
    soup = bs( response,"html.parser")   
    image = soup.find("img", class_="fade-in")["src"]
    featured_image_url = jpl_url+image
    nasa_mars_data["featured_image_url"]=featured_image_url
    

    nasa_url= "https://galaxyfacts-mars.com/"
    browser.visit(nasa_url)
    #creating DataFrame to store the scraped data
    marsfacts_df = pd.read_html(nasa_url)
    #Create Dataframe to store table data
    df = marsfacts_df[0]
    df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    df.set_index('Mars-Earth Comparison',inplace=True)
    df.index.name=None
    html_table = df.to_html(classes = 'table table-striped table-hover')
    nasa_mars_data["html_table"]=html_table
        
    
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
        html = browser.html
        hemi_soup = bs(html, "html.parser")
        hemisph_img_url =  hemi_soup.find("img", class_= "wide-image")["src"]
        final_image_url =  Hemispheres_url+hemisph_img_url
        #appending the titles and hemisphere_urls into the dict
        img_data=dict({'title':title, 'img_url':final_image_url})
        hemisp_image_urls.append(img_data)

    browser.back()
        
    nasa_mars_data["hemisp_image_urls"] = hemisp_image_urls
    browser.quit()
    return nasa_mars_data
    
    

    
    
    
    
    
        
        
        
        
        
    
    
    
    
   
    
    
    
    
    
    
    
    
    

    

