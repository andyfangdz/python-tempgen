class {{ classname }}:
    """
    {% for param in params -%}
    @param: {{ param.name }}: {{ param.desc }}
    {% endfor -%}
    @return: {{ return.desc }}
    """
    def {{ methodname }}(self, {% for param in params -%}
            {{ param.name }}{% if not loop.last %}, {% endif %}
            {%- endfor %}):
        # {{ hint }}