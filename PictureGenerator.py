from craiyon import Craiyon

def generateImage(prompt, fileLocation):
    generator = Craiyon() # Instantiates the api wrapper
    result = generator.generate(prompt)
    result.save_images(fileLocation) # Saves the generated images to 'current working directory/generated', you can also provide a custom path
