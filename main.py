from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def scraper(url):
    driver = webdriver.Chrome(executable_path="E:\Scraper\chromedriver.exe")


    driver.get(url)

    get_url = driver.current_url
    print("The current url is:"+str(get_url))

    for j in range(0,10):
        driver.execute_script("scrollBy(0,+500);")
        time.sleep(3)
        driver.execute_script("scrollBy(0,-300);")
        time.sleep(3)
        print("scrolling..")

    soup=BeautifulSoup(driver.page_source,"html.parser")
    print(soup.title.text)

    for img in soup.find_all('table'):
        print(img.get('class'))

    #img URL##############################################################
    images = soup.find_all('img')
    #  Looking for the table with the classes 'wikitable' and 'sortable'
    im = soup.find_all('img', class_='test-main_image')
    #print(im)


    image = []
    for img in im:
        image.append("https://shop.adidas.jp" + img.get('src'))

    print(image)

    df1 = pd.DataFrame(image,  columns =['img_url'])
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df1.to_csv("img-url/img-url"+"-"+timestr+".csv")
    print(df1)

    #Breadcrumb(Category)###################################################
    catagory = soup.find("ul", {"class": "breadcrumbList clearfix test-breadcrumb css-2lfxqg"})
    #print(catagory)
    b_cat_ul =[]
    for ul in catagory:
        ul = ul.text.replace("iconArrowCircleLeft","")
        b_cat_ul.append(ul)
    # for li in ul.findAll('li'):
    #     print(li)
    df2 = pd.DataFrame(b_cat_ul,  columns =['Breadcrumb(Category)'])
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df2.to_csv('Breadcrumb(Category)/Breadcrumb(Category)'+'-'+timestr+'.csv')
    print(df2)

    #Category###############################################################
    cat = soup.find("span", {"class": "categoryName test-categoryName"})

    cat_lst =[cat.text]
    print(cat_lst)

    #Product Name############################################################
    p_title = soup.find("h1", {"class": "itemTitle test-itemTitle"})

    pro_t_lst =[p_title.text]
    print(pro_t_lst)

    #Product Price############################################################
    articlePrice =soup.find("div", {"class": "articlePrice test-articlePrice css-1apqb46"})
    price = articlePrice.find("span", {"class": "price-value test-price-value"})

    pro_price_lst =[price.text]
    print(pro_price_lst)

    # dictionary of lists###################################################### 
    dict = {'Category': cat_lst, 'Product Name': pro_t_lst, 'Product Price': pro_price_lst} 
        
    df3 = pd.DataFrame(dict)
    timestr = time.strftime("%Y%m%d-%H%M%S")    
    df3.to_csv("product_details/product_details"+"-"+timestr+".csv")
    print(df3)

    #Available Size#############################################################
    size = soup.find("ul", {"class": "sizeSelectorList"})
    if size is None:
        pass
    else:  
        #print(a_size)

        a_size_lst=[]
        for ul in size:
            a_size_lst.append(ul.text)

        df4 = pd.DataFrame(a_size_lst,  columns =['Available Size'])
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df4.to_csv('Available-Size/Available-Size'+'-'+timestr+'.csv')
        print(df4)

    #Sense of the Size###########################################################
    sense_size = soup.find("div", {"class": "sizeFitBar css-zrdet1"})
    if sense_size is None:
        pass
    else:
        s_size_lst=[]
        for t in sense_size.find_all("span"):
            s_size_lst.append(t.text)

        df5 = pd.DataFrame(s_size_lst,  columns =['Sense of the Size'])
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df5.to_csv('Sense of the Size/Sense of the Size'+'-'+timestr+'.csv')
        print(df5)

    #Coordinate Product Name#####################################################
    coordinate_title = soup.find("span", {"class": "titleWrapper"})
    if coordinate_title is None:
        pass
    else:

        coor_n_lst=[coordinate_title.text]
        print(coor_n_lst)

        #Coordinate Product Price####################################################
        cp_cnt =soup.find("div", {"class": "mdl-price test-Type2 css-izzs0m"})
        coordinate_price = cp_cnt.find("span", {"class": "price-value test-price-salePrice-value"})
        coor_p_lst=[coordinate_price.text]
        print(coor_p_lst)

        # coordinator cnt############################################################
        image_wrapper= soup.find("div", {"class": "css-1dq7gyf"})
        #print(image_wrapper)

        pg_lst =[]
        for link in image_wrapper.find_all('a'):
            pg_lst.append('https://shop.adidas.jp/'+link.get('href'))

        print(pg_lst)

        # img path
        img_lst=[]
        for img in image_wrapper.find_all('img'):
            img_lst.append('https://shop.adidas.jp/'+img.get('src'))

        print(img_lst)

        dic ={'Product Name':coor_n_lst, 'Product Price':coor_p_lst, 'Product Details Page':pg_lst, 'Product Img URL':img_lst}

        df5 = pd.DataFrame(dic)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df5.to_csv('coordinate product details/coordinate product details'+'-'+timestr+'.csv')
        print(df5)

    # Title of Description########################################################
    title_des = soup.find("h4", {"class": "heading itemFeature test-commentItem-subheading"})
    if title_des is None:
        pass
    else:
        
        t_o_d_lst=[title_des.text]
        #print(t_o_d_lst)
        df6 = pd.DataFrame(t_o_d_lst,  columns =['Title of Description'])
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df6.to_csv('Title of Description/Title of Description'+'-'+timestr+'.csv')
        print(df6)

    # General Desciption of the product#############################################
    des = soup.find("div", {"class": "commentItem-mainText test-commentItem-mainText"})
    if des is None:
        pass
    else:
        g_d_o_t_p_lst=[des.text]
        df7 = pd.DataFrame(g_d_o_t_p_lst,  columns =['General Desciption of the product'])
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df7.to_csv('General Desciption of the product/General Desciption of the product'+'-'+timestr+'.csv')
        print(df7)

    # General Discription (itemization)##############################################
    des_ul = soup.find("ul", {"class": "articleFeatures description_part css-1lxspbu"})
    if des_ul is None:
        pass
    else:
        g_d_lst=[]
        for ul in des_ul:
            g_d_lst.append(ul.text)

        df8 = pd.DataFrame(g_d_lst,  columns =['General Discription (itemization)'])
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df8.to_csv('General Discription (itemization)/General Discription (itemization)'+'-'+timestr+'.csv')
        print(df8)

    #Tale of Size###################################################################
    sizetable =  soup.find('table')
    if sizetable is None:
        pass
    else:
        sizetable0 =  soup.findAll('table', class_='sizeChartTable')[0]
        
        indexvalues = []
        for value in sizetable0.find_all('tr'):
            #print(value.text)
            indexvalues.append(value.text)

        sizetable1 =  soup.findAll('table', class_='sizeChartTable')[1]

        rows={}
        i = 0
        for value in sizetable1.findAll('tr'):
            row_data=[]
            for v in value.findAll('td'):
                row_data.append(v.text)
            if row_data:
                rows[indexvalues[i]]=row_data
            i+=1

        df9 = pd.DataFrame.from_dict(rows, orient='index')
        df9.columns=df9. iloc[0]
        df9 = df9.iloc[1:]
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df9.to_csv('Tale-of-Size/Tale-of-Size'+'-'+timestr+'.csv')
        print(df9)

    rating = soup.find("span", {"class": "BVRRNumber BVRRRatingNumber"})
    if rating is None:
        rating_lst=[]
        print(rating_lst)
    else:
        rating_lst=[rating.text]
        print(rating_lst)

    review = soup.find("span", {"class": "BVRRNumber BVRRBuyAgainTotal"})
    if review is None:
        review_lst =[]
        print(review_lst)
    else:
        review_lst=[review.text]
        print(review_lst)

    recomadation = soup.find("span", {"class": "BVRRBuyAgainPercentage"})
    if recomadation is None:
        recomadation_lst=[]
        print(recomadation_lst)
    else:
        recomadation_lst=[recomadation.text]
        print(recomadation_lst)

    dict = {'Rating': rating_lst, 'Number of Reviews': review_lst, 'Recommended rate': recomadation_lst}   
    df10 = pd.DataFrame(dict)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df10.to_csv('Rating-Review-Recommended/Rating-Review-Recommended'+'-'+timestr+'.csv')

    RatingsContainer = soup.find_all("div", {"class": "BVRRSecondaryRatingsContainer"})
    print(RatingsContainer)
    if RatingsContainer is None:
        pass
    else:

        #RatingFit
        rf_cnt = soup.find("div", {"class": "BVRRRating BVRRRatingRadio BVRRRatingFit"})
        #print(rf_cnt)

        rf_list =[]
        if rf_cnt is None:
            pass
        else:
            for rf in rf_cnt:
                rf_list.append(rf.text)

            print(rf_list)

        if rf_cnt is None:
            rf_s_lst = []
        else:
            rf_score = rf_cnt.find('img').get('title')
            rf_s_lst=[rf_score]
            print(rf_s_lst)

        #RatingLength
        rl_cnt = soup.find("div", {"class": "BVRRRating BVRRRatingRadio BVRRRatingLength"})
        #print(rl_cnt)
        rl_list=[]
        if rl_cnt is None:
            pass
        else:
            for rl in rl_cnt:
                rl_list.append(rl.text)
            print(rl_list)

        if rl_cnt is None:
            rl_s_lst=[]
        else:
            rl_score = rl_cnt.find('img').get('title')
            rl_s_lst = [rl_score]
            print(rl_s_lst)


        #RatingQuality
        rq_cnt = soup.find("div", {"class": "BVRRRating BVRRRatingRadio BVRRRatingQuality"})

        rq_list=[]
        if rq_cnt is None:
            pass
        else:
            for rq in rq_cnt:
                
                rq_list.append(rq.text)
            print(rq_list)

        if rq_cnt is None:
            rq_s_lst=[]
        else:
            rq_score = rq_cnt.find('img').get('title')
            rq_s_lst = [rq_score]
            print(rq_s_lst)    

        #RatingComfort
        rc_cnt = soup.find("div", {"class": "BVRRRating BVRRRatingRadio BVRRRatingComfort"})

        rc_list=[]
        if rc_cnt is None:
            pass
        else:
            for rc in rc_cnt:
                rc_list.append(rc.text)
            print(rc_list)

        if rc_cnt is None:
            rc_s_lst=[]
        else:    
            rc_score = rc_cnt.find('img').get('title')
            rc_s_lst =[rc_score]
            print(rc_s_lst)

        dic={
            'Sense of Fitting': rf_list,
            'Appropriation of length': rl_list,
            'Quality of material' : rq_list,
            'Comfort': rc_list   
        }

        df11 = pd.DataFrame(dic)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df11.to_csv('Sense-of-Fitting-Appropriation-of-length-Quality-of-material-Comfort/Sense-of-Fitting-Appropriation-of-length-Quality-of-material-Comfort'+'-'+timestr+'.csv')
        print(df11)

        dic={
            'Fitting Rating': rf_s_lst,
            'length Rating': rl_s_lst,
            'material Rating' : rq_s_lst,
            'Comfort Rating': rc_s_lst  
        }

        df_r= pd.DataFrame(dic)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df_r.to_csv('Fitting-length-Quality-Comfort-Rating/Fitting-length-Quality-Comfort-Rating'+'-'+timestr+'.csv')

    user_review_cnt = soup.find('div', class_='BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVContentJaJp BVDI_BAContentVerifiedPurchaser BVRRDisplayContentReviewOdd BVRRDisplayContentReviewFirst BVRROdd BVRRFirst')
    #print(user_review_cnt)
    if user_review_cnt is None:
        pass
    else:

    
        user_review_date = user_review_cnt.find("span", {"class": "BVRRValue BVRRReviewDate"})
    
        r_d_lst=[user_review_date.text]

        print(r_d_lst)

        user_review_rating =user_review_cnt.find('img').get('title')
    
        r_r_lst=[user_review_rating]
        print(r_r_lst)

        user_review_title = user_review_cnt.find("span", {"class": "BVRRValue BVRRReviewTitle"})
        r_t_lst=[user_review_title.text]
        print(r_t_lst)

        user_review_des= user_review_cnt.find("span", {"class": "BVRRReviewText"})
        r_d_lst=[user_review_des.text]
        print(r_d_lst)

        dic={
            'Date':r_d_lst, 
            'Rating':r_r_lst,
            'Review title':r_t_lst,
            'Review descriptions':r_d_lst
        }

        df12 = pd.DataFrame(dic)
        timestr = time.strftime("%Y%m%d-%H%M%S")
        df12.to_csv('Verified-Product-Reviewer-Details/Verified-Product-Reviewer-Details'+'-'+timestr+'.csv')
        print(df12)

    review_date_lst =[]
    review_rating_lst=[]
    review_title_lst=[]
    review_des__lst=[]
    review_id_lst=[]

    #evenReviewer
    BVRReven = soup.find_all('div', {"class": "BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVContentJaJp BVRRDisplayContentReviewEven BVRREven"})
    #print(BVRRodd)

    if BVRReven is None:
        pass
    else:

        for even in BVRReven:
            #date
            even_review_date = even.find("span", {"class": "BVRRValue BVRRReviewDate"})
            review_date_lst.append(even_review_date.text)
            print(review_date_lst)

            #rating
            even_review_rating =even.find('img').get('title')
            review_rating_lst.append(even_review_rating)
            print(review_rating_lst)

            #title
            even_review_title = even.find("span", {"class": "BVRRValue BVRRReviewTitle"})
            review_title_lst.append(even_review_title.text)
            print(review_title_lst)

            #des
            even_review_des= even.find("span", {"class": "BVRRReviewText"})
            review_des__lst.append(even_review_des.text)
            print(review_des__lst)
            
            #id
            even_review_id= even.find("span", {"class": "BVRRNickname"})
            review_id_lst.append(even_review_id.text)
            print(review_id_lst)

    #oddReviewer
    BVRRodd = soup.find_all('div', {"class": "BVRRContentReview BVRRDisplayContentReview BVDIContentNative BVRRContentReviewNative BVContentJaJp BVRRDisplayContentReviewOdd BVRROdd"})
    #print(BVRRodd)

    if BVRRodd is None:
        pass
    else:

        for odd in BVRRodd:
            #date
            odd_review_date = odd.find("span", {"class": "BVRRValue BVRRReviewDate"})
            review_date_lst.append(odd_review_date.text)
            print(review_date_lst)

            #rating
            odd_review_rating =odd.find('img').get('title')
            review_rating_lst.append(odd_review_rating)
            print(review_rating_lst)

            #title
            odd_review_title = odd.find("span", {"class": "BVRRValue BVRRReviewTitle"})
            review_title_lst.append(odd_review_title.text)
            print(review_title_lst)

            #des
            odd_review_des= odd.find("span", {"class": "BVRRReviewText"})
            review_des__lst.append(odd_review_des.text)
            print(review_des__lst)
            
            #id
            odd_review_id= odd.find("span", {"class": "BVRRNickname"})
            review_id_lst.append(odd_review_id.text)
            print(review_id_lst)

    dic={
        'Date':review_date_lst, 
        'Rating':review_rating_lst,
        'Review title':review_title_lst,
        'Review descriptions':review_des__lst,
        'Reviewer ID':review_id_lst
    }

    df13 = pd.DataFrame(dic)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df13.to_csv('product-Reviewer-details/product Reviewer details'+'-'+timestr+'.csv')
    print(df13)

    kw = soup.find("div", {"class": "test-category_link null css-vxqsdw"})
    #print(kw)
    kw_lst=[]
    for link in kw.find_all('a'):
        kw_lst.append(link.text)

    #print(kw_lst)


    df14 = pd.DataFrame([[str(str(kw_lst)[1:-1])]], columns =['KW'])
    timestr = time.strftime("%Y%m%d-%H%M%S")
    df14.to_csv('KW/KW'+'-'+timestr+'.csv')
    print(df14)



