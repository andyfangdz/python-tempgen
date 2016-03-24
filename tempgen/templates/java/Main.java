import java.util.Scanner;
import java.io.PrintWriter;
import java.io.FileReader;
import java.io.IOException;

class Main {
    public static void main(String[] args) {
        try {
            Scanner in = new Scanner(new FileReader(args[0]));
            PrintWriter writer = new PrintWriter(args[1], "UTF-8");

            {% for param in params -%}
            {{ param.repr }} {{ param.name }} = {{ param.decoder }}(in.next());
            {% endfor -%}

            {{ classname }} solution = new {{ classname }}();

            writer.println({{ return.encoder }}(solution.{{ methodname }}({% for param in params -%}
            {{ param.name }}{% if not loop.last %}, {% endif %}
            {%- endfor %})));
            writer.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}