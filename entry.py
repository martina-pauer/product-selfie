#!/usr/bin/python3
# Gtk App for Data Entry Human Worker
from lib.clasifier import DatagramGenerator as report
from lib.clasifier import ImageClasify as img
from lib.debugger import VarsFollowing as dbg
# Initialize object for could use it with all his atributes
report = report()
img = img()
dbg = dbg()
# This procedure need be defined within the module for get access to vars
def follow(follow_name: str, kind: str, moment: str):
    dbg.set_var(follow_name, kind, f'{eval(follow_name)}')
    dbg.set_moment(follow_name, moment)
    dbg.get_following(follow_name)
# Make start following
for name in ['report', 'img', 'dbg']:
    # 3 lines saved
    follow(f'{name}', 'lib object', 'Start Line 1 to 9')   
# Use global modules for the graphicals works
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
# Make ImageRanker class before window class
class ImageRanker:
    def __init__(self):
        '''
           Gtk Graphical User Interface
        '''
        # Folder Prefix Setting
        self.prefix = './'
        # Following: 6 lines saved
        follow('ImageRanker().prefix', 'text', 'ImageRanker().__init__(): Line 26')
        # Class Atributes
        import os
        os.system(f'ls {self.prefix} >> temp.txt')
        self.image_paths: list[str] = []
        # 9 lines saved: for don't repeat lines save lines multiples of function
        follow('ImageRanker().image_paths', 'Text List', 'ImageRanker().__init__(): Line 36')
        with open('temp.txt', 'r') as image:
            line = image.readline().split(' ')
            follow('line', 'text', '"temp.txt" loop: Line 39 to 41')
            # Add Image paths when are the image type
            for content in line:
                # Foreach file name only add whose has image file extension
                if content.__contains__(img.image_type):
                    image_name: str = content.replace("\n", "").replace("\t", "")
                    self.image_paths.append(f'{self.prefix}{image_name}')
                    follow('image_name', 'text', f'Images For Loop "{content}" iteration: lines 43 to 47')
                    follow('ImageRanker().image_paths', 'Text List', f'Images For Loop "{content}" iteration: lines 43 to 47')
                    del image_name
        os.system('rm temp.txt')
        del os
        self.image_index: int = 0
        follow('ImageRanker().image_index', 'integer', 'Line 53: Image Selector Index')
        # Key: Category, Value: Category Path
        self.category_paths: dict[str, str] = {}
        follow('ImageRanker().category_paths', 'Name to Paths Text Dictionary', 'Line 56: Category Paths Getter')
        # Get categories from data/conf.csv one time for optimize
        config = open('data/conf.csv', 'r')
        follow('config', 'File Handler', 'Line 59: Open data/conf.csv as reading')
        # Add each category to categories register
        for line in config.readlines():
            if not line.__contains__('Category'):
              # Load without newlines for get the path and names right
                part: list[str] = line.replace('\n', '').split(', ')
                part[1] = f'{self.prefix}{part[1]}'
                self.category_paths.__setitem__(part[0], part[1])
                follow('part', 'Text List', 'Line 62 to 67: data/conf.csv Lines Reading')
                follow('ImageRanker().prefix', 'text', 'Line 62 to 67: data/conf.csv Lines Reading')
                follow('ImageRanker().category_paths', 'Name To Paths Text Dictionary', 'Lines 62 to 67: data/conf.csv Line Reading')
        # Make folder if not exist
        try:
            os.system(f'mkdir -p {part[1]}')
            del part, os
        except:
            pass
        # Close file to Free Out memmory and could use it in the future
        config.close()
        del config
        # Add categories to the report object
        for category_path in list(self.category_paths.values()):
            # Get the category paths for get categories
            separate: list[str] = category_path.split('/')
            report.add_category(separate[separate.__len__() - 1], category_path)
            # Make Following Over the Loop Iterations
            follow('separate', 'Text List', f'Lines 81 to 84: For Loop with category_path Equal To "{category_path}"')
          
    def move_files(self):
        '''
          From the folder where are the image move
          to the folder with image with same category.
        '''
        # Make Following
        follow('ImageRanker().image_paths', 'Text List', 'ImageRanker move_files Method')
        follow('ImageRanker().category_paths', 'Name To Paths Text Dictionary', 'ImageRanker move_files method')
        import os
        # Get images folder path and where move
        for image in self.image_paths:
         # Add exception handle for don't give systems errors
            try:
                os.system(f'mv {image} {self.category_paths[image]}')
            except:
                pass 
        # Free Out memory
        del os

    def show_graphical_interface(self):
        '''
          Render Gtk app on the screen.
        '''
        try:
            # Create Scaled Image From The Original
            scaled_preview = GdkPixbuf.Pixbuf.new_from_file_at_scale(
              filename = self.image_paths[self.image_index],
              width = 250, height = 250,
              preserve_aspect_ratio = True
            )
            follow('scaled_preview', 'Gdk Pixbuf', 'ImageRanker: Window Calling')
            follow('ImageRanker().image_paths', 'Name To Paths Text Dictionary', 'ImageRanker: Window Calling')
            # Change image scale
            maker.image.set_from_pixbuf(scaled_preview)
            follow('maker', 'Gtk.Window extended "app" object', 'ImageRanker: Window Calling')
            maker.show_all()
            Gtk.main()
        except:
            maker.close()  

    def update_poll_visualizer(self, widget: Gtk.Button):
        '''
          Update stats visualization and make more current HTML output
          for keep up to date the information very fast.
        '''
        result: str = ''
        follow('result', 'text', 'ImageRanker: Window Event update_poll_visualizer')
        # Add each one of the categories and how much images has each one
        self.move_files()
        for category in self.category_paths.keys():
            counter: int = report.count_from_folders(category)
            follow('counter', 'integer', f'ImageRanker: Window Event "{category}" For Loop')
            result = f'\n\nCategory: {category},\tImages: {counter}' 
            del counter
            follow('result', 'text', f'ImageRanker: Window Event "{category}" For Loop')
            # Show the result
        self.refresh_interface(result)
        # Make the report
        report.write_file('data/report.html')
    
    def refresh_interface(self, last_results: str):
        '''
          Auxiliar internal method for load
          next image and show last results
        '''
        if self.image_index < (self.image_paths.__len__() - 1):
            # When has the image max restar image index
            self.image_index += 1
            follow('ImageRanker().image_index', 'integer', 'ImageRanker: Refresh Graphics')
        else:
            self.image_index = 0
            follow('ImageRanker().image_index', 'integer', 'ImageRanker: Refresh Graphics')
        # Create Scaled Image From The Original
        scaled_preview = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename = self.image_paths[self.image_index],
            width = 250, height = 250,
            preserve_aspect_ratio = True
        )
        follow('ImageRanker().scaled_preview', 'Gdk Pixbuf', 'ImageRanker: Refresh Graphics')
        # Change image scale
        maker.image.set_from_pixbuf(scaled_preview)
        maker.results.set_text(last_results)
        follow('maker', 'Gtk.Window extended "app" object', 'ImageRanker: Refresh Graphics')
