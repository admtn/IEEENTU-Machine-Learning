# importing required modules
import jinja2
import PictureGenerator
import qrcode

def generateInfographic(data_dict):
    context = {
        'title' : data_dict['title'],
        'author_name' : data_dict['author_name'],
        'date' : data_dict['date'],
        'summary' : data_dict['summary']
        }
    
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)
    template_name_collection = ["templatequatro", "templarecinco"]

    template_name = template_name_collection[0]

    template = template_env.get_template(template_name + ".html")
    output_text = template.render(context)

    PictureGenerator.generateImage(data_dict['title'], template_name + "_files/")
    # Data to encode
    data = "https://www.google.com/search?q=" + data_dict['source']
    
    # Creating an instance of QRCode class
    qr = qrcode.QRCode(version = 1,
                    box_size = 10,
                    border = 5)
    
    # Adding data to the instance 'qr'
    qr.add_data(data)
    
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'black',
                        back_color = 'white')
    
    img.save(template_name + '_files/MyQRCode.png')

    with open('html_report_jinja.html', 'w', encoding="utf-8") as f:
        f.write(output_text)