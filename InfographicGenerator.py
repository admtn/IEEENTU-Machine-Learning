# importing required modules
import jinja2

# wkhtml path = C:\Program Files\wkhtmltopdf\bin
title = "Traumatic brain injury"
abstract = '''The decrease in mortality and improved outcome for patients with severe traumatic brain injury over the past 25 years
            can be attributed to the approach of "squeezing oxygenated blood through a swollen brain". Quantification of cerebral
            perfusion by monitoring of intracranial pressure and treatment of cerebral hypoperfusion decrease secondary injury.
            Before the patient reaches hospital, an organised trauma system that allows rapid resuscitation and transport directly
            to an experienced trauma centre significantly lowers mortality and morbidity. Only the education of medical personnel
            and the institution of trauma hospital systems can achieve further improvements in outcome for patients with
            traumatic brain injuries.'''
author_name = "Jamshid Ghajar"
article_origin = "THE LANCET, Vol 356"
date = "September 9, 2000"
research_gap = '''Other studies have shown no difference in
                survival or an improvement with use of hypertonic saline
                with or without dextran over isotonic saline for fluid
                resuscitation; most benefit was seen in the subgroup of
                patients with GCS scores below 9. Hypertonic saline may
                offer a distinct survival advantage in patients with severe
                traumatic brain injury, but definitive prospective clinical
                trials have not yet been done.'''

context = {
        'title' : title,
        'abstract' : abstract,
        'author_name' : author_name,
        'article_origin' : article_origin,
        'date' : date,
        'research_gap' : research_gap
        }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template("Home.html")
output_text = template.render(context)

with open('html_report_jinja.html', 'w') as f:
    f.write(output_text)
