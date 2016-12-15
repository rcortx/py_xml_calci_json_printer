# py_py_xml_calci_json_printer
XML Calculator
and
Beautifies and prints JSON strings

Solutions to:

JSON Prettier:-

Write a program which takes JSON as input and gives prettified JSON

You need to read JSON from STDIN. Input gives one line of uglified JSON.
Output should be formatted JSON. Check the standard output link.
Use 2 white spaces (not‘\t’) for one indentation.
SAMPLE INPUT:

{“group” : {list : [1,2,3]}, “list” : [“a”,”b”,”c”]}

SAMPLE OUTPUT:

{

  “group” : {

      List : [
                1,
                2,
                3
             ]

  },

  “list” : [
              “a”,
              ”b”,
              ”c”
            ]

}

EXPLANATION: Input will be uglifiedjson in one line and output will be prettified format of that.

 

QUESTION 2:

XML parse plus series computation

Evaluate an expression given in XML format. Keys will be Expr- contains the entire expression. Elem – contains the digit, sum, Prod- contains two or more keys whose evaluation needs to be summed or multiplied respectively. Sub will contain 2 keys or more, where the second key onwards will have to be subtracted from the first one. Div- will contain 2 keys in which first key will need to be divided by second.

 

SAMPLE INPUT:

<expr>

<sum>

<elem>4</elem>

<elem>6</elem>

<elem>7</elem>

<elem>3</elem>

</sum>

</expr>

 

SAMPLE OUTPUT:
20
