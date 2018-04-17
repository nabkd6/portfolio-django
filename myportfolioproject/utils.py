
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image.url
