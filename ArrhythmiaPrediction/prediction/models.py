# from django.db import models
# from PIL import Image
#
# # Create your models here.
# class Upload(models.Model):
#     image = models.ImageField(default='default.jpg', upload_to='images')
#
#
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
#         img = Image.open(self.image.path)
#
#         if img.height > 128 or img.width > 128:
#             output_size = (128, 128)
#             img.thumbnail(output_size)
#             img.save(self.image.path)