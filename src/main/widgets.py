from django.forms import widgets
from django.utils.safestring import mark_safe

class CustomPictureWidget(widgets.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        default_html = super().render(name, value, attrs, **kwargs)
        img_html = ""
        if value and hasattr(value, 'url'):
            # Add a specific class and inline style so global `img { width: 100% }`
            # cannot override the preview size. Inline style has highest priority.
            img_html = mark_safe(
                f'<img src="{value.url}" class="avatar-preview" '
                f'style="width:80px;height:auto;max-width:none;border-radius:50%;" />'
            )
        # Ensure the combined HTML is marked safe so Django doesn't auto-escape it
        return mark_safe(str(img_html) + str(default_html))