# from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# from django.urls import conf
# from django.db.models import Q
from .models import Profile
# from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
# from .utils import searchProfiles, paginateProfiles


def loginMember(request):
#     page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            member = User.objects.get(username=username)
        except:    # noqa: E722
            messages.error(request, 'Username does not exist.')

        member = authenticate(request, username=username, password=password)

        if member is not None:
            login(request, member)
        #     return redirect(request.GET['next'] if 'next' in request.GET else 'account')
            return redirect('profiles')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'members/login_register.html')


def logoutMember(request):
    logout(request)
    messages.info(request, 'Member was logged out!')
    return redirect('login')


# def registerMember(request):
#     page = 'register'
#     form = CustomUserCreationForm()

#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             member = form.save(commit=False)
#             member.username = member.username.lower()
#             member.save()

#             messages.success(request, 'User account was created!')

#             login(request, member)
#             return redirect('edit-account')

#         else:
#             messages.success(
#                 request, 'An error has occurred during registration')

#     context = {'page': page, 'form': form}
#     return render(request, 'members/login_register.html', context)


def profiles(request):
    # profiles, search_query = searchProfiles(request)
    profiles = Profile.objects.all()
    # custom_range, profiles = paginateProfiles(request, profiles, 3)
    context = {"profiles": profiles}
    return render(request, "members/profiles.html", context)


def memberProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {"profile": profile, "topSkills": topSkills, "otherSkills": otherSkills}
    return render(request, "members/member-profile.html", context)


# @login_required(login_url='login')
# def memberAccount(request):
#     profile = request.user.profile

#     skills = profile.skill_set.all()
#     projects = profile.project_set.all()

#     context = {'profile': profile, 'skills': skills, 'projects': projects}
#     return render(request, 'members/account.html', context)


# @login_required(login_url='login')
# def editAccount(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)

#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=profile)
#         if form.is_valid():
#             form.save()

#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'members/profile_form.html', context)


# @login_required(login_url='login')
# def createSkill(request):
#     profile = request.user.profile
#     form = SkillForm()

#     if request.method == 'POST':
#         form = SkillForm(request.POST)
#         if form.is_valid():
#             skill = form.save(commit=False)
#             skill.owner = profile
#             skill.save()
#             messages.success(request, 'Skill was added successfully!')
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'members/skill_form.html', context)


# @login_required(login_url='login')
# def updateSkill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     form = SkillForm(instance=skill)

#     if request.method == 'POST':
#         form = SkillForm(request.POST, instance=skill)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Skill was updated successfully!')
#             return redirect('account')

#     context = {'form': form}
#     return render(request, 'members/skill_form.html', context)


# @login_required(login_url='login')
# def deleteSkill(request, pk):
#     profile = request.user.profile
#     skill = profile.skill_set.get(id=pk)
#     if request.method == 'POST':
#         skill.delete()
#         messages.success(request, 'Skill was deleted successfully!')
#         return redirect('account')

#     context = {'object': skill}
#     return render(request, 'delete_template.html', context)https://dennisivy.teachable.com/courses/django-beginners-course/lectures/33190379


# @login_required(login_url='login')
# def inbox(request):
#     profile = request.user.profile
#     messageRequests = profile.messages.all()
#     unreadCount = messageRequests.filter(is_read=False).count()
#     context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
#     return render(request, 'members/inbox.html', context)


# @login_required(login_url='login')
# def viewMessage(request, pk):
#     profile = request.user.profile
#     message = profile.messages.get(id=pk)
#     if message.is_read == False:
#         message.is_read = True
#         message.save()
#     context = {'message': message}
#     return render(request, 'members/message.html', context)


# def createMessage(request, pk):
#     recipient = Profile.objects.get(id=pk)
#     form = MessageForm()

#     try:
#         sender = request.user.profile
#     except:
#         sender = None

#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.sender = sender
#             message.recipient = recipient

#             if sender:
#                 message.name = sender.name
#                 message.email = sender.email
#             message.save()

#             messages.success(request, 'Your message was successfully sent!')
#             return redirect('profile', pk=recipient.id)

#     context = {'recipient': recipient, 'form': form}
#     return render(request, 'members/message_form.html', context)
