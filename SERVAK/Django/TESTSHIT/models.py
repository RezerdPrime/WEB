# from django.db import models
# from django.contrib.auth.models import User
#
# class Gender_shit(models.Model):
#     gender = models.CharField("Gender",
#                               max_length=20,
#                               choices=[('1', 'parquet'), ('2', 'laminate'), ('3', 'helicopter boss')])
#
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
# class Math_shit(models.Model):
#     math = models.CharField("Fav_obj",
#                             max_length=20,
#                             choices=[('1', 'Gamma function'), ('2', 'Series of inverse squares'), ('3', 'Gaussian integral')])
#
#     user_id = models.ManyToManyField(User)