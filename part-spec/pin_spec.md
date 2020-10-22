# pinProperities
* number
    * pin or ball number as defined by datasheet
    * datatype: string
* name
    * name of pin as defined by datasheet
    * datatype: string
* functions
    * list of functions an individual pin can have
    * should map 1:1 with directions list
    * datatype: list of strings
* directions
    * list of directions an individual pin can have
    * should map 1:1 with functions list
    * options:
        * in (input)
        * out (output, push-pull)
        * od (output, open-drain)
        * iod (input or output, open-drain)
        * inout (input or output, push-pull)
        * analog
        * power
        * ground