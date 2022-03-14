# Insta Likes
### _Scrape and display your Instagram likes_
Download every image you've liked on Instagram.\
Optionally use the included HTML page to display them in the browser.

Instagram does not allow you to view your liked posts from the browser, only in the app. This script emulates the app to get your likes, then enables you to display them in the browser.\
You have to scrape the images first, because Instagram prevents hot-linking with a CORP header.

## Usage
Requirements: python3 and 'requests' `python -m pip install requests`

* Open `get-likes.py` and enter your username and password.
* Run `./get-likes.py` which creates two files:
  * _creds-username.json_ - Saves your session variables, so it doesn't have to login every time it runs.
  * _likes.json_ - All your liked posts on Instagram.
* `./scrape-images.py`
  * Saves the highest resolution version of every image in _likes.json_.
  * Saves the profile picture of the owner of every liked post.
  * Skips any pre-existing images.
  * Names images: $DIR/yyyy-mm-dd_username_code.jpg
    * If image is part of a carousel, _'-n'_ will be appended.
    * $DIR is defined in the script. If you change it, also change it in _my_likes.html_.

### About
The backend API code was forked from [instagram_private_api](https://github.com/ping/instagram_private_api). I just kept what I needed for the single API call this script uses, and wrote all the scripts mentioned above.\
It saves all files with a .jpg extension because some of the images it downloaded had a different extension but were actually jpeg. I have not ran across an image that wasn't jpeg, but if you do, LMK. The code for using the extension from the image URL is in _scrape-images.py_ just commented out.\
Session credentials expire after 90 days, so you may need to periodically delete them.

### Support
I am glad to fix bugs with the code, but if your problem is with Python, go to Google.\

### License
[MIT](LICENSE)
