from tkinter import *
import requests

country = {'AED': 3.6718, 'ALL': 89.334999, 'ANG': 1.78, 'ARS': 3.0675, 'AUD': 1.2642, 'AWG': 1.79, 'BBD': 1.97, 'BDT': 66.655998, 'BGN': 1.4746, 'BHD': 0.36129, 'BIF': 954.859985, 'BMD': 1.001, 'BND': 1.5059, 'BOB': 7.995, 'BRL': 2.1325, 'BSD': 0.9975, 'BWP': 6.0334, 'BZD': 1.8723, 'CAD': 1.1643, 'CDF': 540.0, 'CHF': 1.2166, 'CLP': 532.25, 'CNY': 7.806, 'COP': 2237.5, 'CRC': 519.0, 'CUP': 0.9601, 'CVE': 80.124001, 'CYP': 0.4369, 'CZK': 20.756001, 'DJF': 166.740005, 'DKK': 5.6397, 'DOP': 33.08, 'DZD': 68.9855, 'EGP': 5.6647, 'ETB': 8.438, 'EUR': 0.75649, 'FJD': 1.6668, 'GBP': 0.50911, 'GMD': 26.489, 'GNF': 5429.799805, 'GTQ': 7.622, 'HKD': 7.7749, 'HNL': 18.89, 'HRK': 5.5708, 'HTG': 35.299, 'HUF': 189.940002, 'IDR': 8965.700195, 'ILS': 4.2145, 'INR': 44.215, 'IQD': 1260.400024, 'IRR': 8830.099609, 'ISK': 69.211998, 'JMD': 66.0, 'JOD': 0.704, 'JPY': 118.879997, 'KES': 66.211998, 'KHR': 3889.399902, 'KMF': 376.0, 'KRW': 917.22998, 'KWD': 0.2876, 'KYD': 0.82, 'KZT': 126.81, 'LAK': 9296.900391, 'LBP': 1512.0, 'LKR': 103.040001, 'LSL': 6.975, 'LTL': 2.5839, 'LVL': 0.52043, 'LYD': 1.2216, 'MAD': 8.466, 'MDL': 12.945, 'MGA': 2020.0, 'MKD': 46.675, 'MMK': 818.0, 'MNT': 1165.5, 'MOP': 7.685, 'MRO': 267.05, 'MUR': 33.25, 'MVR': 12.8, 'MWK': 134.490005, 'MXN': 10.803, 'MYR': 3.5231, 'NAD': 6.996, 'NGN': 128.8, 'NIO': 17.9, 'NOK': 6.2231, 'NPR': 66.862999, 'NZD': 1.4172, 'OMR': 0.38399, 'PAB': 0.96366, 'PEN': 3.19625, 'PGK': 2.8088, 'PHP': 48.950001, 'PKR': 60.880001, 'PLN': 2.8984, 'PYG': 5170.0, 'QAR': 3.4809, 'RON': 2.5559, 'RSD': 60.49, 'RUB': 26.305, 'RWF': 524.869995, 'SAR': 3.7498, 'SBD': 7.467503, 'SCR': 5.4468, 'SEK': 6.8413, 'SGD': 1.532, 'SIT': 181.479996, 'SLL': 3000.0, 'SOS': 1248.199951, 'STD': 6785.0, 'SVC': 8.75, 'SYP': 49.82, 'SZL': 6.975, 'THB': 35.291, 'TND': 1.302, 'TRY': 1.408, 'TTD': 6.33, 'TWD': 32.575001, 'TZS': 1263.5, 'UAH': 5.053, 'UGX': 1743.0, 'UYU': 24.4, 'UZS': 1240.0, 'VND': 15374.0, 'VUV': 102.0, 'WST': 2.747771, 'XAF': 477.01001, 'XOF': 497.05, 'XPF': 95.55, 'YER': 196.75, 'ZAR': 7.0, 'ZMK': 4427.0}

HEIGHT = 500
WIDTH = 600

root = Tk()
root.title('Forex Exchange')
root.geometry('800x800')
nations = list(country.keys())
nat = StringVar(root)
nat.set('Currency') 

amount = StringVar(root)
amount.set('Enter your USD amount')

def format_response(currency):
	value = currency['rates'][nat.get()]
	value = int(entry.get())* value

	final_str = 'Converted value: %f %s' % (value, nat.get())

	return final_str
def convert():
	key = 'b5449979-dfb8-4e8b-9780-5ea0e3e19144'
	url = 'https://v2.api.forex/rates/latest.json'
	params={'beautify':True, 'key':key}
	data = requests.get(url, params=params)
	currency = data.json()
	label['text'] =  format_response(currency)
	

background_image = PhotoImage(file='aa.png')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, textvariable=amount,font=40)
entry.place(relwidth=0.3, relheight=1)

cald = OptionMenu(frame, nat, *nations)  
cald.place(relx=0.4,relwidth=0.2, relheight=0.8)

button = Button(frame, text="convert?", font=40, command = lambda:convert())
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = Label(lower_frame, font=('times new roman', 20))
label.place(relwidth=1, relheight=1)

root.mainloop()
