import random


class Codec:

    dataset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdeghijklmnopqrstuvwxyz0123456789'

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.dataset) for _ in range(8))

            while code in self.code2url:
                code = ''.join(random.choice(Codec.dataset) for _ in range(8))

            self.code2url[code] = longUrl
            self.url2code[longUrl] = code

        return "http://tinyurl.com/" + str(self.url2code[longUrl])

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """

        return self.code2url[shortUrl[-8:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
