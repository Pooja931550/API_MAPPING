from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import Student

# from .models import Person, Group,Membership

# class User_Registration(forms.ModelForm):
#     # email = forms.EmailField(required=True)
#     # pho_no = forms.IntegerField(required=True,max_value=25)

#     class Meta:
#         model = User
#         fields = "__all__"

# def is_student(x , y):
# 	return sorted(x) == sorted(y)



#############################################################


class NewUserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = '__all__'

	def save(self, commit=True):
		user = super(NewUserForm, self).save()
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		exclude = ('user',)
		fields = '__all__'

	# def clean_student(self):
	# 	data = self.cleaned_data.gat('student')
	# 	if not is_student(data, 'listen'):
	# 		raise StudentForm.ValidationError('This in not an studentfrom of listen')

	# 	return data





###################################################################











# class PersonForm(forms.ModelForm):

# 	class Meta:
# 		model = Person
# 		fields = '__all__'


# class GroupForm(forms.ModelForm):

# 	class Meta:
# 		model = Group
# 		fields = '__all__'



# class MembershipForm(forms.ModelForm):

# 	class Meta:
# 		model = Membership
# 		exclude = ('Membership',)
# 		fields = '__all__'