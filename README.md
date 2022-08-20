# Discord Amogus

Host this, and send https://your_host_url/amogus.jpg to your friends on Discord and ask them what number they see

Also ask them to click the image to zoom, and open it in browser after that :D

## Run it
Install dependencies from requirements.txt

```
$ pip install -r requirements.txt
```

Now run the server
```
$ python mogus.py
```

MAKE SURE TO HOST THIS SOMEWHERE SO YOUR FRIENDS CAN SEE IT (considering you have any). 
If you cannot afford/don't want a host, you can use something free like [Ngrok](https://ngrok.com/) to proxy the URL and make it public.

## How it works

The most important thing here is the Cache-Control header. When someone sees an image on Discord, the Discord CDN caches that image and others
can see the cached thing. BUT, if u disable cache control on your source server i.e this Python app, it will not cache it. So for every user who
sees the image, it will re-fetch it from the server.

On every request, this app generates a new number and creates a new image. So for every person, it will be a different number (fun to troll with).
When the request is received, it checks for Discord CDN's User Agent on the headers. If it's the CDN, it shows the image and disables cache.

If it's not a CDN agent i.e it's just a normal guy visiting from browser, redirect them to Among Drip video (be thankful it wasn't a rickroll).
