# key
## component type
* fieldName
    * definition of field
    * unit
    * required/optional
    * format
    * json type

# passives
## resistor
* tolerance
    * nominal tolerance of a resistor
    * unit: %
    * required
    * type: float
* powerRating
    * measure of power a resistor can dissipate indefinitely without degrading performance
    * unit: watts
    * optional
    * type: float
* package
    * package size of resistor
    * format: 0201, 2.0x1.0x0.5
    * optional
    * type: string
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * optional (required if package is listed)
    * type: string
* value
    * resistance value expressed as a float
    * unit: ohms
    * required
    * type: float
* humanValue
    * resistance value expressed with metric prefix
    * unit: ohms
    * optional
    * type: string

## capacitor
* package
    * package size of capacitor
    * format: 0201, 2.0x1.0x0.5
    * optional
    * type: string
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * optional (required if package is listed)
    * type: string
* value
    * capacitance value
    * unit: farads
    * type: float
    * required
* humanValue
    * capacitance value expressed with metric prefix
    * unit: farads
    * optional
    * type: string
* tolerance
    * nominal tolerance of a capacitor
    * unit: %
    * optional
    * type: float
* ratedVoltage
    * maximum voltage which may be applied continuously to a capacitor
    * type: float
    * unit: volts
    * required
* dielectric
    * dielectric material in a fixed capacitor
    * format: ceramic, C0G, NP0, X7R, Y5V, Z5U, electrolytic, tantalum, plasticFilm
    * type: string
    * optional
* polarized
    * whether a capacitor is polarized
    * type: string
    * format: yes, no
    * optional
* esr
    * equivalent series resistance of a capacitor
    * unit: ohms
    * type: float
    * optional
* maxTemp
    * maximum temperature under which a capacitor can be expected to reliably operate
    * unit: degrees C
    * type: float
    * optional
* minTemp
    * minimum temperature under which a capacitor can be expected to reliably operate
    * unit: degrees C
    * type: float
    * optional

## inductor
* package
    * package size of inductor
    * format: 0201, 2.0x1.0x0.5
    * optional
    * type: string
* packageFormat
    * format used for expressing package code
    * format: metric, imperial, length(mm)xwidth(mm)xheight(mm)
    * optional (required if package is listed)
    * type: string
* value
    * inductance value
    * unit: henries
    * type: float
    * required
* humanValue
    * inductance value expressed with metric prefix
    * unit: henries
    * optional
    * type: string
* tolerance
    * nominal tolerance of inductor
    * unit: %
    * optional
    * type: float
* isat
    * saturation current or the applied DC current at which inductance drops below a specified level, typically 30% of the specced inductance
    * unit: amps
    * type: float
    * optional
* irms
    * applied DC current that produces an inductor temperature rise of 40 deg C
    * unit: amps
    * type: float
    * optional
* dcr
    * dc resistance of an inductor
    * unit: ohms
    * type: float
    * optional
* acr
    * ac resistance of an inductor
    * type: dictionary<float><float>
    * format: dictionary<frequency><AC resistance>
    * unit: dictionary<Hz><ohms>
    * optional


# power
## ldo
* type
    * ldo type
    * format: fixed, adjustable
    * required
    * type: string
* manufacturer
    * company that manufacturers the part
    * required
    * type: string
* mpn
    * manufacturer part number
    * required
    * type: string
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* dropoutVoltage
    * nominal dropout voltage for ldo
    * unit: volts
    * optional
    * type: float
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * optional
    * type: float
* turnOnTime
    * time for output voltage to go from 10% vout nominal to 90% vout nominal
    * unit: seconds
    * optional
    * type: float

## voltage regulator
* type
    * switching voltage regulator type
    * format: buck, boost, buck-boost, other
    * required
    * type: string
* manufacturer
    * company that manufacturers the part
    * required
    * type: string
* mpn
    * manufacturer part number
    * required
    * type: string
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* voutMin
    * minimum output voltage part can regulate
    * unit: volts
    * optional
    * type: float
* voutMax
    * maximum output voltage part can regulate
    * unit: volts
    * optional
    * type: float
* fsw
    * swtiching frequency of voltage regulator
    * unit: hertz
    * optional
    * type: []float
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * optional
    * type: float
* turnOnTime
    * time for output voltage to go from 10% vout nominal to 90% vout nominal
    * unit: seconds
    * optional
    * type: float
