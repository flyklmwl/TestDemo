import json
import tkinter as tk
import tkinter.messagebox
import urllib.request

#path="Settings1.json"
#url = ''
path="F:\Settings1.json"

def loadUrl(url):

	f = urllib.request.urlopen(url)
	html = f.read()
	return html

def loadfile(path):
	f = open(path,encoding='utf-8')
	setting = json.load(f)
	#family = setting['BaseSettings']['size']
	#size = setting['fontSize']
	#return family
	
	#success = setting['successful']
	maxcount = setting['resultValue']['itemCount'] - 1	
	busiinstOrderAbstract = []

	for num in range(0,maxcount):
		#print(busiinstOrderAbstract)
		#busiinstOrderAbstract = setting['resultValue']['items'][num]['busiinstOrderAbstract']	
		busiinstOrderAbstract.append(setting['resultValue']['items'][num]['busiinstOrderAbstract'])
		if (setting['resultValue']['items'][num]['busiinstOrderAbstract'] == "营销GIS"):
			root = tk.Tk()
			root.geometry('0x0')
			root.attributes('-alpha',0)
			tk.messagebox.showinfo('提示','营销GIS')
	return busiinstOrderAbstract


if(__name__=="__main__"):
	#t = loadUrl(url)
	t = loadfile(path)
	print(t)


#root = tk.Tk()
#root.geometry('0x0')
#root.attributes('-alpha',0)
#tk.messagebox.showinfo('提示ʾ','人生苦短')
