# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

MANAGED = True

class AnswerGroups(models.Model):
    name_en = models.CharField(max_length=-1, blank=True, null=True)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)
    min_select_count = models.SmallIntegerField(blank=True, null=True)
    max_select_count = models.SmallIntegerField(blank=True, null=True)
    group_type_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'answer_groups'


class AnswerScene(models.Model):
    show_scene_id = models.IntegerField(blank=True, null=True)
    answer_seq = models.CharField(max_length=-1, blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'answer_scene'


class Answers(models.Model):
    answer_en = models.CharField(max_length=-1, blank=True, null=True)
    answer_ar = models.CharField(max_length=-1, blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'answers'


class Categories(models.Model):
    name_en = models.CharField(max_length=-1)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'categories'


class GroupType(models.Model):
    id = models.IntegerField(primary_key=True)
    name_en = models.CharField(max_length=-1, blank=True, null=True)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'group_type'


class Menu(models.Model):
    menu_name = models.CharField(max_length=-1)

    class Meta:
        managed = MANAGED
        db_table = 'menu'


class Privilage(models.Model):
    user_groups = models.ForeignKey('UserGroups', models.DO_NOTHING, blank=True, null=True)
    menu = models.ForeignKey(Menu, models.DO_NOTHING, blank=True, null=True)
    can_view = models.IntegerField()
    can_add = models.IntegerField()
    can_edit = models.IntegerField()
    can_delete = models.IntegerField()

    class Meta:
        managed = MANAGED
        db_table = 'privilage'


class QuestionAudit(models.Model):
    question = models.CharField(max_length=-1)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    audit_type = models.CharField(max_length=-1)
    audit_time = models.DateTimeField()

    class Meta:
        managed = MANAGED
        db_table = 'question_audit'


class QuestionGroups(models.Model):
    question_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    show_group_name = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'question_groups'
        unique_together = (('question_id', 'group_id'),)


class Questions(models.Model):
    question_en = models.CharField(max_length=-1)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    question_ar = models.CharField(max_length=-1)

    class Meta:
        managed = MANAGED
        db_table = 'questions'


class SceneVideoType(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'scene_video_type'


class Scenes(models.Model):
    url = models.CharField(max_length=-1)
    type_id = models.IntegerField(blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    question_id = models.IntegerField(blank=True, null=True)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'scenes'



class Tags(models.Model):
    name_en = models.CharField(max_length=-1)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'tags'


class VideoAudit(models.Model):
    name_en = models.CharField(max_length=-1)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    is_visible = models.IntegerField()
    is_delete = models.IntegerField()
    is_approved = models.IntegerField()
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video_type = models.ForeignKey('VideoTypes', models.DO_NOTHING, blank=True, null=True)
    audit_type = models.CharField(max_length=-1, blank=True, null=True)
    audit_time = models.DateTimeField()

    class Meta:
        managed = MANAGED
        db_table = 'video_audit'


class VideoCategories(models.Model):
    video_id = models.IntegerField(blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_categories'
        unique_together = (('video_id', 'category_id'),)


class VideoComments(models.Model):
    comment = models.TextField()
    commented_at = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_comments'


class VideoLikes(models.Model):
    liked_at = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_likes'


class VideoPreview(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)
    previewed_at = models.DateTimeField()

    class Meta:
        managed = MANAGED
        db_table = 'video_preview'


class VideoScenes(models.Model):
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)
    scenes = models.ForeignKey(Scenes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_scenes'


class VideoSharing(models.Model):
    shared_at = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_sharing'


class VideoTags(models.Model):
    tag = models.ForeignKey(Tags, models.DO_NOTHING, blank=True, null=True)
    video = models.ForeignKey('Videos', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_tags'
        unique_together = (('video', 'tag'),)


class VideoTypes(models.Model):
    name = models.CharField(max_length=-1)

    class Meta:
        managed = MANAGED
        db_table = 'video_types'


class VideoUsersVoting(models.Model):
    voting_date = models.DateTimeField()
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video_scenes = models.ForeignKey(VideoScenes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'video_users_voting'


class Videos(models.Model):
    name_en = models.CharField(max_length=-1)
    name_ar = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    is_visible = models.IntegerField()
    is_delete = models.IntegerField()
    is_approved = models.IntegerField()
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    video_type = models.ForeignKey(VideoTypes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = MANAGED
        db_table = 'videos'
