import webbrowser
fav_websites = ['https://www.youtube.com/', 'https://fitgirl-repacks.site/', 'https://fmovies24.to/home', 'https://github.com/', 'https://www.hackerrank.com/dashboard']
for website_index in range(len(fav_websites)):
    print("%d- "%(website_index+1) + fav_websites[website_index][fav_websites[website_index].index('//') + 2 : fav_websites[website_index].rindex('.')].removeprefix('www.'))
choice = int(input("Choose a website: "))
webbrowser.open(fav_websites[choice - 1])
