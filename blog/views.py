from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from blitzr import BlitzrClient
# Create your views here.

def post_list(request):
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  return render(request, 'blog/post_list.html', {'posts':posts})
  
def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  


  blitzr = BlitzrClient('42b3a88e99f4c3545d713b3824544370')
  artist = post.title
  artists = blitzr.search_artist(
    query=artist,
    autocomplete=True
    )

  artist_uuid = artists['results'][0]['uuid']
  print (artist_uuid)


  artists1 = blitzr.get_artist_similar(
            slug = artist)
  print (artists1)  
  artists_list = []
  for items in range(0,5):
    artists_list.append(artists1[items]['name'])
  print (artists_list)
  post.artist1 = artists_list[0]
  post.artist2 = artists_list[1]
  post.artist3 = artists_list[2]
  post.artist4 = artists_list[3]
  post.artist5 = artists_list[4]
  
  
  
  
  
  return render(request, 'blog/post_detail.html', {'post': post})
  
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #print (form.cleaned_data[title])
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
         post = form.save(commit=False)
         post.author = request.user
         post.published_date = timezone.now()
         post.save()
         #print (form.cleaned_data['my_form_field_name'])
         return redirect('post_detail', pk=post.pk)
    else:
       form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    


