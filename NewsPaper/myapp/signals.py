from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем декоратор сигнала
from django.core.mail import EmailMultiAlternatives
from .models import Post, Category, User, PostCategory
from django.template.loader import render_to_string


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
#  параметр instance хранит в себе только что сохранённый объект модели sender, а created — булевая переменная, которая хранит в себе True или False в зависимости от того, как вы могли догадаться, есть ли такой объект в базе или нет.
@receiver (post_save,sender=Post)
def send_new_post(sender, instance, created, **kwargs):
    new_post = Post.objects.get(id=instance.id)
    html_content= render_to_string('new_post.html',
                                   {'new_post': new_post},
                                   ) # получаем наш html
    msg = EmailMultiAlternatives(
        subject='Заголовок',
        body='сообщение',
        from_email='oOo.example@yandex.ru',
        to=['olzim@tut.by'],
    )
    msg.attach_alternative(html_content,'text/html') # добавляем html
    msg.send()

