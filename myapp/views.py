from django.shortcuts import render,redirect
from django.conf import settings
import datetime
from .models import Admin_User,Student_reg,Student_Inquiry,fees_detaile,Remaining_fees,Event,Holiday,Notice,Createclass,StudentLeave,StudentSubmitions,Suggestion
# Create your views here.
def index(request):
	return render(request,'login.html')

def admin_login(request):
	if request.method=="POST":
		admin_email=request.POST['admin_email']
		admin_password=request.POST['admin_password']
		try:
			admin_user=Admin_User.objects.get(email=admin_email,password=admin_password)
			request.session['admin_email']=admin_user.email
			return render(request,'admin_dashboard.html')
		except:
			msg="Encorect Email or Password"
			return render(request,'index.html',{'msg':msg})
	else:
		return render(request,'admin_login.html')
def admin_dashboard(request):
		return render(request,'admin_dashboard.html')
def logout(request):
	try:
		del request.session['admin_email']
		return render(request,'index.html')
	except:
		pass
def Student_Registration(request):
	if request.method=="POST":
		f=request.POST['fname']
		l=request.POST['lname']
		fn=request.POST['father_name']
		e=request.POST['email']
		m=request.POST['mobile']
		fmo=request.POST['father_mobile']
		dob=request.POST['dob']
		cast=request.POST['cast']
		gender=request.POST['gender']
		add=request.POST['address']
		course=request.POST['course']
		reg_id=request.POST['registration_id']
		join_dt=request.POST['join_date']
		p=request.POST['password']
		cp=request.POST['cpassword']
		ph=request.FILES['photo']
		bnm=request.POST['batch_name']
		try:
			student=Student_reg.objects.get(registration_id=reg_id)
			msg="Student Id Alredy Registered"
			return render(request,'Student_Registration.html',{'msg':msg})
		except:
			if p==cp:
				Student_reg.objects.create(fname=f,lname=l,father_name=fn,email=e,mobile=m,father_mobile=fmo,gender=gender,address=add,course=course,registration_id=reg_id,dob=dob,join_date=join_dt,cast=cast,batch=bnm,password=p,cpassword=cp,photo=ph)
				# rec=[e,]
				# subject="OTP for Successefully Regisration"
				# otp=random.randint(1000,9999)
				# massege="Your OTP For Registration Is"+" "+str(otp)
				# email_from=settings.EMAIL_HOST_USER
				# send_mail(subject,massege,email_from,rec)
				msg="Student Registered Successefully"
				return render(request,'Student_Registration.html',{'msg':msg})
			else:
				msg="Password Does Not Match"
				return render(request,'Student_Registration.html',{'msg':msg})
	else:
		return render(request,'Student_Registration.html')

def student_login(request):
	if request.method=="POST":
		student_id=request.POST['student_id']
		student_password=request.POST['student_password']
		try:
			student=Student_reg.objects.get(registration_id=student_id,password=student_password)
			request.session['fname']=student.fname
			request.session['student_id']=student.registration_id
			request.session['photo']=student.photo.url

			student=Student_reg.objects.get(registration_id=request.session['student_id'])
			total_submitions=StudentSubmitions.objects.filter(batch=student.batch)
			request.session['total_submitionslen']=len(total_submitions)

			return redirect('student_dashboard')
		except:
			msg="Encorect Email or Password"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'index.html')
def student_logout(request):
	try:
		del request.session['student_id']
		del request.session['fname']
		del request.session['photo']
		del request.session['total_submitionslen']
		return render(request,'login.html')
	except:
		pass
def View_Students(request):
	student=Student_reg.objects.all()
	return render(request,'student_list.html',{'student':student})

def student_moreinfo(request,pk):
	student=Student_reg.objects.get(pk=pk)
	return render(request,'student_moreinfo.html',{'student':student})

def delete_student(request,pk):
	student=Student_reg.objects.get(pk=pk)
	student.delete()
	msg="Student Deleted Successfully"
	student=Student_reg.objects.all()
	return render(request,'student_list.html',{'student':student,'msg':msg})

