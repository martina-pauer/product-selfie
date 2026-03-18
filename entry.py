#!/usr/bin/python3
# Gtk App for Data Entry Human Worker
from lib.clasifier import DatagramGenerator as report
# Initialize object for could use it with all his atributes
report = report()
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
    # Class Atributes
    self.image_paths: list[str] = [f'{self.prefix}First.jpg', f'{self.prefix}Second.jpg', f'{self.prefix}Third.jpg']
    self.image_index: int = 0
    # Key: Category, Value: Category Path
    self.category_paths: dict[str, str] = {}
    # Get categories from data/conf.csv one time for optimize
    config = open('data/conf.csv', 'r')
    # Add each category to categories register
    for line in config:
      if not line.__contains__('Category'):
        # Load without newlines for get the path and names right
        part: list[str] = line.replace('\n', '').split(', ')
        part[1] = f'{self.prefix}{part[1]}'
        self.category_paths.__setitem__(part[0], part[1])
        # Make folder if not exist
        try:
          import os
          os.system(f'mkdir -p {part[1]}')
          del part
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
      # Add exception handle for don't give systems errors
      try:
        os.system(f'mv {image} {self.category_paths[image]}')
      except:
        pass  
    # Free Out memory
    del os
    # When the file was moved restart all
    self.__init__()

  def show_graphical_interface(self):
    '''
      Render Gtk app on the screen.
    '''    
    try:
      # Create Scaled Image From The Original  
      scaled_preview = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename = self.image_paths[self.image_index],
            width = 250,
            height = 250,
            preserve_aspect_ratio = True
          )
      # Change image scale
      maker.image.set_from_pixbuf(scaled_preview)
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
    self.move_files()
    for category in self.category_paths.keys():
      result += f'\n\nCategory: {category},\tImages: {report.count_from_folders(category)}' 
    # Show the result  
    self.refresh_interface(result)
    # Make the report  
    report.write_file('data/report.html')
    
  def  refresh_interface(self, last_results: str):
    '''
      Auxiliar internal method for load
      next image and show last results
    '''
    if self.image_index >= (self.image_paths.__len__() - 1):
      # When has the image max restar image index
      self.image_index = 0
    else:
      self.image_index += 1  
    # Create Scaled Image From The Original  
    scaled_preview = GdkPixbuf.Pixbuf.new_from_file_at_scale(
          filename = self.image_paths[self.image_index],
          width = 250,
          height = 250,
          preserve_aspect_ratio = True
        )
    # Change image scale
    maker.image.set_from_pixbuf(scaled_preview)
    maker.results.set_text(last_results)
# Make Gtk Window
class app(Gtk.Window):
    def __init__(self):
      # Init config
      super().__init__(title = 'Image Categorizer')
      self.set_size_request(480, 480)
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
# Run the program
program = ImageRanker()
program.show_graphical_interface() 