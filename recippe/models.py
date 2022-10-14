from django.db import models

'''
수정일 : 220929
전반적인 데이터 모델 작업
사실상 새로운 모델
'''
# 데이터
# 식재료 데이터
class Ingredients(models.Model):
    name = models.CharField(max_length=50, primary_key=True, null=False)

# 단위 데이터
class Units(models.Model):
    unit = models.CharField(max_length=30, primary_key=True, null=False)

# 데이터 모델
# 사용자 정보
class User(models.Model):
    nickname = models.CharField(max_length=50, primary_key=True, null=False, unique=True)
    uid = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=30, null=False, unique=True)
    auto_login = models.BooleanField(null=False)

# 사진 게시글
class PhotoPost(models.Model):
    post_id = models.AutoField(primary_key=True, null=False, unique=True)
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="author", related_name="photopost_user")
    photo_link = models.CharField(max_length=200, null=False, unique=True)
    like_count = models.IntegerField(null=False, default=0)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)

# 레시피 게시글
class RecipePost(models.Model):
    post_id = models.AutoField(primary_key=True, null=False, unique=True)
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="author", related_name="recipepost_user")
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)
    degree_of_spicy = models.IntegerField(null=True, default=1)
    description = models.CharField(max_length=300, null=True)
    views = models.IntegerField(default=0, null=False)
    like_count = models.IntegerField(null=False, default=0)
    comment_count = models.IntegerField(null=False, default=0)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)

# 쪽지함
class Mail(models.Model):
    mail_id = models.AutoField(primary_key=True, null=False, unique=True)
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="sender", related_name="mail_user")
    receiver = models.CharField(max_length=30, null=False)
    title = models.CharField(max_length=100, null=False)
    contents = models.CharField(max_length=100, null=True)
    send_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)
    sender_check = models.BooleanField(defalut=True, null=False)
    receiver_check = models.BooleanField(default=True, null=False)

# 좋아요
class LikeInfo(models.Model):
    like_id = models.AutoField(primary_key=True, null=False, unique=True)
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="nickname", related_name="likeinfo_user")
    post_id = models.ForeignKey(RecipePost, null=False, on_delete=models.CASCADE, db_column="post_id", related_name="likeinfo_recipepost")
    post_type = models.IntegerField(null=False)

# 댓글
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, null=False, unique=True)
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="nickname", related_name="comment_user")
    post_id = models.ForeignKey(RecipePost, null=False, on_delete=models.CASCADE, db_column="post_id", related_name="comment_recipepost")
    comments = models.CharField(max_length=100, null=False)
    comment_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)

# n:n 관계를 별도의 테이블로 정의
# 냉장고재료
class Refrigerator(models.Model):
    name = models.ForeignKey(Ingredients, null=False, on_delete=models.CASCADE, db_column="name", related_name="Refrigerator")
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="nickname", related_name="Refrigerator")
    unit = models.ForeignKey(Units, null=False, on_delete=models.CASCADE, db_column="unit", related_name="Refrigerator")
    amount = models.FloatField(null=False, default=0)
    expiry_date = models.CharField(max_length=100, null=False)

# 레시피재료
class Recipe_Ingredients(models.Model):
    name = models.ForeignKey(Ingredients, null=False, on_delete=models.CASCADE, db_column="name", related_name="Recipe_Ingredients")
    post_id = models.ForeignKey(RecipePost, null=False, on_delete=models.CASCADE, db_column="post_id", related_name="Recipe_Ingredients")
    unit = models.ForeignKey(Units, null=False, on_delete=models.CASCADE, db_column="unit", related_name="Refrigerator")
    amount = models.FloatField(null=False, default=0)

# 신고
class Report(models.Model):
    nickname = models.ForeignKey(User, null=False, on_delete=models.CASCADE, db_column="reporter", related_name="report_user")
    contents = models.CharField(max_length=300, null=True)
    post_type = models.IntegerField(null=False)
    post_id = models.IntegerField(null=False)