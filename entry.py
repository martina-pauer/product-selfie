#!/usr/bin/python3
# Gtk App for Data Entry Human Worker
from lib.clasifier import DatagramGenerator as report
# Initialize object for could use it with all his atributes
report = report()
# Use global modules for the graphicals works
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ImageRanker:
  def __init__(self):
    '''
      Gtk Graphical User Interface
    '''
    self.image_paths: list[str] = ['./']
    # Key: Category, Value: Category Path
    self.category_paths: dict[str, str] = {}
    # Get categories from data/conf.csv one time for optimize
    config = open('data/conf.csv', 'r')
    # Add each category to categories register
    for line in config:
      if not line.__contains__('Category'):
        part: list[str] = line.split(', ')
        self.category_paths.__setitem__(part[0], part[1])
        del part
        # Make folder if not exist
        try:
          import os
          os.system(f'mkdir -p {part[1]}')
        except:
          pass

        del os
    # Close file to Free Out memmory and could use it in the future    
    config.close()
    del config
    # Add categories to the report object      
    for category_path in list(self.category_paths.values()):
      # Get the category paths for get categories
      separate: list[str] = category_path.split('/')
      report.add_category(separate[separate.__len__() - 1], category_path)    

  def move_files(self):
    '''
      From the folder where are the image move
      to the folder with image with same category.
    '''
    import os
    # Get images folder path and where move
    for image in self.image_paths:
      os.system(f'mv {image} {self.category_paths[image]}')
    # Free Out memory
    del os
    # When the file was moved restart all
    self.__init__()

  def show_graphical_interface(self, screen_width: int, screen_height: int):
    '''
      Render Gtk app on the screen.
    '''
    # Make Gtk Window
    class app(Gtk.Window):
      def __init__(self):
        # Init config
        super().__init__(title = 'Image Categorizer')
        self.set_size_request(screen_width, screen_height)
        # Containers
        self.big_container = Gtk.VBox()
        self.image_container = Gtk.VBox()
        self.form_container = Gtk.VBox()
        self.results_container = Gtk.VBox()
        # Image View
        self.image = Gtk.Image()
        # Category Selection Menu
        self.categories_menu = Gtk.ComboBoxText()
        self.categories_menu.set_entry_text_column(0)
        
        for category in ImageRanker().category_paths.keys():
          self.categories_menu.append_text(category)
        # Sender Button
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
            
        self.add(self.big_container)    
    # Show all
    maker = app()

    maker.connect('delete-event', Gtk.main_quit)
    
    try:
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
    # Add each one of the categories and how much images has each one
    for category in self.category_paths.keys():
      result += f'Category: {category},\tImages: {report.count_from_folders(category)}'
    # Show the result  
    self.show_graphical_interface(480, 480)
    # Make the report  
    report.write_file('data/report.html')
    
# Run the program
program = ImageRanker()
program.show_graphical_interface(480, 480) 