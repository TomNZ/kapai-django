# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RecruitmentClass'
        db.create_table('recruitment_recruitmentclass', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image_url', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('requirements', self.gf('django.db.models.fields.CharField')(default='None', max_length=20, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True)),
        ))
        db.send_create_signal('recruitment', ['RecruitmentClass'])


    def backwards(self, orm):
        
        # Deleting model 'RecruitmentClass'
        db.delete_table('recruitment_recruitmentclass')


    models = {
        'recruitment.recruitmentclass': {
            'Meta': {'object_name': 'RecruitmentClass'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requirements': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['recruitment']
