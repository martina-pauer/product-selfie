class DatagramGenerator:
  
  def __init__(self):
    '''
      Generate the HTML file output
      with product variants and how
      much is used each one.

      Strcture each data about image, categories
      and counting mainly.
   '''
    self.categories: list[str] = []
    # Key Category and Count of Same category images
    self.poll: dict[str, int] = {}
    # Key Category and Folder Path
    self.folders_paths: dict[str, str] = {}

  def add_category(self, name: str, folder_path: str):
    '''
      Load a new category and his respective
      folder to move the images
    '''  
    self.folder_paths[name] = folder_path
    self.categories.append(name)

  def count_from_folders(self, category: str) -> int:
   '''
      How much images has the folder of that category.
    '''
   images: int = 0
   # Make temp file for get the text to show files
   import os
   # Use folder only for selfie images
   os.system(f'ls {self.get_path(category)} >> file_count_temp.txt')
   # Get output from file, count dots and storage result on image
   # Free out Memory because don't need module
   # Show image count
   return images

  def write_file(self, name: str):
    '''
      Write the HTML output
    '''
    prefix: str = './'
    # Prepare and proceed
    try:
      # Delete if exist old files
      import os
      os.system(f'rm {prefix}/{name}.html')
      del prefix
    except:
      pass
    # Delete uneed module for free out memory
    del os
    # Prepare content
    content: str = '<!DOCTYPE html>\n\t'
    # Page Metadata
    content += '<head>\n\t\t'
    content += '</head>\n\t'
    # Visible Part
    content += '<body>\n\t\t'
    for category in self.poll.keys:
      # Count the images in each category
      content += '<div style = "text-align: center; padding: 0.5em; border: 2px solid black; border-radius: 0.5em; background: #2535cf; color: #efefef; font-weight: 840;">\n\t\t\t'
      content += f'{category}<span style = "text-align: center; margin: 0.5 padding: 0.5em; border: 2px solid black; background: #efefef; color: black; font-weight: 840;">{self.poll[category]}</span\n'
      content += '\t\t</div>\n\t\t'
    content += '</body>\n'
    content += '<html>'
    # Create and write html
    output = open(name, 'x')
    output.write(content)
    del content
    output.close()
    del output

  def get_path(self, category: str) -> str:
    return self.folder_paths[category]

class  ImageClasify:
  def __init__(self):
    '''
      Data about where is the image,
      the category and file type (PNG, SVG, GIF, ICO, etc)
    '''  
    self.name: str = ''
    
    self.folder_path: str = './'

    self.category: str = 'Selfie'

    self.image_type: str = 'jpg'

  def set_name(self, name: str, folder_path: str):
    '''
      Name for the image and path to folder that
      contains the image for make absolute path.
    '''
    self.name = name

  def set_category(self, category: str):
      '''
        Define a category where better fits the
        image.
      '''
      self.category = category

  def get_folder(self) -> str:
      '''
        Path to the folder with the image
        is initially.
      '''
      return self.folder_path

  def get_category(self) -> str:
      '''
        Category for clasiy the image.
      '''       
      return self.category