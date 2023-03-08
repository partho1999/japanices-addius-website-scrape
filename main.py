import requests
from bs4 import BeautifulSoup
import pandas as pd
import time



def scraper(url):

    headers = {
        'authority': 'shop.adidas.jp',
        'cache-control': 'max-age=0',
        'rtt': '300',
        'downlink': '1.35',
        'ect': '3g',
        'sec-ch-ua': '"Google Chrome"; v="83"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cookie': 'aws-priv=eyJ2IjoxLCJldSI6MCwic3QiOjB9; session-id=139-7350741-1081713; ubid-main=135-9894765-6184621; lc-main=en_US; s_fid=0A4730DDD06B62E4-1DB478AB62143F35; regStatus=pre-register; x-main=hd2N9IEBuVL7il1dbkhEEHTQSf4Q7uviwjc2eikr0hRGGOyI2RYIiRsk3GvDKLSx; at-main=Atza|IwEBIJdoAZ4Y6j2IIGvC29t1ha634aK-p2kAl8rHhQRCSGMSU_nwQvM6fakAbYEjpVLPU4Jj0TwKvX70d6QnlouKPh0QwpHJG8rHUNVb-gmhS9shHM8fCJk45r1XW2FOSpLoM1iAO9kYIpOoW2M5We9xfdqlLuQBB-D5fQeO5Vqew4RnHesPNZuF4DQNlcqL7wrGjDY1JQKzlzARfATAuwaCy4jMD5bNmxpcWtTgNGrTtLpGv1Y-4Mnx2axxQYFgwpRNv_sPNZrMAfHdU7MX67HbyPyV3V21KAl8QNl0xE-lNl3myxnfyWH68Z5D-j501S7HWzkKxopy3SfGuwwZTjSVSVlnH4RmTwvEnW8W3tndcX6X1ETysYYXmO7TudIjtq7aUZqPBJe_MViePcWL3OV4q2b5; sess-at-main="TjcvTeXAA2dP6HOMGcG/n+Cdkr+peDBlNMOvfBz6oE0="; sst-main=Sst1|PQGR5AF9x4yS-iMft3B9aBzJC8v-e4M1kmB_3KS0pxtVTj1cH8hl3fajgigt6xEYhan-kUJuY5KNbteBgbiyDIRCs4ISve5MdRhDdoy7XKrVD1g5McZTyvdwYLfbTJbTUov51hOyPcE8BKpFL1bGpJiiJbZ0TV7Pyc6tkndogjneZATDErc4U08WE4LwPJxCiF-I-7Av4-JEfwH1ZQ81mz6rqy-K1o6bCMRRZ8kWuzrl0wobKsr4Sz0-m1K0waguIewhXNm4V4DLe8mn-_6I8_k9p9v3NiFRpp04v0Ptzw8V1ARo2U18t5f2nx54EXwHzvzOQlpeBVY2U0WpXDcKsU3C8Q; session-id-time=2082787201l; i18n-prefs=USD; x-wl-uid=1MwJyD7dRnGiVdHw1PKiwmoNP9S/0xy+3KAKCJl2fM5VOthLzEW3dzyeW4zdKAepcIxkXpJFkxWcafUXXcS0MeSyLyFoBkl3xnNPLiRK0Rq33AHw0gL3W1FDBUn9OcakOzJGVGKZRc5E=; s_vn=1614974634531%26vn%3D4; s_nr=1590823888871-Repeat; s_vnum=2022823888872%26vn%3D1; s_dslv=1590823888874; sp-cdn="L5Z9:FR"; session-token=3AIPjoIrP8ITt1e/KXLZGSlnOPpirrWotNpCpCEfNRCY9mCfAV169URMcAX8XECtxt/qJujUn66Oyz8KIFDMieNmSdzEKA0K8I4AqbzplslzVGtZ6rNg+XsX/Bdc3hxnB7tUqQhrbrtVUncdzUMN1c95vhL7p+AEog3iiDkhLch0VO+Sl8HkAdZ/63xrp0stAaUsYo1GgsOFGI8+3wJUp4CHrJnoj/0lqjCJCpgXTZfxJcfWy9KarcGAPkno+fuMQqMoShJdi8R+DZ9XmIMib1bsLwXnerZa; csm-hit=tb:GVY0F2K4G05TXW59KB9M+s-GVY0F2K4G05TXW59KB9M|1592424615451&t:1592424615452&adb:adblk_yes',
    }

    params = (
        ('k', 'Python'),
        ('ref', 'nb_sb_noss'),
    )

    timestr = time.strftime("%Y%m%d-%H%M%S")

    r = requests.get(url, headers=headers, params=params)
    #print(r.text)

    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.title.text)

    # Image URL##############################################
    images = soup.find_all('img')

    #  Looking for the img with the classes 
    im = soup.find_all('img', class_='test-main_image')
    #print(im)


    image = []
    for img in im:
        image.append("https://shop.adidas.jp" + img.get('src'))

    print(image)

    df = pd.DataFrame(image,  columns =['img_url'])
    
    df.to_csv("img-url"+"-"+timestr+".csv")
    print(df)

    # Breadcrumb(Category)######################################
    catagory = soup.find("ul", {"class": "breadcrumbList clearfix test-breadcrumb css-2lfxqg"})
    #print(catagory)
    b_cat_ul =[]
    for ul in catagory:
        ul = ul.text.replace("iconArrowCircleLeft","")
        b_cat_ul.append(ul)
    # for li in ul.findAll('li'):
    #     print(li)
    df1 = pd.DataFrame(b_cat_ul,  columns =['Breadcrumb(Category)'])
    
    df1.to_csv('Breadcrumb(Category)'+'-'+timestr+'.csv')
    print(df1)

    # Category####################################################
    cat = soup.find("span", {"class": "categoryName test-categoryName"})

    cat_lst =[cat.text]
    print(cat_lst)

    # Product Name#################################################
    p_title = soup.find("h1", {"class": "itemTitle test-itemTitle"})

    pro_t_lst =[p_title.text]
    print(pro_t_lst)

    # Product Price################################################
    price = soup.find("span", {"class": "price-value test-price-value"})

    pro_price_lst =[price.text]
    print(pro_price_lst)
    
    # dictionary of lists 
    dict = {'Category': cat_lst, 'Product Name': pro_t_lst, 'Product Price': pro_price_lst} 
        
    df2 = pd.DataFrame(dict)
       
    df2.to_csv("product_details"+"-"+timestr+".csv")
    print(df2)

    # Available Size#################################################
    size = soup.find("ul", {"class": "sizeSelectorList"})
    #print(a_size)

    a_size_lst=[]
    for ul in size:
        a_size_lst.append(ul.text)

    df3 = pd.DataFrame(a_size_lst,  columns =['Available Size'])
    
    df3.to_csv('Available Size'+'-'+timestr+'.csv')
    print(df3)

    # Sense of the Size##############################################
    sense_size = soup.find("div", {"class": "sizeFitBar css-zrdet1"})
    print(sense_size)
    if sense_size is None:
        pass
    else:
        s_size_lst=[]
        for t in sense_size.find_all("span"):
            s_size_lst.append(t.text)

        df4 = pd.DataFrame(s_size_lst,  columns =['Sense of the Size'])
        
        df4.to_csv('Sense of the Size'+'-'+timestr+'.csv')
        print(df4)











    # Title of Description##############################################
    title_des = soup.find("h4", {"class": "heading itemFeature test-commentItem-subheading"})

    t_o_d_lst=[title_des.text]
    #print(t_o_d_lst)
    df5 = pd.DataFrame(t_o_d_lst,  columns =['Title of Description'])
    
    df5.to_csv('Title of Description'+'-'+timestr+'.csv')
    print(df5)

    # General Desciption of the product###################################
    des = soup.find("div", {"class": "commentItem-mainText test-commentItem-mainText"})
    g_d_o_t_p_lst=[des.text]
    df6 = pd.DataFrame(g_d_o_t_p_lst,  columns =['General Desciption of the product'])
    
    df6.to_csv('General Desciption of the product'+'-'+timestr+'.csv')
    print(df6)

    # General Discription (itemization)#####################################
    des_ul = soup.find("ul", {"class": "articleFeatures description_part css-1lxspbu"})

    g_d_lst=[]
    for ul in des_ul:
        g_d_lst.append(ul.text)

    df7 = pd.DataFrame(g_d_lst,  columns =['General Discription (itemization)'])
    
    df7.to_csv('General Discription (itemization)'+'-'+timestr+'.csv')
    print(df7)








    # KW###########################################################################
    kw = soup.find("div", {"class": "test-category_link null css-vxqsdw"})
    #print(kw)
    for link in kw.find_all('a'):
        print(link.text)


scraper("https://shop.adidas.jp/products/IA4778/")






