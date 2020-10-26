# pin properities
* number
    * pin or ball number as defined by datasheet
    * type: string
    * required
* name
    * name of pin as defined by datasheet
    * type: string
    * required
* functions
    * list of functions an individual pin can have
    * should map 1:1 with directions list
    * format: [i2c, spi, gpio]
    * type: []string
    * optional
* directions
    * list of directions an individual pin can have
    * should map 1:1 with functions list
    * format:
        * in (input)
        * out (output, push-pull)
        * od (output, open-drain)
        * iod (input or output, open-drain)
        * inout (input or output, push-pull)
        * analog
        * power
        * ground
    * type: []string
    * optional
* polarity
* vihMin
    * minimum voltage at which an input is read as high
    * unit: volts
    * type: float
    * optional
* vilMax
    * maximum voltage at which an input is read as low
    * unit: volts
    * type: float
    * optional
* vol
    * voltage ouput low or minimum voltage of a high output
    * unit: volts
    * type: float
    * optional
* voh
    * voltage ouput high or maximum voltage of a high output
    * unit: volts
    * type: float
    * optional
* vmax
    * maximum continuous voltage that can safely be applied to a pin
    * unit: volts
    * type: float
    * optional
* imax
    * maximum continuous current that can safely be drawn from a pin
    * unit: amps
    * type: float
    * optional
* inputLeakage
    * maximum current draw into a high impedance input pin
    * unit: amps
    * type: float
    * optional
* dcResistance
    * resistance of a pin of a connector
    * unit: ohms
    * type: float
    * optional
* voltageOptions
    * list of voltage levels supported by a pin
    * unit: volts
    * type: []float
    * optional
* floatUnused
    * description of whether pin can safely be floated if it is not used
    * format: yes, no
    * type: string
    * optional
* externalComponents
    * list of external component structures recommended to be attached to a pin
    * type: []externalComponent
    * optional

# external components
* type
    * type of component connected to a pin
    * format: resistor, capacitor, fet, diode, etc.
    * type: string
    * required
* configuration
    * electrical configuration of component connected to pin with respect to the pin
    * format: pu (pull up to power), pd (pull down to ground), series (in series)
    * type: string
    * optional
* minValue
    * minimum value of component if a range is specified
    * type: float
    * optional
* maxValue
    * minimum value of component if a range is specified
    * type: float
    * optional
* value
    * value of component if a range is not specified
    * type: float
    * optional
* componentUnit
    * unit of min/max value
    * format: ohms, micro farads, micro heneries
    * type: string
    * optional (required if min/max value are listed)