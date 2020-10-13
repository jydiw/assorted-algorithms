import time
from requests_html import HTMLSession

### input your variables here ###

# the url you want to check
# wrap it in quotes
BASE_URL = 'https://novelkeys.xyz/collections/keyboards/products/nk65-entry-edition'

# how often you want to check the site, in seconds
INTERVAL = 10

# if you want it to print "sold out" every INTERVAL seconds
VERBOSE = True



### HERE IS THE CODE // CHANGE IF YOU KNOW WHAT YOU'RE DOING ###

class Novelkeys(HTMLSession):

    def __init__(self, base_url):
        '''
        HTMLSession object as basis for check script

        base_url : str
        the url you want to check
        '''
        super().__init__()
        self.unavailable = True
        self.base_url = base_url

    def check(self, interval, verbose):
        '''
        basic script to check the page at some user-defined interval

        interval : int
        interval to refresh page, in seconds

        verbose : bool
        whether you want the script to continually update you that it's out of stock
        '''

        # this is to be nice to the site, which might ban you if you ping too often
        if interval <= 2:
            interval = 2
        
        # keep checking if it's unavailable
        # once it's "not unavailable", do something
        while self.unavailable:
            self.r = self.get(self.base_url)    # navigate to base_url
            self.html = self.r.html             # get the html for the page
            # the specific html for the "add to cart" button
            button_what = "//button[@id='AddToCart-product-template']"
            # search for the button
            self.button = self.html.xpath(button_what, first=True)
            # get the text in the button
            self.span = self.button.xpath("//span", first=True)
            # check the contents of the text
            if self.span.text.lower() not in ['unavailable', 'sold out']:
                self.unavailable = False
                print("---------AVAILABLE---------")
                # here goes code to notify or even purchase
                # fill in later
            elif verbose:
                print(self.button.text.lower())
            time.sleep(interval)



### actually running the script ###

nk = Novelkeys(base_url=BASE_URL)
nk.check(interval=INTERVAL, verbose=VERBOSE)