#!/usr/bin/python3
# Gtk App for Data Entry Human Worker
from lib.clasifier import DatagramGenerator as report

class ImageRanker:
  def __init__(self):
    '''
      Gtk Graphical User Interface
    '''
    self.image_paths: list[str] = []
    # Key: Image Path, Value: Category Path
    self.category_paths: dict[str, str] = {}

  def move_files(self):
    '''
      From the folder where are the image move
      to the folder with image with same category.
    '''
    import os
    # Get images folder path and where move
    for image in self.image_paths:
      os.system(f'mv {image} {self.category_path[image]}')
    # Free Out memory
    del os
    # When the file was moved restart all
    self.__init__()

  def show_graphical_interface(self, screen_width: int, screen_height: int):
    '''
      Render Gtk app on the screen.
    '''  
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk
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
        self.results_comtainer = Gtk.VBox()
        # Image View
        self.image = Gtk.Image()
        # Category Selection Menu
        self.categories_menu = Gtk.ComboBoxText()
        self.categories_menu.set_entry_text_column(0)
        
        for category in ['Category 1', 'Category 2', 'Category 3']:
          self.categories_menu.append_text(category)
        # Sender Button
        self.sender = Gtk.Button(label = 'Categorize')
        # Report View
        self.results = Gtk.Label()
        # Connect events
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
    maker = app(480, 480)

    maker.connect('delete-event', Gtk.main_quit)
    
    try:
      maker.show_all()
      Gtk.main()
    except:
      maker.close()  
      del maker, app, Gtk
    # Free out RAM
    del gi, gi.repository

  def update_poll_visualizer(self, categories: list[str]):
    '''
      Update stats visualization and make more current HTML output
      for keep up to date the information very fast.
    '''
    pass
