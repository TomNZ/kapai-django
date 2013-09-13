# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding field 'RecruitmentClass.color'
        db.add_column('recruitment_recruitmentclass', 'color', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting field 'RecruitmentClass.color'
        db.delete_column('recruitment_recruitmentclass', 'color')
    
    
    models = {
        'recruitment.recruitmentclass': {
            'Meta': {'object_name': 'RecruitmentClass'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'requirements': ('django.db.models.fields.CharField', [], {'default': "'None'", 'max_length': '20', 'blank': 'True'})
        }
    }
    
    complete_apps = ['recruitment']