def student_profile(request):
	student=Student_reg.objects.get(registration_id = request.session['student_id'])
	return render(request,'student_profile.html',{'student':student})

def student_dashboard(request):
	total_amount=[]
	student=Student_reg.objects.get(registration_id=request.session['student_id'])
	classlist=Createclass.objects.filter(batch_nm=student.batch).order_by('-id')[:2]

	holiday=Holiday.objects.all().order_by('-id')[0:1]

	notice=Notice.objects.all().order_by('-id')[0:1]

	event=Event.objects.all().order_by('-id')[0:1]

	total_holiday=Holiday.objects.all()
	total_holidaylen=len(total_holiday)
	total_event=Event.objects.all()
	total_eventlen=len(total_event)
	total_notice=Notice.objects.all()
	total_noticelen=len(total_notice)

	total_fees=fees_detaile.objects.filter(registration_id=request.session['student_id'])
	total_feeslen=len(total_fees)
	for i in total_fees:
			total_amount.append(int(i.amount))
	total_feeslen = sum(total_amount)

	now = datetime.datetime.now()
	print(now)
	total_submitionslen=""
	student=Student_reg.objects.get(registration_id=request.session['student_id'])
	total_submitions=StudentSubmitions.objects.filter(batch=student.batch)
	request.session['total_submitionslen']=len(total_submitions)


	return render(request,'Student_main_dashboard.html',{'now':now ,'classlist':classlist,'holiday':holiday,'notice':notice,'event':event,'total_holidaylen':total_holidaylen,'total_eventlen':total_eventlen,'total_noticelen':total_noticelen,'total_submitionslen':total_submitionslen,'total_feeslen':total_feeslen})

def student_change_password(request):
	if request.method=="POST":
		old_password=request.POST['old_pass']
		password=request.POST['pass']
		cpassword=request.POST['cpass']
		try:
			student=Student_reg.objects.get(registration_id = request.session['student_id'])
			if student.password==old_password and password==cpassword:
				student.password=password
				student.cpassword=password
				student.save()
				return redirect('student_logout')
			else:
				msg="Password & Confirm Password Does Not Matched"
				return render(request,'student_change_password.html',{'msg':msg})
		except:
			pass
	else:
		return render(request,'student_change_password.html')

def edit_std_detail(request,pk):
	student=Student_reg.objects.get(pk=pk)
	return render(request,'edit_std_detail.html',{'student':student})

def student_inquiry(request):
	if request.method=="POST":
		date=request.POST['date']
		f=request.POST['fname']
		e=request.POST['email']
		m=request.POST['mobile']
		dob=request.POST['dob']
		gender=request.POST['gender']
		add=request.POST['address']
		course=request.POST['course']
		edu_que=request.POST['education']
		ref=request.POST['refrence']
		try:
			Student_Inquiry.objects.create(date=date,fname=f,gender=gender,email=e,mobile=m,dob=dob,address=add,course=course,education=edu_que,reference=ref)
			# rec=[e,]
			# subject="OTP for Successefully Regisration"
			# otp=random.randint(1000,9999)
			# massege="Your OTP For Registration Is"+" "+str(otp)
			# email_from=settings.EMAIL_HOST_USER
			# send_mail(subject,massege,email_from,rec)
			msg="Student Inquery Registered Successefully"
			return render(request,'student_inquiry.html',{'msg':msg})
		except:
			msg="Student Data not Submited"
			return render(request,'student_inquiry.html',{'msg':msg})
	else:
		return render(request,'student_inquiry.html')

def student_inquiry_list(request):
	student=Student_Inquiry.objects.all()
	return render(request,'student_inquiry_list.html',{'student':student})
def add_fees(request):
	return  render(request,'add_fees.html')
def add_std_attendence(request):
	return render(request,'add_std_attendence.html')
def fill_attendence(request):
	course_id=request.POST['course_id']
	batch_id=request.POST['batch_id']
	student=Student_reg.objects.filter(course=course_id,batch=batch_id)
	return render(request,'fill_attendence.html',{'student':student})
