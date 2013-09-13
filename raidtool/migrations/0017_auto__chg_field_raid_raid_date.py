# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Raid.raid_date'
        db.alter_column('raidtool_raid', 'raid_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True))
    
    
    def backwards(self, orm):
        
        # Changing field 'Raid.raid_date'
        db.alter_column('raidtool_raid', 'raid_date', self.gf('django.db.models.fields.DateField')())
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'progression.boss': {
            'Meta': {'object_name': 'Boss'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'cleared_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.Instance']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        'progression.bossdetail': {
            'Meta': {'object_name': 'BossDetail'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'boss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.Boss']"}),
            'cleared_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'important': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        'progression.instance': {
            'Meta': {'object_name': 'Instance'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'cleared_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'players': ('django.db.models.fields.IntegerField', [], {'default': '25'})
        },
        'raidtool.character': {
            'Meta': {'object_name': 'Character'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'char_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recruitment.RecruitmentClass']", 'null': 'True', 'blank': 'True'}),
            'ep': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raidtool.CharacterRole']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'raidtool.characterboss': {
            'Meta': {'unique_together': "(('char', 'boss', 'boss_detail'),)", 'object_name': 'CharacterBoss'},
            'boss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.Boss']"}),
            'boss_detail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.BossDetail']", 'null': 'True', 'blank': 'True'}),
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raidtool.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'raidtool.characterrole': {
            'Meta': {'object_name': 'CharacterRole'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'raidtool.raid': {
            'Meta': {'object_name': 'Raid'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_boss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.Boss']", 'null': 'True', 'blank': 'True'}),
            'last_boss_detail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.BossDetail']", 'null': 'True', 'blank': 'True'}),
            'last_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.Instance']", 'null': 'True', 'blank': 'True'}),
            'raid_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'raidtool.raidchar': {
            'Meta': {'object_name': 'RaidChar'},
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raidtool.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raid': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raidtool.Raid']"}),
            'slot': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'recruitment.recruitmentclass': {
            'Meta': {'object_name': 'RecruitmentClass'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'FFFFFF'", 'max_length': '6'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requirements': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '20', 'blank': 'True'})
        }
    }
    
    complete_apps = ['raidtool']
