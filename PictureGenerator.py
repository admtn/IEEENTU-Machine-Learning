from craiyon import Craiyon

generator = Craiyon() # Instantiates the api wrapper
result = generator.generate("Traumatic brain injury")
result.save_images() # Saves the generated images to 'current working directory/generated', you can also provide a custom path