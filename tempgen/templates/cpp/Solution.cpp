class {{ classname }} {
public:
    /*
     {% for param in params -%}
     * @param {{ param.name }}: {{ param.desc }}
     {% endfor -%}
     * @return: {{ return.desc }}
     */
    {{ return.repr }} {{ methodname }}({% for param in params -%}
            {{ param.repr }} {{ param.name }}{% if not loop.last %}, {% endif %}
            {%- endfor %}) {
        // {{ hint }}
    }
};
