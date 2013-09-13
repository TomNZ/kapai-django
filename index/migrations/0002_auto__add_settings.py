# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('index_settings', (
            ('base_gp', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('index', ['Settings'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('index_settings')
    
    
    models = {
        'index.newsitem': {
            'Meta': {'object_name': 'NewsItem'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'when_published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'index.settings': {
            'Meta': {'object_name': 'Settings'},
            'base_gp': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }
    
    complete_apps = ['index']
