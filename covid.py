
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.yellowpages.com/los-angeles-ca')
soup = BeautifulSoup(page.content,'html.parser')
week = soup.find(id='coupons')
items = week.find_all(class_='coupon')


# print(items[0].find(class_='coupon-title').get_text())
# print(items[0].find(class_='coupon-listing-name').get_text())
# print(items[0].find(class_='sf_colsIn').get_text())


# print(items[0].find(class_="period-name").get_text())

# print(items[0].find(class_="short-desc").get_text())
# print(items[0].find(class_="temp").get_text())

cupon_title = [item.find(class_="coupon-title").get_text() for item in items]
coupon_listing_name =  [item.find(class_='coupon-listing-name').get_text() for item in items]
coupon_citystate =  [item.find(class_='coupon-citystate').get_text() for item in items]
coupon_value =  [item.find(class_='actual-price').get_text() for item in items]
favorites_actions =  [item.find(class_='favorites-actions').get_text() for item in items]
# coupon_link =  [item.find(class_='coupon-link').get_text() for item in items]

# print(cupon_title)
# print(coupon_listing_name)
# print(tempareture)



Coupons_And_Deals = pd.DataFrame(
    {
        'cupon_title' : cupon_title,
        'coupon_listing_name' : coupon_listing_name,
        'coupon_citystate' :coupon_citystate,
        'coupon_value' : coupon_value,
        'favorites_actions' : favorites_actions,
        # 'coupon_link' : coupon_link

    }
)


print(Coupons_And_Deals)
Coupons_And_Deals.to_csv('Coupons_And_Deals.csv')