def get_url(category,page):
    # Create webdriver object
    driver = webdriver.Chrome(executable_path="E:\Scraper\chromedriver.exe")

    driver.get('https://shop.adidas.jp/item/?category='+category+'&gender=mens&limit=120&page='+page)
    # r = requests.get(url)
    # #print(r.text)

    for j in range(0,20):
        driver.execute_script("scrollBy(0,+1000);")
        time.sleep(3)
        driver.execute_script("scrollBy(0,-500);")
        time.sleep(3)
        print("scrolling..")

    soup=BeautifulSoup(driver.page_source,"html.parser")


    product = soup.find("div", {"class": "test-articleDisplay css-1yuo7po"})
    #print(product)

    product_url =[]
    for div in product.find_all('div'):
        #print(div)
        for link in div.find_all('a'):
            #print(link.get('href'))
            product_url.append("https://shop.adidas.jp" + link.get('href'))

    # for link in product.find_all('a'):
    #     product_url.append("https://shop.adidas.jp" + link.get('href'))

    print(product_url)

    

    df = pd.DataFrame(product_url,  columns =['product_details_url'])
    df = df.drop(df[df['product_details_url']=="https://shop.adidas.jp/adiclub/membersweek/"].index)
    df = df.drop_duplicates()


    timestr = time.strftime("%Y%m%d-%H%M%S")
    df.to_csv("product-details-url-list/product-details-url-list"+"-"+timestr+".csv")
    print(df)

    col_list = df.product_details_url.values.tolist()
    for url in col_list:
        scraper(url)
        time.sleep(10)

for i in range(1,4):# set range how much page you want to scrape 
    print(i)
    get_url('wear',str(i)) #set the category which you want to scrape

# def test():
#     df = pd.read_csv(r'E:\Scraper\product-details-url-list\product-details-url-list-20230311-131332.csv')

#     #print(df.head(96))
#     col_list = df.product_details_url.values.tolist()
#     #print(len(col_list))
#     #print(col_list.index('https://shop.adidas.jp/products/GF0210/'))
#     filter_col = col_list[3:]

#     for url in filter_col:
#         scraper(url)
#         time.sleep(10)
    

# test()