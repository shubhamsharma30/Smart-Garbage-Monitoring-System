# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  name=models.CharField(max_length=30)
  contact_no=models.CharField(max_length=10)

  def __str__(self):
    return self.user.username



class D_Details(models.Model):
  Name = models.CharField(max_length=200)
  Address = models.CharField(max_length=200)
  Ph_no = models.CharField(max_length=10)
  Truck_no = models.CharField(max_length=200)

  def __str__(self):
    return self.Name


class C_Details(models.Model):

  C_Name = models.CharField(max_length=200)
  C_Address = models.CharField(max_length=200)
  C_Ph_no = models.CharField(max_length=10)
  C_D_id = models.ForeignKey(D_Details, on_delete=models.CASCADE)
  C_Dustbin_ID = models.CharField(max_length=200)

  def __str__(self):
    return self.C_Name


class Trashcan1(models.Model):
  T_ID = models.CharField(max_length=10)
  T_x_c = models.CharField(max_length=14)
  T_y_c = models.CharField(max_length=14)
  T_C_id = models.ForeignKey(C_Details, on_delete=models.CASCADE, default="")
  T_D_id = models.ForeignKey(D_Details, on_delete=models.CASCADE, default="")
