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
def follow(follow_name: str, moment: str):
    dbg.set_moment(follow_name, moment)
    dbg.get_following(follow_name)
# Make start following
for follow_name in ['report', 'img', 'dbg']:
    # 2 lines saved
    dbg.set_var(follow_name, 'lib object', f'{eval(follow_name)}')
    follow(f'{follow_name}', 'Start Line 1 to 9')   
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
        # Following: 5 lines saved
        dbg.set_var('ImageRanker().prefix', 'text', self.prefix)
        follow('ImageRanker().prefix', 'ImageRanker().__init__(): Line 26')
        # Class Atributes
        import os
        os.system(f'ls {self.prefix} >> temp.txt')
        self.image_paths: list[str] = []
        # 8 lines saved: for don't repeat lines save lines multiples of function
        dbg.set_var('ImageRanker().image_paths', 'Text List', f'{eval("self.image_paths")}')
        follow('ImageRanker().image_paths', 'ImageRanker().__init__(): Line 36')
        with open('temp.txt', 'r') as image:
            line = image.readline().split(' ')
            dbg.set_var('line', 'text', line)
            follow('line', '"temp.txt" loop: Line 39 to 41')
            # Add Image paths when are the image type
            for content in line:
                # Foreach file name only add whose has image file extension
                if content.__contains__(img.image_type):
                    image_name: str = content.replace("\n", "").replace("\t", "")
                    self.image_paths.append(f'{self.prefix}{image_name}')
                    dbg.set_var('image_name', 'text', image_name)
                    follow('image_name', f'Images For Loop "{content}" iteration: lines 43 to 47')
                    dbg.set_var('ImageRanker().image_paths', 'Text List', f'{eval("self.image_paths")}')
                    follow('ImageRanker().image_paths', f'Images For Loop "{content}" iteration: lines 43 to 47')
                    del image_name
        os.system('rm temp.txt')
        del os
        self.image_index: int = 0
        dbg.set_var('ImageRanker().image_index', 'integer', f'{eval("self.image_index")}')
        follow('ImageRanker().image_index', 'Line 53: Image Selector Index')
        # Key: Category, Value: Category Path
        self.category_paths: dict[str, str] = {}
        dbg.set_var('ImageRanker().category_paths', 'Name To Paths Text Dictionary', f'{eval("self.category_paths")}')
        follow('ImageRanker().category_paths', 'Line 56: Category Paths Getter')
        # Get categories from data/conf.csv one time for optimize
        config = open('data/conf.csv', 'r')
        dbg.set_var('config', 'File Handler', f'{eval("config")}')
        follow('config', 'Line 59: Open data/conf.csv as reading')
        # Add each category to categories register
        for line in config.readlines():
            if not line.__contains__('Category'):
              # Load without newlines for get the path and names right
                part: list[str] = line.replace('\n', '').split(', ')
                part[1] = f'{self.prefix}{part[1]}'
                self.category_paths.__setitem__(part[0], part[1])
                dbg.set_var('part', 'Text List', f'{eval("part")}')
                follow('part', 'Line 62 to 67: data/conf.csv Lines Reading')
                dbg.set_var('ImageRanker().prefix', 'text', self.prefix)
                follow('ImageRanker().prefix', 'Line 62 to 67: data/conf.csv Lines Reading')
                dbg.set_var('ImageRanker().category_paths', 'Name To Paths Text Dictionary', f'{eval("self.category_paths")}')
                follow('ImageRanker().category_paths', 'Lines 62 to 67: data/conf.csv Line Reading')
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
            dbg.set_var('separate', 'Text List', f'{eval("separate")}')
            follow('separate', f'Lines 81 to 84: For Loop with category_path Equal To "{category_path}"')
          
    def move_files(self):
        '''
          From the folder where are the image move
          to the folder with image with same category.
        '''
        # Make Following
        dbg.set_var('ImageRanker().image_paths', 'Text List', f'{eval("self.image_paths")}')
        dbg.set_var('ImageRanker().category_paths', 'Name To Paths Text Dictionary', f'{eval("self.category_paths")}')
        follow('ImageRanker().image_paths', 'ImageRanker move_files Method')
        follow('ImageRanker().category_paths', 'ImageRanker move_files method')
        import os
        # Get images folder path and where move
        for image in self.image_paths:
         # Add exception handle for don't give systems errors
            try:
                os.system(f'mv {image} {self.category_paths[image]}')
                dbg.set_var('image', 'text', image)
                follow('image', 'ImageRanker move_files Method')
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
            dbg.set_var('scaled_preview', 'Gdk Pixbuf', f'{eval("scaled_preview")}')
            follow('scaled_preview', 'ImageRanker: Window Calling')
            dbg.set_var('ImageRanker.image_paths', 'Name To Paths Text Dictionary', f'{eval("self.image_paths")}')
            follow('ImageRanker().image_paths', 'ImageRanker: Window Calling')
            # Change image scale
            maker.image.set_from_pixbuf(scaled_preview)
            dbg.set_var('maker', 'Gtk.Window extended "app" object', f'{eval("maker")}')
            follow('maker', 'ImageRanker: Window Calling')
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
        dbg.set_var('result', 'text', result)
        follow('result', 'ImageRanker: Window Event update_poll_visualizer')
        # Add each one of the categories and how much images has each one
        self.move_files()
        for category in self.category_paths.keys():
            counter: int = report.count_from_folders(category)
            dbg.set_var('counter', 'integer', f'{counter}')
            follow('counter', f'ImageRanker: Window Event "{category}" For Loop')
            result = f'\n\nCategory: {category},\tImages: {counter}' 
            del counter
            dbg.set_var('result', 'text', result)
            follow('result', f'ImageRanker: Window Event "{category}" For Loop')
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
            dbg.set_var('ImageRanker().image_index', 'integer', f'{self.image_index}')
            follow('ImageRanker().image_index', 'ImageRanker: Refresh Graphics')
        else:
            self.image_index = 0
            dbg.set_var('ImageRanker().image_index', 'integer', f'{self.image_index}')
            follow('ImageRanker().image_index', 'ImageRanker: Refresh Graphics')
        # Create Scaled Image From The Original
        scaled_preview_second = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename = self.image_paths[self.image_index],
            width = 250, height = 250,
            preserve_aspect_ratio = True
        )
        dbg.set_var('scaled_preview_second', 'Gdk Pixbuf', f'{eval("scaled_preview_second")}')
        follow('scaled_preview_second', 'ImageRanker: Refresh Graphics')
        # Change image scale
        maker.image.set_from_pixbuf(scaled_preview_second)
        maker.results.set_text(last_results)
        dbg.set_var('maker', 'Gtk.Window extended "app" object', f'{eval("maker")}')
        follow('maker', 'ImageRanker: Refresh Graphics')
