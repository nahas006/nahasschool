from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import FormRegistration, Department, Course, Purpose  # Import your custom models

# Define your form-related lists
departments = ["Commerce", "Science", "Arts", "Computer Science", "Business"]
courses = {
    "Commerce": ["BCom", "MCom"],
    "Science": ["BSc", "MSc"],
    "Arts": ["BA", "MA"],
    "Computer Science": ["BCA", "MCA"],
    "Business": ["BBA", "MBA"],
}
purposes = ["Enquiry", "Place Order", "Return"]

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone_number = request.POST.get('phone_number')
        mail_id = request.POST.get('mail_id')
        address = request.POST.get('address')
        department = request.POST.get('department')
        course = request.POST.get('course')
        purpose = request.POST.get('purpose')

        # Check if an email already exists in your custom model
        if User.objects.filter(email=mail_id).exists():
            messages.info(request, "Email Taken")
            return redirect('form')  # Redirect to the form page


        department_obj = Department.objects.get(name=department)
        course_obj = Course.objects.get(name=course, department=department_obj)
        purpose_obj = Purpose.objects.get(name=purpose)

        user = FormRegistration(
            name=name, dob=dob, age=age, gender=gender, phone_number=phone_number,
            mail_id=mail_id, address=address, department=department_obj, course=course_obj,
            purpose=purpose_obj
        )
        user.save()

        messages.success(request, "Registration successful")
        return redirect('home/school')  # Redirect to the 'school' URL

    return render(request, 'form.html', {'departments': departments, 'purposes': purposes, 'courses': courses})