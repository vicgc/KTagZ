from gi.repository import Nautilus, GObject

class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
	def __init__(self):
		pass

	def menu_activate_cb(self, menu, file):
		print "Menu_activate_cb", file

	def get_file_items(self, window, files):
		if len(files) != 1:
			return
		
		file = files[0]

		item = Nautilus.MenuItem(
			name='SimpleMenuExtension::Show_File_Name',
			label='Showing %s' % file.get_name(),
			tip='Showing %s' % file.get_name()
		)
		item.connect('activate', self.menu_activate_cb, file)

		return [item]
