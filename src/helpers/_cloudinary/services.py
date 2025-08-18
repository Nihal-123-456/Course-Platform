from django.utils.text import slugify
from django.template.loader import get_template
from django.conf import settings
import uuid

def cloudinary_image_processing(instance, field_name='image', width=200):
    image_obj = getattr(instance, field_name) # image_obj = instance.field_name
    if not image_obj:
        return None
    image_options = {
        "width": width
    }
    # self.image.image(**image_options) would return a html image tag containing the image url
    # self.image.build_url and self.image.image are part of the cloudinary package
    # creating the image url with the necessary options
    url = image_obj.build_url(**image_options)
    return url

def cloudinary_video_processing(instance, field_name='video', as_html=True, width=None, height=None, sign_url=True):
    video_obj = getattr(instance, field_name) 
    if not video_obj:
        return None
    video_options = {
        #sign_url needs to be true for private videos
        "sign_url": sign_url,
    }
    if width is not None:
        video_options['width']=width
    if height is not None:
        video_options['height']=height

    url = video_obj.build_url(**video_options)
    if as_html:
        # getting the html template and then redering it by passing the required arguments
        template = get_template('snippets/embed.html')
        html = template.render({'video_url': url, 'cloud_name':settings.CLOUDINARY_CLOUD_NAME})
        return html
    return url

# public_id_prefix, display_name, tags are all optional parameters in cloudinary
def get_public_id_prefix(instance, *args, **kwargs):
    path = instance.path
    if path is not None:
        if path.startswith('/'):
            path = path[1:]
        return path
    model_class = instance.__class__ # for getting the model class
    model_name = model_class.__name__ # for getting the model name
    model_name_slug = slugify(model_name)
    if instance.slug_id:
        return f'{model_name_slug}/{instance.slug_id}'
    return f'{model_name_slug}'

def get_display_name(instance, *args, **kwargs):
    return instance.get_display_name()

def generate_slug_id(instance, *args, **kwargs):
    unique_id = str(uuid.uuid4()).replace("-","")
    if not instance.title:
        return f"{unique_id}"
    # for creating a slug like appearance of the title
    slug = slugify(instance.title) 
    unique_id_short = unique_id[:5]
    return f'{slug}-{unique_id_short}'