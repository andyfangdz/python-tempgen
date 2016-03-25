#include <iostream>
#include <string>
#include <fstream>
#include <string>
#include "Solution.cpp"

using namespace std;

int main(int argc, char *argv[]) {
    ifstream in(argv[1]);
    ofstream out(argv[2]);

    string data;

    {% for param in params -%}
    std::getline(in, data);
    {{ param.repr }} {{ param.name }} = {{ param.decoder }}(data);
    {% endfor %}

    {{ classname }} solution;
    out << solution.{{ methodname }}(
    {%- for param in params -%}
    {{ param.name }}{% if not loop.last %}, {% endif %}
    {%- endfor %}) << std::endl;

    out.close();
    return 0;
}