import Image
import uuid
import os
import re
import datetime
import xml.sax.handler
import binascii
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.utils import simplejson
from kapai_django.gallery.models import *
from kapai_django.progression.models import *
from kapai_django.raidtool.models import *
from kapai_django.recruitment.models import *
from kapai_django import settings

class KapaiContext(RequestContext):
    def __init__(self, request, dict=None, processors=None, current_app=None):
		RequestContext.__init__(self, request, dict, current_app=current_app)
		self.dicts[0]['instances'] = Instance.objects
		self.dicts[0]['recruitment_classes'] = RecruitmentClass.objects
		self.dicts[0]['gallery'] = Gallery.objects

class DataImport:
	def process_raid_list(self, raid, data):
		# Dirty hack to fake the encoding
		data = data.replace('encoding="utf-8"', 'encoding="utf-16"')
		raid_data = xml2obj(data)
		raid.raidchar_set.all().delete()
		for group in raid_data.group:
			if group.player:
				group_slot = 0
				for player in group.player:
					char = self.get_char_by_name(player.name)
					slot = (int(group['id']) - 1) * 5 + group_slot
					# Update the character's class, if known
					if player.classname:
						recruitmentclass = self.get_recruitmentclass_by_name(player.classname)
						if recruitmentclass and not char.char_class:
							char.char_class = recruitmentclass
							char.save()
					# Populate the raid char's details
					raidchar = RaidChar(raid=raid, char=char, slot=slot)
					raidchar.save()
					group_slot = group_slot + 1
					
	
	def process_epgp_data(self, data):
		obj = simplejson.loads(data)
		roster = obj['roster']
		for roster_char in roster:
			char = self.get_char_by_name(roster_char[0])
			char.ep = roster_char[1]
			char.gp = roster_char[2]
			char.save()
		return len(roster)
		
	def get_char_by_name(self, name):
		try:
			char = Character.objects.get(name=name)
		except ObjectDoesNotExist:
			# Not found - new char
			char = Character(name=name)
			char.save()
		return char
	
	def get_recruitmentclass_by_name(self, name):
		try:
			return RecruitmentClass.objects.get(name__iexact=name)
		except ObjectDoesNotExist:
			return None

class ImageProcessor:
	def get_unique_short_name(self, original_file_name):
		return 'img/gallery/' + uuid.uuid4().hex[:8] + os.path.splitext(original_file_name)[1]
	
	def save_file_upload(self, file):
		# Get a unique filename for the file
		filename = self.get_unique_short_name(os.path.split(file.name)[1])
		# Save it to disk
		destination = open(settings.MEDIA_ROOT + filename, 'wb+')
		for chunk in file.chunks():
			destination.write(chunk)
		destination.close()
		# Return the location of the saved file
		return filename
	
	def resize_image(self, filename, max_width, max_height):
		img = Image.open(settings.MEDIA_ROOT + filename)
		img.thumbnail((max_width, max_height), Image.ANTIALIAS)
		ext = os.path.splitext(filename)
		thumb_filename = ext[0] + '_' + str(max_width) + '_' + str(max_height) + ext[1]
		img.save(settings.MEDIA_ROOT + thumb_filename, "JPEG", quality = 80, optimize = 1)
		return thumb_filename

# Utility function to convert XML to a Python object
# Downloaded from:
# http://code.activestate.com/recipes/534109-xml-to-python-data-structure/
def xml2obj(src):
    """
    A simple function to converts XML data into native Python object.
    """

    non_id_char = re.compile('[^_0-9a-zA-Z]')
    def _name_mangle(name):
        return non_id_char.sub('_', name)

    class DataNode(object):
        def __init__(self):
            self._attrs = {}    # XML attributes and child elements
            self.data = None    # child text data
        def __len__(self):
            # treat single element as a list of 1
            return 1
        def __getitem__(self, key):
            if isinstance(key, basestring):
                return self._attrs.get(key,None)
            else:
                return [self][key]
        def __contains__(self, name):
            return self._attrs.has_key(name)
        def __nonzero__(self):
            return bool(self._attrs or self.data)
        def __getattr__(self, name):
            if name.startswith('__'):
                # need to do this for Python special methods???
                raise AttributeError(name)
            return self._attrs.get(name,None)
        def _add_xml_attr(self, name, value):
            if name in self._attrs:
                # multiple attribute of the same name are represented by a list
                children = self._attrs[name]
                if not isinstance(children, list):
                    children = [children]
                    self._attrs[name] = children
                children.append(value)
            else:
                self._attrs[name] = value
        def __str__(self):
            return self.data or ''
        def __repr__(self):
            items = sorted(self._attrs.items())
            if self.data:
                items.append(('data', self.data))
            return u'{%s}' % ', '.join([u'%s:%s' % (k,repr(v)) for k,v in items])

    class TreeBuilder(xml.sax.handler.ContentHandler):
        def __init__(self):
            self.stack = []
            self.root = DataNode()
            self.current = self.root
            self.text_parts = []
        def startElement(self, name, attrs):
            self.stack.append((self.current, self.text_parts))
            self.current = DataNode()
            self.text_parts = []
            # xml attributes --> python attributes
            for k, v in attrs.items():
                self.current._add_xml_attr(_name_mangle(k), v)
        def endElement(self, name):
            text = ''.join(self.text_parts).strip()
            if text:
                self.current.data = text
            if self.current._attrs:
                obj = self.current
            else:
                # a text only node is simply represented by the string
                obj = text or ''
            self.current, self.text_parts = self.stack.pop()
            self.current._add_xml_attr(_name_mangle(name), obj)
        def characters(self, content):
            self.text_parts.append(content)

    builder = TreeBuilder()
    if isinstance(src,basestring):
        xml.sax.parseString(src, builder)
    else:
        xml.sax.parse(src, builder)
    return builder.root._attrs.values()[0]