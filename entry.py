#!/usr/bin/python3
# Gtk App for Data Entry Human Worker
import lib.DatagramGenerator as report

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

  def update_poll_visualizer(self, categories: list[str]);
    '''
      Update stats visualization and make more current HTML output
      for keep up to date the information very fast.
    '''
    pass