def add_fees(request):
	return render(request,'add_fees.html')
def fees_details(request):
	sid=request.POST['registration_id']
	try:
		student=Student_reg.objects.get(registration_id=sid)
		try:
			fees=fees_detaile.objects.filter(registration_id=sid)
			rem_fees=Remaining_fees.objects.filter(registration_id=sid)
			return render(request,'fees_details.html',{'student':student,'fees':fees,'rem_fees':rem_fees})
		except:
			feesmsg="No Installment Found"
			rem_feesmsg="No panding Installment Found"
			return render(request,'fees_details.html',{'student':student,'feesmsg':feesmsg,'rem_feesmsg':rem_feesmsg})
	except:
		msg="No Student Data Found"
		return render(request,'add_fees.html',{'msg':msg})
def sid_list(request):
	student=Student_reg.objects.all()
	return render(request,'sid_list.html',{'student':student})

def add_installment(request):
	sid=request.POST['sid']
	return render(request,'add_installment.html',{'sid':sid})

def add_remaining_ins(request):
	sid=request.POST['sid']
	return render(request,'add_remaining_ins.html',{'sid':sid})

def add_fees_record(request):
	if request.method=="POST":
		sid=request.POST['sid']
		ins_num=request.POST['ins_num']
		Amount=request.POST['Amount']
		pdate=request.POST['pdate']
		ptype=request.POST['ptype']
		rec_num=request.POST['rec_num']
		Recipt=request.FILES['Recipt']
		try:
			fees_detaile.objects.create(registration_id=sid,installment_no=ins_num,amount=Amount,payment_date=pdate,payment_type=ptype,recipt_no=rec_num,recipt=Recipt)
			msg="Student Installment Registered Successefully"
			return render(request,'add_installment.html',{'msg':msg})
		except:
			msg="Student Installment Not Registered"
			return render(request,'add_installment.html',{'msg':msg})
	else:
		return render(request,'add_installment.html')



def insert_remeining_ins(request):
	if request.method=="POST":
		sid=request.POST['sid']
		ins_num=request.POST['ins_num']
		Amount=request.POST['Amount']
		pdate=request.POST['pdate']
		try:
			Remaining_fees.objects.create(registration_id=sid,installment_no=ins_num,amount=Amount,payment_date=pdate)
			msg="Student Installment Registered Successefully"

			return render(request,'add_remaining_ins.html',{'msg':msg})
		except:
			msg="Student Installment Not Registered"
			return render(request,'add_remaining_ins.html',{'msg':msg})
	else:
		return render(request,'add_remaining_ins.html')
 
def event(request):
	event=Event.objects.all()
	return render(request,'event.html',{'event':event})
	print(event)
def insert_event(request):
	event=Event.objects.all().order_by('-id')
	if request.method=="POST":
		event_name=request.POST['event_name']
		edate=request.POST['edate']
		etime=request.POST['etime']
		place=request.POST['place']
		try:
			Event.objects.create(event_nm=event_name,event_date=edate,event_time=etime,place=place)
			msg="Event Registered Successefully"
			return render(request,'event.html',{'msg':msg,'event':event})
		except:
			msg="Event Can't Registered"
			return render(request,'event.html',{'msg':msg,'event':event})
	else:
		return render(request,'event.html',{'event':event})

def holiday(request):
	holiday=Holiday.objects.all().order_by('-id')
	if request.method=="POST":
		holidays_name=request.POST['Holidays_name']
		hdate=request.POST['hdate']
		holiday_days=request.POST['holiday_days']
		try:
			Holiday.objects.create(holiday_nm=holidays_name,holiday_date=hdate,holiday_day=holiday_days)
			msg="Holiday Registered Successefully"
			return render(request,'holiday.html',{'msg':msg,'holiday':holiday})
		except:
			msg="Event Can't Registered"
			return render(request,'holiday.html',{'msg':msg,'holiday':holiday})
	else:
		return render(request,'holiday.html',{'holiday':holiday})
def demo(request):
	return render(request,'enroll_student.html')
