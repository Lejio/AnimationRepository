import webview

window = webview.create_window('Woah dude!', 'https://projectvoltair.com')
webview.start()
print(window.get_elements('.main'))