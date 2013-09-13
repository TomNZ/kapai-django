# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Instance'
        db.create_table('progression_instance', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('cleared_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('progression', ['Instance'])

        # Adding model 'Boss'
        db.create_table('progression_boss', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('current', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['progression.Instance'])),
            ('cleared_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('progression', ['Boss'])

        # Adding model 'BossDetail'
        db.create_table('progression_bossdetail', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ordering', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('boss', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['progression.Boss'])),
            ('cleared_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('progression', ['BossDetail'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Instance'
        db.delete_table('progression_instance')

        # Deleting model 'Boss'
        db.delete_table('progression_boss')

        # Deleting model 'BossDetail'
        db.delete_table('progression_bossdetail')
    
    
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
        }
    }
    
    complete_apps = ['progression']
