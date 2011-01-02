# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'RImage.priority'
        db.add_column('serials_rimage', 'priority', self.gf('django.db.models.fields.IntegerField')(default='0'), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'RImage.priority'
        db.delete_column('serials_rimage', 'priority')


    models = {
        'serials.episode': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Episode'},
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'}),
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_img': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'serial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['serials.Serial']"}),
            'watch_online_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'})
        },
        'serials.news': {
            'Meta': {'ordering': "('-pub_date', 'name')", 'object_name': 'News'},
            'full_description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'short_description': ('django.db.models.fields.TextField', [], {})
        },
        'serials.rimage': {
            'Meta': {'ordering': "('-priority',)", 'object_name': 'RImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'to_url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'blank': 'True'})
        },
        'serials.serial': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Serial'},
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_img': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'origin_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'})
        }
    }

    complete_apps = ['serials']
