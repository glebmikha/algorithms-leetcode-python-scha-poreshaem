import hashlib


class Codec:

    def __init__(self):
        self.url_db = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        shortUrl = hashlib.sha1(longUrl.encode('utf-8')).hexdigest()[:6]
        self.url_db[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_db[shortUrl]

if __name__ == '__main__':
    c = Codec()
    url = 'abds'
    shorten = c.encode(url)
    print(shorten)
    original = c.decode(shorten)
    print(original)
