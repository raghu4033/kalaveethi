from django.db import models
from datetime import datetime    

# Create your models here.
class Admin_User(models.Model):
	email=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)

	def __str__(self):
		return self.email

class Student_reg(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	father_name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	father_mobile=models.CharField(max_length=100)
	CHOICES = (("male",'male'),("female",'female'),)
	gender=models.CharField(max_length=200,choices=CHOICES,default="")
	address=models.TextField()
	COURSE_CHOICES = (("fashion",'fashion'),("graphics",'graphics'),("fineart",'fineart'),("textile",'textile'),("jwellery",'jwellery'),)
	course=models.CharField(max_length=200,choices=COURSE_CHOICES,default="")
	password=models.CharField(max_length=100)
	cpassword=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="inactive")
	registration_id=models.CharField(max_length=100)
	dob=models.DateField(max_length=8)
	join_date=models.DateField(max_length=8)
	cast=models.CharField(max_length=100,default="")
	batch=models.CharField(max_length=100,default="")
	photo=models.ImageField(upload_to='images/',default="")

	def __str__(self):
		return self.fname+" "+self.lname+" "+self.course

class Student_Inquiry(models.Model):
	date=models.DateField(max_length=8)
	fname=models.CharField(max_length=100)
	CHOICES = (("male",'male'),("female",'female'),)
	gender=models.CharField(max_length=200,choices=CHOICES,default="")
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	dob=models.DateField(max_length=8)
	address=models.TextField()
	education=models.CharField(max_length=100)
	COURSE_CHOICES = (("fashion",'fashion'),("graphics",'graphics'),("fineart",'fineart'),("textile",'textile'),("jwellery",'jwellery'),)
	course=models.CharField(max_length=200,choices=COURSE_CHOICES,default="")
	reference=models.CharField(max_length=100)
	
	def __str__(self):
		return self.fname+" "+self.course

class fees_detaile(models.Model):
	registration_id=models.CharField(max_length=100)
	installment_no=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)
	payment_date=models.DateField(max_length=8)
	payment_type=models.CharField(max_length=100)
	recipt_no=models.CharField(max_length=100)
	recipt=models.FileField(upload_to='recipt/',default="")

	def __str__(self ):
		return self.registration_id+" "+self.amount

class Remaining_fees(models.Model):
	registration_id=models.CharField(max_length=100)
	installment_no=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)
	payment_date=models.DateField(max_length=8)

	def __str__(self ):
		return self.registration_id+" "+self.amount

class Event(models.Model):
	event_nm=models.CharField(max_length=100)
	place=models.CharField(max_length=100,default="kalaveethi Institute")
	event_date=models.DateField(max_length=8)
	event_time=models.TimeField(auto_now=False, auto_now_add=False)
	status=models.CharField(max_length=100,default="active")

	def __str__(self ):
		return self.event_nm+" "+self.place

class Holiday(models.Model):
	holiday_nm=models.CharField(max_length=100)
	holiday_date=models.DateField(max_length=8)
	holiday_day=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="active")

	def __str__(self ):
		return self.holiday_nm
class Notice(models.Model):
	
	COURSE_CHOICES = (("fashion",'fashion'),("graphics",'graphics'),("fineart",'fineart'),("textile",'textile'),("jwellery",'jwellery'),("all",'all'))
	notice=models.CharField(max_length=200,choices=COURSE_CHOICES,default="all")
	notice_sub=models.CharField(max_length=100)
	notice_date=models.DateField(max_length=8)
	notice_desc=models.TextField()
	status=models.CharField(max_length=100,default="active")

	def __str__(self ):
		return self.notice_sub+" "+self.notice_desc
class Createclass(models.Model):
	class_date=models.DateField(max_length=8)
	class_time=models.TimeField(auto_now=False, auto_now_add=False)
	subject=models.CharField(max_length=100)
	CLASS_CHOICES = (("lab",'lab'),("stitching",'stitching'),("theory",'theory'))
	classtype=models.CharField(max_length=200,choices=CLASS_CHOICES,default="")
	batch_nm=models.CharField(max_length=100)
	organizer=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="active")

	def __str__(self ):
		return self.subject+" "+self.classtype

class StudentLeave(models.Model):
	registration_id=models.CharField(max_length=100)
	sname=models.CharField(max_length=100)
	course=models.CharField(max_length=100)
	leavedate=models.DateField(max_length=8,default="")
	LEAVE_CHOICES = (("Sick_Leave",'Sick_Leave'),("Extended_Sick",'Extended_Sick'),("Emergency_Leave",'Emergency_Leave'),("Long_Leave",'Long_Leave'))
	Leave_catagory=models.CharField(max_length=200,choices=LEAVE_CHOICES,default="")
	leave_reason=models.CharField(max_length=100)
	leave_day=models.CharField(max_length=100)
	status=models.CharField(max_length=100,default="Panding_Request")

	def __str__(self ):
		return self.sname+" "+self.leave_reason

class StudentSubmitions(models.Model):
	COURSE_CHOICES = (("fashion",'fashion'),("graphics",'graphics'),("fineart",'fineart'),("textile",'textile'),("jwellery",'jwellery'),("all",'all'))
	submitions=models.CharField(max_length=200,choices=COURSE_CHOICES,default="all")
	submition_name=models.CharField(max_length=100)
	batch=models.CharField(max_length=100)
	topic=models.CharField(max_length=100)
	submition_desc=models.TextField()
	submition_date=models.DateField(max_length=8)
	submition_file=models.FileField(upload_to='student_submitions/',default="")
	status=models.CharField(max_length=100,default="deactive")

	def __str__(self ):
		return self.submition_name+" "+self.topic

class Suggestion(models.Model):
	registration_id=models.CharField(max_length=100)
	suggestion_msg=models.TextField()
	suggestion_date=models.DateTimeField(auto_now_add=True)

	def __str__(self ):
		return self.registration_id+" "+self.suggestion_msg
