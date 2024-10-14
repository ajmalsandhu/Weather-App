from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import requests

# Function to get weather data
def data_get():
    city = city_name.get()  # Get the city from the combobox
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=15b77f3b0ebade4d9701629b20919745").json()
    
    wc_lable1.config(text=data["weather"][0]["main"])  # Weather condition
    wd_lable1.config(text=data["weather"][0]["description"])  # Weather description
    temp_lable1.config(text=str(int(data["main"]["temp"] - 273.15)))  # Temperature in Celsius
    pre_lable1.config(text=data["main"]["pressure"])  # Pressure
    hmdty_lable1.config(text=data["main"]["humidity"])  # Humidity

# Create main window
win = Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("530x550")  # Set window size

# To set Background Image (line 25 - 30)
img = Image.open('E:\Practice Python\Projects\weatherbg.jpeg')
resized_img = img.resize((530,550)) # there is a problem that background image cannot fit the geometry size.
img = ImageTk.PhotoImage(resized_img)

img_label = Label(win, image=img, bg='#0096DC')
# img_label.pack(pady=(10,10))# here if we cannot give pady then the background image is fit in background
img_label.pack()

# App title label
name_lable = Label(win, text="Weather App", font=("Time new Roman", 30, "bold"))
name_lable.place(x=100, y=25, height=50, width=300)

# List of cities
list_name = ["Ahmadpur East"," Ahmed Nager Chatha"," Ali Khan Abad"," Alipur"," Arifwala"," Attock"," Bhera"," Bhalwal"," Bahawalnagar"," Bahawalpur"," Bhakkar"," Burewala"," Chillianwala"," Choa Saidanshah"," Chakwal"," Chak Jhumra"," Chichawatni"," Chiniot"," Chishtian"," Chunian"," Dajkot"," Daska"," Davispur"," Darya Khan"," Dera Ghazi Khan"," Dhaular"," Dina"," Dinga"," Dhudial Chakwal"," Dipalpur"," Faisalabad"," Fateh Jang"," Ghakhar Mandi"," Gojra"," Gujranwala"," Gujrat"," Gujar Khan"," Harappa"," Hafizabad"," Haroonabad"," Hasilpur"," Haveli Lakha"," Jalalpur Jattan"," Jampur"," Jaranwala"," Jhang"," Jhelum"," Kallar Syedan"," Kalabagh"," Karor Lal Esan"," Kasur"," Kamalia"," Kāmoke"," Khanewal"," Khanpur"," Khanqah Sharif"," Kharian"," Khushab"," Kot Adu"," Jauharabad"," Lahore"," Islamabad"," Lalamusa"," Layyah"," Lawa Chakwal"," Liaquat Pur"," Lodhran"," Malakwal"," Mamoori"," Mailsi"," Mandi Bahauddin"," Mian Channu"," Mianwali"," Miani"," Multan"," Murree"," Muridke"," Mianwali Bangla"," Muzaffargarh"," Narowal"," Nankana Sahib"," Okara"," Renala Khurd"," Pakpattan"," Pattoki"," Pindi Bhattian"," Pind Dadan Khan"," Pir Mahal"," Qaimpur"," Qila Didar Singh"," Rabwah"," Raiwind"," Rajanpur"," Rahim Yar Khan"," Rawalpindi"," Sadiqabad"," Sagri"," Sahiwal"," Sambrial"," Samundri"," Sangla Hill"," Sarai Alamgir"," Sargodha"," Shakargarh"," Sheikhupura"," Shujaabad"," Sialkot"," Sohawa"," Soianwala"," Siranwali"," Tandlianwala"," Talagang"," Taxila"," Toba Tek Singh"," Vehari"," Wah Cantonment"," Wazirabad"," Yazman"," Zafarwal",] 

# Combobox for selecting city
city_name = StringVar()  # Properly initialize StringVar
com = ttk.Combobox(win, values=list_name, font=("Time new Roman", 20), textvariable=city_name)
com.place(x=125, y=100, height=45, width=250)

# Labels for displaying weather information

# for weather climate
wc_lable = Label(win, text="Weather Climate", font=("Time new Roman", 20))
wc_lable.place(x=25, y=230, height=40, width=230)

wc_lable1 = Label(win, text="", font=("Time new Roman", 20))
wc_lable1.place(x=270, y=230, height=40, width=230)

# for weather description

wd_lable = Label(win, text="Weather Description", font=("Time new Roman", 18))
wd_lable.place(x=25, y=290, height=40, width=230)

wd_lable1 = Label(win, text="", font=("Time new Roman", 20))
wd_lable1.place(x=270, y=290, height=40, width=230)

# for Temperature

temp_lable = Label(win, text="Temperature", font=("Time new Roman", 20))
temp_lable.place(x=25, y=350, height=40, width=230)

temp_lable1 = Label(win, text="", font=("Time new Roman", 20))
temp_lable1.place(x=270, y=350, height=40, width=230)

# for Pressure

pre_lable = Label(win, text="Pressure", font=("Time new Roman", 20))
pre_lable.place(x=25, y=410, height=40, width=230)

pre_lable1 = Label(win, text="", font=("Time new Roman", 20))
pre_lable1.place(x=270, y=410, height=40, width=230)

# for Humidity

hmdty_lable = Label(win, text="Humidity", font=("Time new Roman", 20))
hmdty_lable.place(x=25, y=470, height=40, width=230)

hmdty_lable1 = Label(win, text="", font=("Time new Roman", 20))
hmdty_lable1.place(x=270, y=470, height=40, width=230)


# Search button
done_button = Button(win, text="Search", font=("Time new Roman", 20, "bold"), command=data_get)
done_button.place(x=200, y=170, height=40, width=100)

# Start the Tkinter event loop
win.mainloop()









#                  ***** Simple Code with reference website *****

# import requests
# val = input('Enter City: ')
# url = 'https://wttr.in/{}'.format(val)
# response = requests.get(url)
# weather_data = response.text
# print(weather_data)