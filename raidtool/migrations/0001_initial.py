# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'CharacterRole'
        db.create_table('raidtool_characterrole', (
            ('role', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('raidtool', ['CharacterRole'])

        # Adding model 'Character'
        db.create_table('raidtool_character', (
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('main_role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['raidtool.CharacterRole'])),
            ('char_class', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['recruitment.RecruitmentClass'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('raidtool', ['Character'])

        # Adding model 'CharacterBoss'
        db.create_table('raidtool_characterboss', (
            ('char', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['raidtool.Character'])),
            ('boss_detail', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['progression.BossDetail'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('boss', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['progression.Boss'])),
        ))
        db.send_create_signal('raidtool', ['CharacterBoss'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'CharacterRole'
        db.delete_table('raidtool_characterrole')

        # Deleting model 'Character'
        db.delete_table('raidtool_character')

        # Deleting model 'CharacterBoss'
        db.delete_table('raidtool_characterboss')
    
    
    models = {
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
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '100'})
        },
        'raidtool.character': {
            'Meta': {'object_name': 'Character'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'char_class': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['recruitment.RecruitmentClass']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raidtool.CharacterRole']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'raidtool.characterboss': {
            'Meta': {'object_name': 'CharacterBoss'},
            'boss': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.Boss']"}),
            'boss_detail': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['progression.BossDetail']"}),
            'char': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['raidtool.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'raidtool.characterrole': {
            'Meta': {'object_name': 'CharacterRole'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'recruitment.recruitmentclass': {
            'Meta': {'object_name': 'RecruitmentClass'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requirements': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '20', 'blank': 'True'})
        }
    }
    
    complete_apps = ['raidtool']
