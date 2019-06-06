from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def devs(request):
    return render(request, 'devs.html')

def profile(request,username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    
    posts = Post.get_profile_posts(profile.id)
    title = f'@{profile.username} Hood Updates'

    return render(request, 'profile/profile.html',{'title':title, 'profile':profile,'profile_details':profile_details,'posts':posts})
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            # print(f'post is {upload.post}')
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = PostForm()
    
    return render(request, 'profile/upload_post.html', {'form':form})

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile.html')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})

def search(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        profiles = Profile.search_profile(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'profiles':profiles})
    else:
        message = 'Enter term to search'
        return render(request, 'search.html', {'message':message})