# Make Gtk Window
class app(Gtk.Window):
    def __init__(self):
        # Init config
        super().__init__(title = 'Image Categorizer')
        self.set_size_request(480, 480)
        # Containers
        self.big_container = Gtk.VBox()
        follow('app().big_container', 'Gtk Vertical Box Container', 'Window Making: Start')
        self.image_container = Gtk.VBox()
        follow('app().image_container', 'Gtk Vertical Box Container', 'Window Making: Start')
        self.form_container = Gtk.VBox()
        follow('app().form_container', 'Gtk Vertical Box Container', 'Window Making: Start')
        self.results_container = Gtk.VBox()
        follow('app().results_container', 'Gtk Vertical Box Container', 'Window Making: Start')
        # Image View
        self.image = Gtk.Image()
        follow('app().image', 'Gtk Image Widget', 'Window Making: Start')
        # Category Selection Menu
        self.categories_menu = Gtk.ComboBoxText()
        self.categories_menu.set_entry_text_column(0)
        follow('app().categories_menu', 'Gtk Options Selections Menu', 'Window Making: Start')
      
        for category in ImageRanker().category_paths.keys():
            self.categories_menu.append_text(category)
            follow('category', 'text', 'Window Making: Categories Adding For Loop')
        # Sender Button
        # From lines 189 to 198 don't make following for not get over information than only slow the program
        self.sender = Gtk.Button(label = 'Categorize')
        # Report View
        self.results = Gtk.Label()
        # Connect events
        self.sender.connect('clicked', ImageRanker().update_poll_visualizer)
        # Add widgets to containers
        self.form_container.pack_start(self.categories_menu, True, True, 0)
        self.form_container.pack_start(self.sender, True, True, 0)
        self.image_container.add(self.image)
        self.results_container.add(self.results)
        # Add containers to window
        for container in [self.image_container, self.form_container, self.results_container]:
            self.big_container.pack_start(container, True, True, 0)
            follow('container', 'Gtk Widgets Container', 'Window Making: Add Containers For Loop')
            follow('app().big_container', 'Gtk Widgets Container', 'Window Making: Add Containers For Loop')
          
        self.add(self.big_container)    
# Show all
maker = app()
maker.connect('delete-event', Gtk.main_quit)
follow('maker', 'Gtk.Window extended "app" object', 'main program')
# Run the program
program = ImageRanker()
follow('program', 'ImageRanker object', 'main program')
program.show_graphical_interface() 