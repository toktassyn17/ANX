from django.db import models


class Subscriber(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = "MySubscribers"
        verbose_name_plural = "Subscribers"



class Task(models.Model):

    title = models.CharField('Title', max_length=50)
    task = models.TextField('Definition')
    email = models.CharField(max_length = 200, null = True )
    digital = models.BooleanField(default=False, null = True, blank = False)
    image = models.ImageField(null = True, blank = True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'





# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True , blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     price = models.FloatField()
#     digital = models.BooleanField(default=False, null=True, blank=False)
#
#     def __str__(self):
#         return self.name
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#     date_ordered = models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_id = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
# class OrderItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)


