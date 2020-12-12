# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Blade(models.Model):
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    data = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'Blade'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Backbone(models.Model):
    statut = models.CharField(max_length=100)
    ipaddress = models.TextField(db_column='ipAddress')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'backbone'


class Coffrefort(models.Model):
    name = models.CharField(max_length=50)
    information = models.TextField(db_column='Information')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coffreFort'


class Creator(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    command = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'creator'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Knownips(models.Model):
    hostname = models.CharField(max_length=50)
    address = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'knownIps'


class Passwords(models.Model):
    information = models.CharField(db_column='Information', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passwords'


class Rapportexecution(models.Model):
    programme = models.CharField(db_column='Programme', max_length=50)  # Field name made lowercase.
    information = models.TextField(db_column='Information')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rapportExecution'


class Reseau(models.Model):
    network = models.CharField(db_column='Network', max_length=200)  # Field name made lowercase.
    programme = models.CharField(db_column='Programme', max_length=200)  # Field name made lowercase.
    nature = models.CharField(db_column='Nature', max_length=100)  # Field name made lowercase.
    information = models.TextField(db_column='Information')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reseau'


class Servcommands(models.Model):
    information = models.TextField(db_column='Information')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servCommands'


class Server(models.Model):
    ipaddress = models.CharField(db_column='ipAddress', max_length=100)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'server'


class Unknownips(models.Model):
    address = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'unknownIps'
