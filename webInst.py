import urllib.request

def downloadImage(url):
	opener=urllib.request.build_opener()
	opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
	urllib.request.install_opener(opener)

	# url='https://cdn.pixabay.com/photo/2012/08/27/14/19/mountains-55067_960_720.png'
	local='static/img/webImage.jpg'
	urllib.request.urlretrieve(url,local)