* integratedFets
    * whether the regulator contains integrated switching mosfets
    * format: yes, no
    * optional
    * type: string

## load switch
* manufacturer
    * company that manufacturers the part
    * required
    * type: string
* mpn
    * manufacturer part number
    * required
    * type: string
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * optional
    * type: float
* turnOnTimeNominal
    * nominal time for output voltage to go from 10% vout nominal to 90% vout nominal for fixed turn-on time part
    * unit: seconds
    * optional
    * type: float
* turnOnTimeMin
    * minimum time for output voltage to go from 10% vout nominal to 90% vout nominal for variable turn-on time part
    * unit: seconds
    * optional
    * type: float
* turnOnTimeMax
    * minimum time for output voltage to go from 10% vout nominal to 90% vout nominal for variable turn-on time part
    * unit: seconds
    * optional
    * type: float
* reverseCurrentBlocking
    * whether load switch has capability to block current flow from vout to vin
    * format: yes, no
    * optional
    * type: string
* onResistance
    * nominal DC resistance of load switch when enabled
    * units: ohms
    * type: float
    * optional

## battery charger
* converterType
    * switching voltage regulator type
    * format: buck, boost, buck-boost, other
    * required
    * type: string
* chargerTopology
    * type of battery charger topology (Narrow VDC vs Hybrid Power Boost)
    * format: nvdc, hpb
    * optional
    * type: string
* manufacturer
    * company that manufacturers the part
    * required
    * type: string
* mpn
    * manufacturer part number
    * required
    * type: string
* batteryConfig
    * battery serial configurations supported by charger
    * format: 1S, 2S, 3S, 4S
    * type: []string
    * required
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* voutMin
    * minimum output voltage part can regulate
    * unit: volts
    * optional
    * type: float
* voutMax
    * maximum output voltage part can regulate
    * unit: volts
    * optional
    * type: float
* fsw
    * swtiching frequency of voltage regulator
    * unit: hertz
    * optional
    * type: []float
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * optional
    * type: float
* TCPCSupport
    * whether type-C port controller support is built in
    * optional
    * format: yes, no
    * type: string
* BC12Support
    * whether bc 1.2 detection is built in
    * optional
    * format: yes, no
    * type: string
* itegratedLoadSwitch
    * whether the charger contains integrated power path load switch(es)
    * format: yes, no
    * optional
    * type: string
* integratedFets
    * whether the charger contains integrated switching mosfets
    * format: yes, no
    * optional
    * type: string

## display backlight driver
* manufacturer
    * company that manufacturers the part
    * required
    * type: string
* mpn
    * manufacturer part number
    * required
    * type: string
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* voutMin
    * minimum output voltage part can regulate
    * unit: volts
    * optional
    * type: float
* voutMax
    * maximum output voltage part can regulate
    * unit: volts
    * optional
    * type: float
* fsw
    * swtiching frequency of voltage regulator
    * unit: hertz
    * optional
    * type: []float
* ilim
    * maximum sustained current output current under which the part will operate properly
    * unit: amps
    * optional
    * type: float
* integratedFets
    * whether the charger contains integrated switching mosfets
    * format: yes, no
    * optional
    * type: string
* currentMatchingAccuracy
    * current matching between LED strings
    * unit: percentage
    * type: float
    * optional
* numberLEDStrings
    * maximum number of LED strings supported by display driver
    * type: float
    * optional

## PMIC
* manufacturer
    * company that manufacturers the part
    * required
    * type: string
* mpn
    * manufacturer part number
    * required
    * type: string
* targetApplication
    * description of intended PMIC application (example: KBL SOC, LPDDR4 memory, etc.)
    * optional
    * type: string
* numIntegratedFetOutput
    * number of switching DC-DC converters with integrated mosfets in PMIC
    * optional
    * type: float
* numExternalFetOutput
    * number of switching DC-DC converters with external mosfets in PMIC
    * optional
    * type: float
* numLDO
    * number of integrated LDOs in PMIC
    * optional
    * type: float
* numLoadSwitch
    * number of integrated load switches in PMIC
    * optional
    * type: float
* vinMin
    * minimum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* vinMax
    * maximum input voltage under which the part can be expected to operate properly
    * unit: volts
    * optional
    * type: float
* interface
    * communication interface to host device
    * optional
    * type: float
    * format: i2c, spi, enables, etc.