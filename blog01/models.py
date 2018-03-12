from django.db import models
from markdown import markdown


class Blog(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/',blank=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    #adminのブログのタイトル名にtitleのstringを返す


        #if len(self.body))>30:
        #は出来ない。
        #ただしインスタンス変数bodyを使って
        #body.__str__()とすればbodyをstring化することが出来る。.
    def Body(self):
        if len(self.body.__str__())>30:
            self.body = markdown(self.body)
            string = self.body[:30] + "..."
        else:
            self.body = markdown(self.body)
            string = self.body
        return string

# Create your models here.
