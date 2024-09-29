from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='books/pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    cover_page = models.ImageField(upload_to='upload/book/', default='')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return self.title

class category(models.Model):

    name= models.CharField(max_length=200)
    image_cat = models.ImageField(upload_to='upload/book/', default='')

    def __str__(self):
        return self.name