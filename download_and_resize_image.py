import os
import urllib.request
import requests
from PIL import Image
from io import BytesIO
def download_image(hotel,hotel_id,url):
	image_id = url.split('/')[-1]
	"""urllib.request.urlretrieve(url,os.path.join(os.getcwd(),"hotels/"+hotel+"/"+hotel_id+"/"+image_id))"""
	image_response=requests.get(url)
	image=resize_image(image_response)
	image.save(os.path.join(os.getcwd(),"hotels/"+hotel+"/"+hotel_id+"/"+image_id))

def resize_image(image_response):
	image=Image.open(BytesIO(image_response.content))
	nx,ny=image.size
	return image.resize((int(nx*0.75),int(ny*0.75)),Image.ANTIALIAS)
	
# hotel_info=get_image_url_json()
hotel_info={'oyo-hotel': {'MCD020': ['https://images.oyoroomscdn.com/uploads/hotel_image/6736/8684f1a8345884dc.jpg','https://images.oyoroomscdn.com/uploads/hotel_image/6736/775ea9e6edabbedc.jpg'],
                        'KOL168': ['https://images.oyoroomscdn.com/uploads/hotel_image/4151/b7e540898f3d3c1c.jpg', 'https://images.oyoroomscdn.com/uploads/hotel_image/4151/a1fdc42c7325aaa2.jpg'], 
                        'MY_KKB011': ['https://images.oyoroomscdn.com/uploads/hotel_image/11130/c5f415992f9e15f4.jpg', 'https://images.oyoroomscdn.com/uploads/hotel_image/11130/3a80c8e6d2ac1df6.jpg'],
                        'DEL551': ['https://images.oyoroomscdn.com/uploads/hotel_image/8992/16f5e5ace7ee468f.jpg', 'https://images.oyoroomscdn.com/uploads/hotel_image/8992/fd7429d8d1bcd27f.jpg']
                        }}
                        


current_directory=os.getcwd()
directory=os.makedirs('hotels')

for hotel in hotel_info:
    os.makedirs(os.path.join(os.getcwd(),"hotels/"+hotel))
    for hotel_id in hotel_info[hotel]:
        os.makedirs(os.path.join(os.getcwd(),"hotels/"+hotel+"/"+hotel_id))
        for url in hotel_info[hotel][hotel_id]:
            download_image(hotel,hotel_id,url)
