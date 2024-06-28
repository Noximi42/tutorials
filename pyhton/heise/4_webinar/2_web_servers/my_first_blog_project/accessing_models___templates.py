import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_first_blog_project.settings')
setup()

from blog_application.models import BlogPost, Comment


# noinspection PyUnresolvedReferences
def main():
    blog_post = BlogPost(title='Mein erster Blog-Post', 
                         content='Hallo meine Lieben! Herzlich wilkommen zu meinem Beauty-blog!')

    blog_post.save()
    blog_post.comment_set.create(author='Bibi',
                                 e_mail_address='bibi@beatuy.de',
                                 content='Hey, das mach ich schon seit 15 Jahren!')

    blog_post.save()
    print(blog_post)

    print('-' * 100)

    blog_post = BlogPost(title='Mein zweiter Beauty-Post', 
                         content='Hallo meine Lieben! Ich bins wieder!')
    blog_post.save()
    print(BlogPost.objects.all())
    print(BlogPost.objects.filter(title__contains='zweiter'))
    print(BlogPost.objects.get(id=3).comment_set.all())
    print(Comment.objects.filter(blog_post__id=5))

if __name__ == '__main__':
    main()
