public class {{ classname }} {
    /*
     {% for param in params -%}
     * param {{ param.name }}: {{ param.desc }}
     {% endfor -%}
     * return: {{ return.desc }}
     */
    public {{ return.repr }} {{ methodname }}({% for param in params -%}
            {{ param.repr }} {{ param.name }}{% if not loop.last %}, {% endif %}
            {%- endfor %}) {
        // Your code here.
    }
};