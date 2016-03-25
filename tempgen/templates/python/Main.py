from Solution import {{ classname }}
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as content_file:
        {% for param in params -%}
        {{ param.name }} = {{ param.decoder }}(content_file.readline())
        {% endfor -%}

        solution = {{ classname }}()

        with open(sys.argv[2], 'w') as output:
            out = {{ return.encoder }}(solution.{{ methodname }}({% for param in params -%}
            {{ param.name }}{% if not loop.last %}, {% endif %}
            {%- endfor %})) + "\n"
            output.write(out)
