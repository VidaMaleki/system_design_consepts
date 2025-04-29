import string

class URLShortener:
    def __init__(self):
        self.url_to_id = {}
        self.id_to_url = {}
        self.counter = 1  # unique ID
        self.charset = string.ascii_letters + string.digits  # Base62 chars

    def _encode(self, id: int) -> str:
        base = len(self.charset)
        short = []
        while id > 0:
            short.append(self.charset[id % base])
            id //= base
        return ''.join(reversed(short))

    def _decode(self, short: str) -> int:
        base = len(self.charset)
        id = 0
        for char in short:
            id = id * base + self.charset.index(char)
        return id

    def shorten(self, long_url: str) -> str:
        if long_url in self.url_to_id:
            id = self.url_to_id[long_url]
        else:
            id = self.counter
            self.url_to_id[long_url] = id
            self.id_to_url[id] = long_url
            self.counter += 1
        return self._encode(id)

    def restore(self, short_url: str) -> str:
        id = self._decode(short_url)
        return self.id_to_url.get(id, None)


# Test it
if __name__ == "__main__":
    shortener = URLShortener()
    url = "https://example.com/article/12345"
    short = shortener.shorten(url)
    print(f"Shortened: {short}")
    original = shortener.restore(short)
    print(f"Restored: {original}")
