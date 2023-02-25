# importing required modules
import jinja2
import Abstract

def generateInfographic(data_dict):
    context = {
        'title' : data_dict['title'],
        'author_name' : data_dict['author_name'],
        'summary' : data_dict['summary']
        }
    
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    template = template_env.get_template("Home.html")
    output_text = template.render(context)

    with open('html_report_jinja.html', 'w', encoding="utf-8") as f:
        f.write(output_text)