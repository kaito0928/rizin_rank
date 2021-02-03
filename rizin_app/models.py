from django.db import models

class BantamPlayer(models.Model):

    name = models.CharField(verbose_name='名前',max_length=20)
    nickname = models.CharField(verbose_name='ニックネーム',max_length=20,null=True,blank=True)
    photo = models.ImageField(verbose_name='写真')
    birthday = models.CharField(verbose_name='生年月日',max_length=20,null=True)
    nationality = models.CharField(verbose_name='国籍',max_length=20)
    height = models.IntegerField(verbose_name='身長')
    mma_record = models.CharField(verbose_name='MMA戦績',max_length=20)
    rizin_record = models.CharField(verbose_name='RIZIN戦績',max_length=20)

    class Meta:
        verbose_name_plural = 'BantamPlayer'

    def __str__(self):
        return self.name

class FeatherPlayer(models.Model):

    name = models.CharField(verbose_name='名前',max_length=20)
    nickname = models.CharField(verbose_name='ニックネーム',max_length=20,null=True,blank=True)
    photo = models.ImageField(verbose_name='写真')
    birthday = models.CharField(verbose_name='生年月日',max_length=20,null=True)
    nationality = models.CharField(verbose_name='国籍',max_length=20)
    height = models.IntegerField(verbose_name='身長')
    mma_record = models.CharField(verbose_name='MMA戦績',max_length=20)
    rizin_record = models.CharField(verbose_name='RIZIN戦績',max_length=20)

    class Meta:
        verbose_name_plural = 'FeatherPlayer'

    def __str__(self):
        return self.name

class RightPlayer(models.Model):

    name = models.CharField(verbose_name='名前',max_length=20)
    nickname = models.CharField(verbose_name='ニックネーム',max_length=20,null=True,blank=True)
    photo = models.ImageField(verbose_name='写真')
    birthday = models.CharField(verbose_name='生年月日',max_length=20,null=True)
    nationality = models.CharField(verbose_name='国籍',max_length=20)
    height = models.IntegerField(verbose_name='身長')
    mma_record = models.CharField(verbose_name='MMA戦績',max_length=20)
    rizin_record = models.CharField(verbose_name='RIZIN戦績',max_length=20)

    class Meta:
        verbose_name_plural = 'RightPlayer'

    def __str__(self):
        return self.name


class BantamRank(models.Model):
    user = models.CharField(verbose_name='作成者', max_length=20)
    one = models.ForeignKey(BantamPlayer,related_name='bantamrank_one',on_delete=models.PROTECT)
    two = models.ForeignKey(BantamPlayer,related_name='bantamrank_two',on_delete=models.PROTECT)
    three = models.ForeignKey(BantamPlayer,related_name='bantamrank_three',on_delete=models.PROTECT)
    four = models.ForeignKey(BantamPlayer,related_name='bantamrank_four',on_delete=models.PROTECT)
    five = models.ForeignKey(BantamPlayer,related_name='bantamrank_five',on_delete=models.PROTECT)
    six = models.ForeignKey(BantamPlayer,related_name='bantamrank_six',on_delete=models.PROTECT)
    seven = models.ForeignKey(BantamPlayer,related_name='bantamrank_seven',on_delete=models.PROTECT)
    eight = models.ForeignKey(BantamPlayer,related_name='bantamrank_eight',on_delete=models.PROTECT)
    nine = models.ForeignKey(BantamPlayer,related_name='bantamrank_nine',on_delete=models.PROTECT)
    ten = models.ForeignKey(BantamPlayer,related_name='bantamrank_ten',on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'BantamRank'

    def __str__(self):
        return self.user,self.created_at

class FeatherRank(models.Model):
    user = models.CharField(verbose_name='作成者', max_length=20)
    one = models.ForeignKey(FeatherPlayer,related_name='featherrank_one',on_delete=models.PROTECT)
    two = models.ForeignKey(FeatherPlayer,related_name='featherrank_two',on_delete=models.PROTECT)
    three = models.ForeignKey(FeatherPlayer,related_name='featherrank_three',on_delete=models.PROTECT)
    four = models.ForeignKey(FeatherPlayer,related_name='featherrank_four',on_delete=models.PROTECT)
    five = models.ForeignKey(FeatherPlayer,related_name='featherrank_five',on_delete=models.PROTECT)
    six = models.ForeignKey(FeatherPlayer,related_name='featherrank_six',on_delete=models.PROTECT)
    seven = models.ForeignKey(FeatherPlayer,related_name='featherrank_seven',on_delete=models.PROTECT)
    eight = models.ForeignKey(FeatherPlayer,related_name='featherrank_eight',on_delete=models.PROTECT)
    nine = models.ForeignKey(FeatherPlayer,related_name='featherrank_nine',on_delete=models.PROTECT)
    ten = models.ForeignKey(FeatherPlayer,related_name='featherrank_ten',on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'FeatherRank'

    def __str__(self):
        return self.user,self.created_at

class RightRank(models.Model):
    user = models.CharField(verbose_name='作成者', max_length=20)
    one = models.ForeignKey(RightPlayer,related_name='right_one',on_delete=models.PROTECT)
    two = models.ForeignKey(RightPlayer,related_name='right_two',on_delete=models.PROTECT)
    three = models.ForeignKey(RightPlayer,related_name='right_three',on_delete=models.PROTECT)
    four = models.ForeignKey(RightPlayer,related_name='right_four',on_delete=models.PROTECT)
    five = models.ForeignKey(RightPlayer,related_name='right_five',on_delete=models.PROTECT)
    six = models.ForeignKey(RightPlayer,related_name='right_six',on_delete=models.PROTECT)
    seven = models.ForeignKey(RightPlayer,related_name='right_seven',on_delete=models.PROTECT)
    eight = models.ForeignKey(RightPlayer,related_name='right_eight',on_delete=models.PROTECT)
    nine = models.ForeignKey(RightPlayer,related_name='right_nine',on_delete=models.PROTECT)
    ten = models.ForeignKey(RightPlayer,related_name='right_ten',on_delete=models.PROTECT)
    created_at = models.DateTimeField(verbose_name='作成日時',auto_now_add=True)

    class Meta:
        verbose_name_plural = 'RightRank'

    def __str__(self):
        return self.user,self.created_at