# Make Gtk Window
class app(Gtk.Window):
    def __init__(self):
        # Init config
        super().__init__(title = 'Image Categorizer')
        self.set_size_request(480, 480)
        # Containers
        self.big_container = Gtk.VBox()
        dbg.set_var('app().big_container', 'Gtk Vertical Box Container', f'{eval("self.big_container")}')
        follow('app().big_container', 'Window Making: Start')
        self.image_container = Gtk.VBox()
        dbg.set_var('app().image_container', 'Gtk Vertical Box Container', f'{eval("self.image_container")}')
        follow('app().image_container', 'Window Making: Start')
        self.form_container = Gtk.VBox()
        dbg.set_var('app().form_container', 'Gtk Vertical Box Container', f'{eval("self.form_container")}')
        follow('app().form_container', 'Window Making: Start')
        self.results_container = Gtk.VBox()
        dbg.set_var('app().results_container', 'Gtk Vertical Box Container', f'{eval("self.results_container")}')
        follow('app().results_container', 'Window Making: Start')
        # Image View
        self.image = Gtk.Image()
        dbg.set_var('app().image', 'Gtk Image Widget', f'{eval(self.image)}')
        follow('app().image', 'Window Making: Start')
        # Category Selection Menu
        self.categories_menu = Gtk.ComboBoxText()
        self.categories_menu.set_entry_text_column(0)
        dbg.set_var('app().categories_menu', 'Gtk Options Selections Menu', f'{eval("self.categories_menu")}')
        follow('app().categories_menu', 'Window Making: Start')
      
        for category in ImageRanker().category_paths.keys():
            self.categories_menu.append_text(category)
            dbg.set_var('category', 'text', f'{eval("category")}')
            follow('category', 'Window Making: Categories Adding For Loop')
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
            dbg.set_var('container', 'Gtk Widgets Container', f'{eval("container")}')
            dbg.set_var("app().big_container", 'Gtk Widgets Container', f'{eval("self.big_container")}')
            follow('container', 'Window Making: Add Containers For Loop')
            follow('app().big_container', 'Window Making: Add Containers For Loop')
          
        self.add(self.big_container)    
# Show all
maker = app()
maker.connect('delete-event', Gtk.main_quit)
dbg.set_var('maker', 'Gtk.Window extended "app" object', f'{eval("maker")}')
follow('maker', 'main program')
# Run the program
program = ImageRanker()
dbg.set_var('program', 'ImageRanker object', f'{eval("program")}')
follow('program', 'main program')
program.show_graphical_interface() 