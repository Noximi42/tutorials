from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from .models import BlogPost, Comment


def blog_post_list_as_text(request):
    lines = []
    for bp in BlogPost.objects.all():
        lines.append(f'Blog Post "{bp.title}" from {timezone.localtime(bp.last_modified_timestamp)}:')
        lines.append(f'Content: "{bp.content}"')
        lines.append('-' * 100)

    response = HttpResponse('\n'.join(lines))
    response['Content-Type'] = 'text/plain'
    return response


def blog_post_list_via_template(request):
    return render(request, 'blog_post_list.html', context={'blog_post_list': BlogPost.objects.all()})


def blog_post_details_as_text(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    lines = [f'Blog Post "{blog_post.title}" from {timezone.localtime(blog_post.last_modified_timestamp)}:',
             f'Content: "{blog_post.content}"',
             'Comments:']
    lines += [f'    {c.author} ({c.e_mail_address}): {c.content}' for c in blog_post.comment_set.all()]

    response = HttpResponse('\n'.join(lines))
    response['Content-Type'] = 'text/plain'
    return response


def blog_post_details_via_template(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)
    return render(request, 'blog_post_details.html', context={'blog_post': blog_post})


def blog_post_details_with_form(request, blog_post_id):
    blog_post = get_object_or_404(BlogPost, id=blog_post_id)

    if 'save_comment' in request.POST:
        author = request.POST.get('author', '')
        e_mail_address = request.POST.get('e_mail_address', '')
        content = request.POST.get('content', '')
        if author and content:
            comment = blog_post.comment_set.create(author=author, e_mail_address=e_mail_address, content=content)
            comment.save()
            return HttpResponseRedirect('.')
        else:
            return render(request, 'blog_post_details_with_form.html',
                          context={'blog_post': blog_post, 'error_message': 'Please enter your name and a comment.',
                                   'author': author, 'e_mail_address': e_mail_address, 'content': content})

    return render(request, 'blog_post_details_with_form.html', context={'blog_post': blog_post})