def notice(request):
	notice=Notice.objects.all().order_by('-id')
	if request.method=="POST":
		notice_id=request.POST['notice_id']
		sname=request.POST['sname']
		ndate=request.POST['ndate']
		desc=request.POST['desc']
		try:
			Notice.objects.create(notice=notice_id,notice_sub=sname,notice_date=ndate,notice_desc=desc)
			msg="Notice Registered Successefully"
			return render(request,'notice.html',{'msg':msg,'notice':notice})
		except:
			msg="Notice Can't Registered"
			return render(request,'notice.html',{'msg':msg,'notice':notice})
	else:
		return render(request,'notice.html',{'notice':notice})
def Submitions(request):
	Submitionslist=StudentSubmitions.objects.all().order_by('-id')[:3]
	if request.method=="POST":
		submition_id=request.POST['submition_id']
		sname=request.POST['sname']
		batch=request.POST['batch']
		topic=request.POST['topic']
		desc=request.POST['desc']
		edate=request.POST['edate']
		sfile=request.FILES['sfile']
		try:
			StudentSubmitions.objects.create(submitions=submition_id,submition_name=sname,batch=batch,topic=topic,submition_desc=desc,submition_date=edate,submition_file=sfile)
			msg="Submitions Added Successefully"
			return render(request,'Submitions.html',{'msg':msg,'Submitionslist':Submitionslist})
		except:
			msg="Submitions Can't Added"
			return render(request,'Submitions.html',{'msg':msg,'Submitionslist':Submitionslist})
	else:
		return render(request,'Submitions.html',{'Submitionslist':Submitionslist})
def student_fees_detaile(request):
	rem_fees=Remaining_fees.objects.filter(registration_id=request.session['student_id'])
	fees=fees_detaile.objects.filter(registration_id=request.session['student_id'])
	return render(request,'student_fees_detaile.html',{'fees':fees,'rem_fees':rem_fees})
def student_notice_board(request):
	student=Student_reg.objects.get(registration_id=request.session['student_id'])
	notice=Notice.objects.filter(notice=student.course).order_by('-id')
	allnotice=Notice.objects.filter(notice="all").order_by('-id')
	return render(request,'student_notice_board.html',{'notice':notice,'allnotice':allnotice})
def student_holiday(request):
	holiday=Holiday.objects.all().order_by('-id')
	return render(request,'student_holiday.html',{'holiday':holiday})
def student_event(request):
	event=Event.objects.all().order_by('-id')
	return render(request,'student_event.html',{'event':event})
def student_attendence(request):
	return render(request,'student_attendence.html')
def pay_fees(request):
	return render(request,'pay_fees.html')
def student_class(request):
	student=Student_reg.objects.get(registration_id=request.session['student_id'])
	classlist=Createclass.objects.filter(batch_nm=student.batch).order_by('-id')[:5]
	return render(request,'student_class.html',{'classlist':classlist})
def student_submitions(request):
	student=Student_reg.objects.get(registration_id=request.session['student_id'])
	stud_Submitionslist=StudentSubmitions.objects.filter(batch=student.batch).order_by('-id')[:3]
	return render(request,'student_submitions.html',{'stud_Submitionslist':stud_Submitionslist})
def student_leave(request):
	student=Student_reg.objects.get(registration_id=request.session['student_id'])
	if request.method=="POST":
		Regisreation_id=request.POST['Regisreation_id']
		sname=request.POST['sname']
		course=request.POST['course']
		ldate=request.POST['ldate']
		leave_catagory=request.POST['leave_catagory']
		leave_Reason=request.POST['leave_Reason']
		leave_day=request.POST['leave_day']
		try:
			StudentLeave.objects.create(registration_id=Regisreation_id,sname=sname,course=course,leavedate=ldate,Leave_catagory=leave_catagory,leave_reason=leave_Reason,leave_day=leave_day)
			
			msg="Leave Request Send Successefully"
			leavelist=StudentLeave.objects.filter(status="Panding_Request",registration_id=request.session['student_id'])[:1]
			return render(request,'student_leave.html',{'student':student,'msg':msg,'leavelist':leavelist})
		except:
			msg="Leave Can't Registered"
			leavelist=StudentLeave.objects.filter(status="Panding_Request",registration_id=request.session['student_id'])[:1]			
			return render(request,'student_leave.html',{'student':student,'msg':msg,'leavelist':leavelist})
	else:
		leavelist=StudentLeave.objects.filter(status="Panding_Request",registration_id=request.session['student_id'])[:1]
		return render(request,'student_leave.html',{'student':student,'leavelist':leavelist})

def leave_request_status(request):
	leavelist=StudentLeave.objects.filter(registration_id=request.session['student_id']).order_by('-id')
	return render(request,'leave_request_status.html',{'leavelist':leavelist})

def view_leave(request):
	leavelist=StudentLeave.objects.filter(status="Panding_Request").order_by('-id')
	return render(request,'view_leave.html',{'leavelist':leavelist})

def approw_leavelist(request):
	leavelist=StudentLeave.objects.filter(status="approw")
	return render(request,'approw_leave.html',{'leavelist':leavelist})

def reject_leavelist(request):
	leavelist=StudentLeave.objects.filter(status="reject")
	return render(request,'reject_leave.html',{'leavelist':leavelist})

def approw_leave(request):
	if request.method=="POST":
		student=StudentLeave.objects.get(pk=request.POST['pk'])
		student.status="approw"
		student.save()
		leavelist=StudentLeave.objects.filter(status="approw")
		return render(request,'approw_leave.html',{'leavelist':leavelist})
	else:
		leavelist=StudentLeave.objects.filter(status="approw")
		return render(request,'approw_leave.html',{'leavelist':leavelist})

def reject_leave(request):
	if request.method=="POST":
		student=StudentLeave.objects.get(pk=request.POST['pk'])
		student.status="reject"
		student.save()
		leavelist=StudentLeave.objects.filter(status="reject")
		return render(request,'reject_leave.html',{'leavelist':leavelist})
	else:
		leavelist=StudentLeave.objects.filter(status="approw")
		return render(request,'reject_leave.html',{'leavelist':leavelist})

def create_class(request):
	classlist=Createclass.objects.all().order_by('-id')[:3]
	if request.method=="POST":
		cdate=request.POST['cdate']
		ctime=request.POST['ctime']
		subject=request.POST['subject']
		class_id=request.POST['class_id']
		batch=request.POST['batch']
		organizer=request.POST['organizer']
		try:
			Createclass.objects.create(class_date=cdate,class_time=ctime,subject=subject,classtype=class_id,batch_nm=batch,organizer=organizer)
			msg="Class Created Successefully"
			return render(request,'create_class.html',{'msg':msg,'classlist':classlist})
		except:
			msg="Class Can't Registered"
			return render(request,'create_class.html',{'msg':msg,'classlist':classlist})
	else:
		return render(request,'create_class.html',{'classlist':classlist})
def class_list(request):
	classlist=Createclass.objects.all().order_by('-id')
	return render(request,'class_list.html',{'classlist':classlist})
def Insert_Suggestion(request):
	suggestionlist=Suggestion.objects.filter(registration_id=request.session['student_id']).order_by('-id')
	if request.method=="POST":
		suggestion=request.POST['suggestion']
		student_id=request.session['student_id']
		print(suggestion)
		print(student_id)
		try:
			Suggestion.objects.create(registration_id=student_id,suggestion_msg=suggestion,suggestion_date="")
			msg="Suggestion Registered Successefully"
			return render(request,'Insert_Suggestion.html',{'msg':msg})
		except:
			msg="Suggestion Not Registered"
			return render(request,'Insert_Suggestion.html',{'msg':msg})
	else:
		return render(request,'Insert_Suggestion.html',{'suggestionlist':suggestionlist})
def view_suggestion(request):
	suggestionlist=Suggestion.objects.all().order_by('-id')
	return render(request,'view_suggestion.html',{'suggestionlist':suggestionlist})